import os
import sys
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ---------------------------------------------------------------------------
# Resolucao de caminhos — funciona tanto local (src/app/) quanto no HF Spaces
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR  = os.path.abspath(os.path.join(BASE_DIR, '..'))

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

import predexan.preproc as pp

# ---------------------------------------------------------------------------
# Constantes do pipeline
# ---------------------------------------------------------------------------

# Limiar F1-otimizado do stacking_3c sem RFE (fonte: escolha_modelo.ipynb, acuracia 89.73%)
THRESHOLD_F1 = 0.7453494268460579

FEATURES_ROBUST = [
    'duracao_conexao_seg',
    'num_pacotes_origem',
    'num_pacotes_destino',
    'total_bytes_origem',
    'total_bytes_destino',
    'taxa_pacote',
    'carga_origem',
    'carga_destino',
    'pacotes_perdidos_origem',
    'pacotes_perdidos_destino',
    'tempo_medio_pacote_origem',
    'bytes_por_pacote_destino',
    'var_lat_pacotes_origem',
    'var_lat_pacotes_destino',
    'num_sequencia_tcp_origem',
    'num_sequencia_tcp_destino',
    'rtt_handshake_tcp',
    'tempo_syn_synack',
    'tempo_synack_ack',
    'tamanho_medio_pacotes_origem',
    'tamanho_medio_pacotes_destino',
]

FEATURES_MINMAX = [
    'tamanho_janela_tcp_origem',
    'tamanho_janela_tcp_destino',
    'profundidade_transacao_http',
    'tamanho_corpo_resposta_http',
    'conexoes_recentes_ip_porta_destino',
    'conexoes_recentes_ip_porta_origem',
    'ftp_autenticada',
    'num_comandos_ftp',
    'num_metodos_http',
    'ip_porta_origem_destino_iguais',
]

LABELS = {
    'duracao_conexao_seg':                'Duracao da conexao (seg)',
    'num_pacotes_origem':                 'Pacotes enviados (origem)',
    'num_pacotes_destino':                'Pacotes recebidos (destino)',
    'total_bytes_origem':                 'Total de bytes (origem)',
    'total_bytes_destino':                'Total de bytes (destino)',
    'taxa_pacote':                        'Taxa de pacotes',
    'carga_origem':                       'Carga da origem',
    'carga_destino':                      'Carga do destino',
    'pacotes_perdidos_origem':            'Pacotes perdidos (origem)',
    'pacotes_perdidos_destino':           'Pacotes perdidos (destino)',
    'tempo_medio_pacote_origem':          'Tempo medio entre pacotes (origem)',
    'bytes_por_pacote_destino':           'Bytes por pacote (destino)',
    'var_lat_pacotes_origem':             'Variacao de latencia (origem)',
    'var_lat_pacotes_destino':            'Variacao de latencia (destino)',
    'num_sequencia_tcp_origem':           'Numero de sequencia TCP (origem)',
    'num_sequencia_tcp_destino':          'Numero de sequencia TCP (destino)',
    'rtt_handshake_tcp':                  'RTT do handshake TCP',
    'tempo_syn_synack':                   'Tempo SYN para SYN-ACK',
    'tempo_synack_ack':                   'Tempo SYN-ACK para ACK',
    'tamanho_medio_pacotes_origem':       'Tamanho medio de pacotes (origem)',
    'tamanho_medio_pacotes_destino':      'Tamanho medio de pacotes (destino)',
    'tamanho_janela_tcp_origem':          'Janela TCP (origem)',
    'tamanho_janela_tcp_destino':         'Janela TCP (destino)',
    'profundidade_transacao_http':        'Profundidade da transacao HTTP',
    'tamanho_corpo_resposta_http':        'Tamanho do corpo HTTP (bytes)',
    'conexoes_recentes_ip_porta_destino': 'Conexoes recentes (IP/porta destino)',
    'conexoes_recentes_ip_porta_origem':  'Conexoes recentes (IP/porta origem)',
    'ftp_autenticada':                    'FTP autenticado (0=nao, 1=sim)',
    'num_comandos_ftp':                   'Numero de comandos FTP',
    'num_metodos_http':                   'Numero de metodos HTTP',
    'ip_porta_origem_destino_iguais':     'IP/porta origem = destino (0=nao, 1=sim)',
}

PROTOCOLO_OPTIONS = ['tcp', 'udp', 'outros']
SERVICO_OPTIONS   = ['-', 'dns', 'ftp', 'ftp-data', 'http', 'pop3', 'smtp', 'ssh', 'outros']
ESTADO_OPTIONS    = ['CON', 'FIN', 'INT', 'outros']

# Colunas de saida a remover para obter a ordem original das features de entrada
_LABEL_COLS = [
    'label_0', 'label_1',
    'categoria_ataque_Analysis', 'categoria_ataque_Backdoor',
    'categoria_ataque_DoS', 'categoria_ataque_Exploits',
    'categoria_ataque_Fuzzers', 'categoria_ataque_Generic',
    'categoria_ataque_Normal', 'categoria_ataque_Reconnaissance',
    'categoria_ataque_Shellcode', 'categoria_ataque_Worms',
]


# ---------------------------------------------------------------------------
# Carregamento dos artefatos (cache: carrega uma unica vez por sessao)
# ---------------------------------------------------------------------------
@st.cache_resource(show_spinner="Carregando modelo e artefatos...")
def carregar_artefatos():
    modelo = joblib.load(os.path.join(
        SRC_DIR, 'modelos', 'persistencia', 'modelos_persistentes',
        'stacking', 'stacking_3c.pkl',
    ))
    robust_sc = joblib.load(os.path.join(
        SRC_DIR, 'analise_exploratoria_pre_processamento',
        'escalonadores', 'escalonador_robusto.pkl',
    ))
    minmax_sc = joblib.load(os.path.join(
        SRC_DIR, 'analise_exploratoria_pre_processamento',
        'escalonadores', 'escalonador_minmax.pkl',
    ))
    df_ref = pd.read_parquet(os.path.join(
        SRC_DIR, 'dataset', 'pre_processado',
        'treino_pp_sem_normalizacao.parquet',
    ))

    ordem_original = df_ref.drop(columns=_LABEL_COLS, errors='ignore').columns.tolist()

    # Estatisticas por feature para definir limites e valor padrao nos widgets
    stats = {
        col: {
            'min':    float(df_ref[col].min()),
            'max':    float(df_ref[col].max()),
            'median': float(df_ref[col].median()),
        }
        for col in FEATURES_ROBUST + FEATURES_MINMAX
    }

    return modelo, robust_sc, minmax_sc, ordem_original, stats


# ---------------------------------------------------------------------------
# Pipeline de predicao
# ---------------------------------------------------------------------------
def predizer(valores_num, protocolo, servico, estado,
             modelo, robust_sc, minmax_sc, ordem_original):

    # 1. Grupo RobustScaler
    df_r = pd.DataFrame([{f: valores_num[f] for f in FEATURES_ROBUST}])
    arr_r = pp.normalizar_feature(df_r, FEATURES_ROBUST, robust_sc, transformar_apenas=True)
    df_r_norm = pd.DataFrame(arr_r, columns=FEATURES_ROBUST)

    # 2. Grupo MinMaxScaler
    df_m = pd.DataFrame([{f: valores_num[f] for f in FEATURES_MINMAX}])
    arr_m = pp.normalizar_feature(df_m, FEATURES_MINMAX, minmax_sc, transformar_apenas=True)
    df_m_norm = pd.DataFrame(arr_m, columns=FEATURES_MINMAX)

    # 3. One-hot encoding das categoricas
    cat = {}
    for opt in PROTOCOLO_OPTIONS:
        cat[f'protocolo_rede_{opt}'] = 1.0 if opt == protocolo else 0.0
    for opt in SERVICO_OPTIONS:
        cat[f'servico_conexao_{opt}'] = 1.0 if opt == servico else 0.0
    for opt in ESTADO_OPTIONS:
        cat[f'estado_conexao_{opt}'] = 1.0 if opt == estado else 0.0
    df_cat = pd.DataFrame([cat])

    # 4. Concatenar e reordenar exatamente como no treino
    df_input = pd.concat([df_r_norm, df_m_norm, df_cat], axis=1)[ordem_original]

    # 5. Inferencia
    prob = float(modelo.predict_proba(df_input)[:, 1][0])
    classificacao = 'ATAQUE' if prob >= THRESHOLD_F1 else 'NORMAL'
    return prob, classificacao


# ---------------------------------------------------------------------------
# Auxiliar: step automatico para number_input
# ---------------------------------------------------------------------------
def _step(min_v: float, max_v: float) -> float:
    rng = max_v - min_v
    if rng > 1_000_000: return 1.0
    if rng > 1_000:     return 0.1
    if rng > 10:        return 0.01
    if rng > 0.1:       return 0.001
    return 0.0001


# ---------------------------------------------------------------------------
# Interface
# ---------------------------------------------------------------------------
def main():
    st.set_page_config(
        page_title='Deteccao de Ameacas Ciberneticas',
        page_icon='shield',
        layout='wide',
    )

    modelo, robust_sc, minmax_sc, ordem_original, stats = carregar_artefatos()

    # --- Barra lateral ---
    with st.sidebar:
        st.title('Sobre o modelo')
        st.markdown(
            '**Modelo:** Stacking Ensemble (MLP 3 camadas)  \n'
            '**Dataset:** UNSW-NB15  \n'
            '**Acuracia:** 89,73%  \n'
            f'**Threshold F1-otimizado:** {THRESHOLD_F1:.4f}  \n'
            '**CPU em predicao:** 30,7% (1 vCPU)  \n'
            '\n---\n'
            'Projeto academico — PUC Minas  \n'
            'Disciplina: Pesquisa e Experimentacao em SI  \n'
            'Semestre: 2026/1'
        )

    # --- Cabecalho ---
    st.title('Deteccao de Ameacas Ciberneticas com ML')
    st.caption(
        'Preencha os dados de uma conexao de rede e clique em **Classificar** '
        'para obter a predicao do modelo Stacking Ensemble.'
    )
    st.divider()

    # --- Formulario de entrada ---
    with st.form('form_predicao'):

        # Secao 1 — Categoricas
        st.subheader('Protocolo, Servico e Estado da Conexao')
        c1, c2, c3 = st.columns(3)
        with c1:
            protocolo = st.selectbox('Protocolo de rede', options=PROTOCOLO_OPTIONS)
        with c2:
            servico = st.selectbox('Servico de conexao', options=SERVICO_OPTIONS)
        with c3:
            estado = st.selectbox('Estado da conexao', options=ESTADO_OPTIONS)

        st.divider()

        # Secao 2 — Features continuas (RobustScaler)
        st.subheader('Metricas de Fluxo e Pacotes')
        cols_r = st.columns(3)
        valores_num = {}
        for i, feat in enumerate(FEATURES_ROBUST):
            s = stats[feat]
            with cols_r[i % 3]:
                valores_num[feat] = st.number_input(
                    label=LABELS[feat],
                    min_value=s['min'],
                    max_value=s['max'],
                    value=s['median'],
                    step=_step(s['min'], s['max']),
                    format='%.4f',
                    key=feat,
                )

        st.divider()

        # Secao 3 — Features limitadas (MinMaxScaler)
        st.subheader('Metricas de Protocolo (TCP, HTTP e FTP)')
        cols_m = st.columns(3)
        for i, feat in enumerate(FEATURES_MINMAX):
            s = stats[feat]
            with cols_m[i % 3]:
                valores_num[feat] = st.number_input(
                    label=LABELS[feat],
                    min_value=s['min'],
                    max_value=s['max'],
                    value=s['median'],
                    step=_step(s['min'], s['max']),
                    format='%.4f',
                    key=feat,
                )

        st.divider()
        submitted = st.form_submit_button(
            'Classificar conexao',
            type='primary',
            use_container_width=True,
        )

    # --- Resultado ---
    if submitted:
        with st.spinner('Realizando predicao...'):
            prob, classificacao = predizer(
                valores_num, protocolo, servico, estado,
                modelo, robust_sc, minmax_sc, ordem_original,
            )

        prob_pct = prob * 100
        st.divider()
        st.subheader('Resultado da Classificacao')

        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric('Classificacao', classificacao)
        with col_b:
            st.metric('Probabilidade de ataque', f'{prob_pct:.2f}%')
        with col_c:
            st.metric('Threshold utilizado', f'{THRESHOLD_F1:.4f}')

        if classificacao == 'ATAQUE':
            st.error(
                f'ATAQUE detectado — probabilidade de {prob_pct:.2f}% '
                f'(acima do threshold de {THRESHOLD_F1:.4f})'
            )
        else:
            st.success(
                f'Trafego NORMAL — probabilidade de ataque de {prob_pct:.2f}% '
                f'(abaixo do threshold de {THRESHOLD_F1:.4f})'
            )

        st.progress(
            min(prob, 1.0),
            text=f'Probabilidade de ataque: {prob_pct:.2f}%',
        )


if __name__ == '__main__':
    main()
