# APLICAÇÃO - Teste de Modelos

# ========================================================================================================

# A) Importando dependências

# 1. Importando pacotes baixados e nativos do Python
import pandas as pd
import numpy as np
import joblib
import sys
import os

# 2. Importando pacote Predexan
caminho_predexan = os.path.abspath(os.path.join(os.getcwd(), '../'))

if caminho_predexan not in sys.path:
    sys.path.append(caminho_predexan)

print(f"Pastas encontradas: {os.listdir(caminho_predexan)}")

import predexan.preproc as pp
import predexan.metricas as pm
from predexan.deploy import Feature

# ========================================================================================================

# B) Carregando estruturas, modelos e definindo listas

# 1. Carregando escalonadores
robust = joblib.load('../analise_exploratoria_pre_processamento/escalonadores/escalonador_robusto.pkl')
minmax = joblib.load('../analise_exploratoria_pre_processamento/escalonadores/escalonador_minmax.pkl')

# 2. Carregando modelos
rl = joblib.load('../modelos/persistencia/modelos_persistentes/regressao_logistica/rl_c.pkl')
xgb = joblib.load('../modelos/persistencia/modelos_persistentes/xgboost/xgboost_c.pkl')
mlp_2c = joblib.load('../modelos/persistencia/modelos_persistentes/mlp/mlp_2c/mlp_2c.pkl')
mlp_3c = joblib.load('../modelos/persistencia/modelos_persistentes/mlp/mlp_3c/mlp_3c.pkl')
stacking_2c = joblib.load('../modelos/persistencia/modelos_persistentes/stacking/stacking_2c.pkl')
stacking_3c = joblib.load('../modelos/persistencia/modelos_persistentes/stacking/stacking_3c.pkl')

# 3. Definindo o df_treino para servir de referência para criação das Features e seus métodos
df_treino = pd.read_parquet('../dataset/pre_processado/treino_pp_sem_normalizacao.parquet')

# 4. Criação da lista que determina as Features que precisam de RobustScaler para normalização
features_robust_scaler = df_treino[['duracao_conexao_seg',
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
'tamanho_medio_pacotes_destino']]

# 5. Criação da lista que determina as Features que precisam de MinMaxScaler para normalização
features_min_max_scaler = df_treino[['tamanho_janela_tcp_origem','tamanho_janela_tcp_destino',
    'profundidade_transacao_http',
    'tamanho_corpo_resposta_http',
    'conexoes_recentes_ip_porta_destino',
    'conexoes_recentes_ip_porta_origem',
    'ftp_autenticada',
    'num_comandos_ftp',
    'num_metodos_http',
    'ip_porta_origem_destino_iguais']].columns.to_list()

# 6. Criação da lista que determina as Features categóricas
features_categoricas = [
    'protocolo_rede_outros',
    'protocolo_rede_tcp',
    'protocolo_rede_udp',
    'servico_conexao_-',
    'servico_conexao_dns',
    'servico_conexao_ftp',
    'servico_conexao_ftp-data',
    'servico_conexao_http',
    'servico_conexao_outros',
    'servico_conexao_pop3',
    'servico_conexao_smtp',
    'servico_conexao_ssh',
    'estado_conexao_CON',
    'estado_conexao_FIN',
    'estado_conexao_INT',
    'estado_conexao_outros'
]

# ========================================================================================================

# C) Instânciação das Features, com geração de resultados randomizados,  utilizando a classe Feature

# 1. Features que utilizam RobustScaler

instancias_features_robust = {}

for feature in features_robust_scaler:
    # Cria a lista com as features
    instancias_features_robust[feature] = Feature(df=df_treino, 
                          nome_feature=df_treino[feature], 
                          tipagem=np.float64, 
                          valor_min=df_treino[feature].min(), 
                          valor_max=df_treino[feature].max())

for feature in instancias_features_robust:
    print(feature)

# 2. Features que utilizam MinMaxScaler

instancias_features_minmax = {}

for feature in features_min_max_scaler:
    # Cria a lista com as features
    instancias_features_minmax[feature] = Feature(df=df_treino, 
                          nome_feature=df_treino[feature], 
                          tipagem=np.float64, 
                          valor_min=df_treino[feature].min(), 
                          valor_max=df_treino[feature].max())

for feature in features_min_max_scaler:
    print(feature)

# 3. Features Categóricas

instancias_features_categoricas = {}

for feature in features_categoricas:
    # Cria a lista com as features
    instancias_features_categoricas[feature] = Feature(df=df_treino, 
                          nome_feature=df_treino[feature], 
                          tipagem=np.float64, 
                          valor_min=df_treino[feature].min(), 
                          valor_max=df_treino[feature].max())

for feature in instancias_features_categoricas:
    print(feature)

# ========================================================================================================

# D) Geração dos valores random das Features e criação de lista que seja utilizada pelos modelos

# 1. Instâncias de Features que utilizam RobustScaler

dados_reais_robust = {}

for nome_feature, objeto_feature in instancias_features_robust.items():
    valor_real = objeto_feature.processar_valor_feature(random=True)
    dados_reais_robust[nome_feature] = valor_real

colunas_robust = list(dados_reais_robust.keys())
df_robust = pd.DataFrame([dados_reais_robust], columns=colunas_robust)

dados_robust_matriz = pp.normalizar_feature(
    df=df_robust, 
    nome_col=colunas_robust,
    escalonador=robust, 
    transformar_apenas=True
)

df_robust_normalizado = pd.DataFrame(dados_robust_matriz, columns=colunas_robust)

# 2. Instâncias de Features que utilizam MinMaxScaler
dados_reais_minmax = {}

for nome_feature, objeto_feature in instancias_features_minmax.items():
    valor_real = objeto_feature.processar_valor_feature(random=True)
    dados_reais_minmax[nome_feature] = valor_real

colunas_minmax = list(dados_reais_minmax.keys())
df_minmax = pd.DataFrame([dados_reais_minmax], columns=colunas_minmax)

dados_minmax_matriz = pp.normalizar_feature(
    df=df_minmax, 
    nome_col=colunas_minmax,
    escalonador=minmax, 
    transformar_apenas=True
)

df_minmax_normalizado = pd.DataFrame(dados_minmax_matriz, columns=colunas_minmax)

# 3. Instâncias de Features Categóricas

dados_reais_categoricos = {} 

for nome_feature, objeto_feature in instancias_features_categoricas.items():
    # Geração do valor real (que já será 0.0 ou 1.0 por conta da base pré-processada)
    valor_real = objeto_feature.processar_valor_feature(random=True)
    
    # Guarda o valor gerado no dicionário de categóricos
    dados_reais_categoricos[nome_feature] = valor_real

# Cria o DataFrame final dos categóricos
df_categoricos = pd.DataFrame([dados_reais_categoricos])

# Criação do DataFrame que guarda dados reais do usuário, que será normalizado

# 4. Criação do DataFrame que guarda os valores a serem enviados para o modelo processar e adequação da ordem das features
    # 4.1. Ordem original
ordem_original = df_treino.drop(columns=['label_0', 
                                   'label_1',
                                   'categoria_ataque_Analysis',
                                   'categoria_ataque_Backdoor',
                                   'categoria_ataque_DoS',
                                   'categoria_ataque_Exploits',
                                   'categoria_ataque_Fuzzers',
                                   'categoria_ataque_Generic',
                                   'categoria_ataque_Normal',
                                   'categoria_ataque_Reconnaissance',
                                   'categoria_ataque_Shellcode',
                                   'categoria_ataque_Worms'
                                  ]).columns.to_list()

    # 4.2. Criação do df
df_input = pd.concat([
    df_robust_normalizado, 
    df_minmax_normalizado, 
    df_categoricos], axis=1)

    # 4.3. Ordenação
df_input = df_input[ordem_original]

# ========================================================================================================

# E) Testes com os modelos

# 1. Mostrando os dados reais a serem utilizados

dados_reais_usuario = {
    **dados_reais_robust, 
    **dados_reais_minmax, 
    **dados_reais_categoricos
}

print('\n' + '='*50)
print('DADOS REAIS GERADOS PARA ESTA SIMULAÇÃO:')
print('='*50)

# Loop para printar cada feature e seu respectivo valor real de forma organizada
for feature, valor in dados_reais_usuario.items():
    # Se for float, formata com 4 casas decimais para não encher a tela de números
    if isinstance(valor, float):
        print(f" - {feature}: {valor:.4f}")
    else:
        print(f" - {feature}: {valor}")

print("="*50 + "\n")

# 2. Escolha do(s) modelo(s)

print('Escolha o modelo que quer utilizar:')
print(' 1 - Regressão Logística')
print(' 2 - XGBoost')
print(' 3 - MLP de duas camadas ocultas')
print(' 4 - MLP de três camadas ocultas')
print(' 5 - Stacking com MLP de duas camadas ocultas')
print(' 6 - Stacking com MLP de três camadas ocultas')
print(' 7 - Todos ao mesmo tempo para comparação')

escolha = int(input('Digite o número da sua escolha: '))

if escolha < 1 or escolha > 7:
    print('Escolha inválida! Por favor, escolha um número entre 1 e 7.')

else:
    if escolha == 1 or escolha == 7:
        pred_rl = rl.predict_proba(df_input)[:, 1][0] * 100
        print(f'Regressão Logística: A probabilidade da amostra de ter sido um ataque é de {pred_rl:.2f}%')

    if escolha == 2 or escolha == 7:
        pred_xgb = xgb.predict_proba(df_input)[:, 1][0] * 100
        print(f'XGBoost : A probabilidade da amostra de ter sido um ataque é de {pred_xgb:.2f}%')

    if escolha == 3 or escolha == 7:
        pred_mlp_2c = mlp_2c.predict_proba(df_input)[:, 1][0] * 100
        print(f'MLP de duas camadas ocultas: A probabilidade da amostra de ter sido um ataque é de {pred_mlp_2c:.2f}%')

    if escolha == 4 or escolha == 7:
        pred_mlp_3c = mlp_3c.predict_proba(df_input)[:, 1][0] * 100
        print(f'MLP de três camadas ocultas: A probabilidade da amostra de ter sido um ataque é de {pred_mlp_3c:.2f}%')

    if escolha == 5 or escolha == 7:
        pred_stacking_2c = stacking_2c.predict_proba(df_input)[:, 1][0] * 100
        print(f'Stacking com MLP de duas camadas ocultas: A probabilidade da amostra de ter sido um ataque é de {pred_stacking_2c:.2f}%')

    if escolha == 6 or escolha == 7:
        pred_stacking_3c = stacking_3c.predict_proba(df_input)[:, 1][0] * 100 # CORRIGIDO: nome da variável
        print(f'Stacking com MLP de três camadas ocultas: A probabilidade da amostra de ter sido um ataque é de {pred_stacking_3c:.2f}%')