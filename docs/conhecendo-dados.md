# Conhecendo os Dados
## Análise Descritiva e Exploratória — UNSW-NB15 (Training Set)

---

## 1. Visão Geral do Dataset

O dataset utilizado é o **UNSW_NB15_training-set**, carregado em formato `.parquet` via `pd.read_parquet()`. O conjunto conta com **175.341 registros** e **36 colunas**, distribuídas entre variáveis numéricas e categóricas, sem nenhum valor nulo em qualquer atributo.

A ausência completa de valores nulos elimina a necessidade de imputação ou remoção de registros, permitindo que toda a análise exploratória seja realizada sobre a base integral.

### 1.1 Importação das Bibliotecas

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from sklearn.preprocessing import OrdinalEncoder
```

### 1.2 Carregamento dos Dados

```python
df = pd.read_parquet('UNSW_NB15_training-set.parquet')
df.head()
```

A inspeção via `df.info()` confirma 175.341 entradas, zero valores nulos e uso de ~17,1 MB de memória, evidenciando o uso eficiente de tipos compactados (`float32`, `int8`, `int16`, `category`).

```
<class 'pandas.DataFrame'>
RangeIndex: 175341 entries, 0 to 175340
Data columns (total 36 columns):
 #   Column             Non-Null Count   Dtype
---  ------             --------------   -----
 0   dur                175341 non-null  float32
 1   proto              175341 non-null  category
 2   service            175341 non-null  category
 3   state              175341 non-null  category
...
 34  attack_cat         175341 non-null  category
 35  label              175341 non-null  int8
dtypes: category(4), float32(11), int16(9), int32(3), int64(2), int8(7)
memory usage: 17.1 MB
```

### 1.3 Renomeação dos Atributos

Os 36 atributos foram renomeados para o português via `df.rename()`, facilitando a leitura durante a análise exploratória:

```python
df = df.rename(columns={
    'dur':                'duracao_conexao_seg',
    'proto':              'protocolo_rede',
    'service':            'servico_conexao',
    'state':              'estado_conexao',
    'spkts':              'num_pacotes_origem',
    'dpkts':              'num_pacotes_destino',
    'sbytes':             'total_bytes_origem',
    'dbytes':             'total_bytes_destino',
    'rate':               'taxa_pacote',
    'sload':              'carga_origem',
    'dload':              'carga_destino',
    'sloss':              'pacotes_perdidos_origem',
    'dloss':              'pacotes_perdidos_destino',
    'sinpkt':             'tempo_medio_pacote_origem',
    'dinpkt':             'bytes_por_pacote_destino',
    'sjit':               'var_lat_pacotes_origem',
    'djit':               'var_lat_pacotes_destino',
    'swin':               'tamanho_janela_tcp_origem',
    'stcpb':              'num_sequencia_tcp_origem',
    'dtcpb':              'num_sequencia_tcp_destino',
    'dwin':               'tamanho_janela_tcp_destino',
    'tcprtt':             'rtt_handshake_tcp',
    'synack':             'tempo_syn_synack',
    'ackdat':             'tempo_synack_ack',
    'smean':              'tamanho_medio_pacotes_origem',
    'dmean':              'tamanho_medio_pacotes_destino',
    'trans_depth':        'profundidade_transacao_http',
    'response_body_len':  'tamanho_corpo_resposta_http',
    'ct_src_dport_ltm':   'conexoes_recentes_ip_porta_destino',
    'ct_dst_sport_ltm':   'conexoes_recentes_ip_porta_origem',
    'is_ftp_login':       'ftp_autenticada',
    'ct_ftp_cmd':         'num_comandos_ftp',
    'ct_flw_http_mthd':   'num_metodos_http',
    'is_sm_ips_ports':    'ip_porta_origem_destino_iguais',
    'attack_cat':         'categoria_ataque',
    'label':              'label'
})
```

### 1.4 Dicionário de Atributos

| Nome Renomeado | Nome Original | Tipo | Descrição |
|:---|:---|:---|:---|
| `duracao_conexao_seg` | `dur` | float32 | Duração total da conexão (segundos) |
| `protocolo_rede` | `proto` | category | Protocolo de rede (tcp, udp, arp…) |
| `servico_conexao` | `service` | category | Serviço de rede utilizado (http, dns, ftp…) |
| `estado_conexao` | `state` | category | Estado da conexão (FIN, INT, CON…) |
| `num_pacotes_origem` | `spkts` | int16 | Nº de pacotes enviados pela origem |
| `num_pacotes_destino` | `dpkts` | int16 | Nº de pacotes enviados pelo destino |
| `total_bytes_origem` | `sbytes` | int32 | Total de bytes da origem |
| `total_bytes_destino` | `dbytes` | int32 | Total de bytes do destino |
| `taxa_pacote` | `rate` | float32 | Taxa de pacotes por segundo |
| `carga_origem` | `sload` | float32 | Carga de bits/s da origem |
| `carga_destino` | `dload` | float32 | Carga de bits/s do destino |
| `pacotes_perdidos_origem` | `sloss` | int16 | Pacotes retransmitidos pela origem |
| `pacotes_perdidos_destino` | `dloss` | int16 | Pacotes retransmitidos pelo destino |
| `tempo_medio_pacote_origem` | `sinpkt` | float32 | Intervalo médio entre pacotes (origem) |
| `bytes_por_pacote_destino` | `dinpkt` | float32 | Bytes médios por pacote (destino) |
| `var_lat_pacotes_origem` | `sjit` | float32 | Jitter (variação de latência) na origem |
| `var_lat_pacotes_destino` | `djit` | float32 | Jitter (variação de latência) no destino |
| `tamanho_janela_tcp_origem` | `swin` | int16 | Tamanho da janela TCP da origem |
| `num_sequencia_tcp_origem` | `stcpb` | int64 | Número de sequência TCP da origem |
| `num_sequencia_tcp_destino` | `dtcpb` | int64 | Número de sequência TCP do destino |
| `tamanho_janela_tcp_destino` | `dwin` | int16 | Tamanho da janela TCP do destino |
| `rtt_handshake_tcp` | `tcprtt` | float32 | RTT do handshake TCP |
| `tempo_syn_synack` | `synack` | float32 | Tempo entre SYN e SYN-ACK |
| `tempo_synack_ack` | `ackdat` | float32 | Tempo entre SYN-ACK e ACK |
| `tamanho_medio_pacotes_origem` | `smean` | int16 | Tamanho médio dos pacotes (origem) |
| `tamanho_medio_pacotes_destino` | `dmean` | int16 | Tamanho médio dos pacotes (destino) |
| `profundidade_transacao_http` | `trans_depth` | int16 | Profundidade da transação HTTP |
| `tamanho_corpo_resposta_http` | `response_body_len` | int32 | Tamanho do corpo de resposta HTTP |
| `conexoes_recentes_ip_porta_destino` | `ct_src_dport_ltm` | int8 | Conexões recentes por IP/porta de destino |
| `conexoes_recentes_ip_porta_origem` | `ct_dst_sport_ltm` | int8 | Conexões recentes por IP/porta de origem |
| `ftp_autenticada` | `is_ftp_login` | int8 | Indica se sessão FTP foi autenticada |
| `num_comandos_ftp` | `ct_ftp_cmd` | int8 | Nº de comandos FTP na sessão |
| `num_metodos_http` | `ct_flw_http_mthd` | int8 | Nº de métodos HTTP no fluxo |
| `ip_porta_origem_destino_iguais` | `is_sm_ips_ports` | int8 | IP/porta origem = destino? |
| `categoria_ataque` | `attack_cat` | category | Categoria do ataque — **target multiclasse** |
| `label` | `label` | int8 | Normal (0) ou malicioso (1) — **target binário** |

---

## 2. Análise Estatística Univariada

Cada atributo numérico foi analisado individualmente por meio das seguintes funções customizadas:

```python
# Iteração sobre todos os atributos numéricos
coluna_alvo = ['duracao_conexao_seg', 'taxa_pacote', ...]  # lista completa de atributos

funcoes_medidas = [
    calcular_tendencia_central,
    calcular_dispersao,
    calcular_quartis,
    detectar_outliers,
    regra_ouro
]

for col in coluna_alvo:
    gerar_histograma(col)   # histograma + KDE + curva normal
    gerar_boxplot(col)      # boxplot horizontal com limites IQR
    for funcao in funcoes_medidas:
        funcao(col)
```

As métricas calculadas para cada atributo foram:

- **Tendência central:** média aritmética, mediana e moda
- **Dispersão:** desvio padrão, coeficiente de variação (CV) e amplitude
- **Posição:** quartis Q1 (25%), Q2 (50%) e Q3 (75%)
- **Outliers:** limites inferior e superior via IQR (fator 1,5), com contagem e percentual
- **Regra dos 68-95-99,7%:** intervalos de 1σ, 2σ e 3σ em torno da média

### 2.1 Padrão de Distribuição

Nenhum dos 36 atributos segue distribuição normal. Em todos os histogramas, a curva gaussiana se apresenta severamente achatada em relação ao KDE real, e os intervalos da regra dos 68-95-99,7% geram valores negativos fisicamente impossíveis (como durações ou bytes negativos).

Esse comportamento é esperado em dados de tráfego de rede, onde a grande maioria dos valores se concentra próxima a zero e longas caudas à direita são formadas por eventos extremos — ataques volumétricos, sessões de transferência de grandes arquivos ou picos de instabilidade.

### 2.2 Comportamento das Variáveis de Handshake TCP

As variáveis `rtt_handshake_tcp`, `tempo_syn_synack` e `tempo_synack_ack` apresentam alta assimetria positiva, com mais de 95% dos valores concentrados próximos a zero e uma cauda direita expressiva. Essa cauda representa conexões com dificuldade de estabelecimento, frequentemente associadas a tentativas de ataque ou sobrecarga de rede.

### 2.3 Presença de Outliers

A maioria das variáveis de tráfego exibiu presença significativa de outliers pelo critério IQR. Os atributos com maior percentual de valores discrepantes foram `carga_destino`, `var_lat_pacotes_origem` e `pacotes_perdidos_origem`. Atributos categóricos binários e os números de sequência TCP não apresentaram outliers dentro dos limites estatísticos calculados.

### 2.4 Decisão Sobre os Outliers

**Os outliers foram mantidos integralmente.** No domínio de cibersegurança e análise de redes, valores extremos não representam erros de medição — são assinaturas de comportamentos anômalos, picos de instabilidade ou eventos de ataque real. Removê-los implicaria descartar exatamente as amostras mais relevantes para o objetivo do projeto.

---

## 2. Descrição dos Achados

### 2.1 Centralidade dos Dados

O achado mais relevante relativo à tendência central é a **discrepância sistemática entre média e mediana** na grande maioria dos atributos numéricos. Em variáveis como `carga_origem`, `taxa_pacote` e `carga_destino`, a média é substancialmente superior à mediana, evidenciando forte assimetria positiva causada por outliers de alta magnitude. Esse comportamento é típico de distribuições log-normais observadas em métricas de tráfego de rede.

O atributo `label` (binário: 0 ou 1) apresenta média de 0,50 e mediana de 0,00, indicando que aproximadamente metade dos registros são tráfego normal e metade são ataques — um dataset razoavelmente balanceado para classificação binária.

### 2.2 Correlação entre os Atributos

A **Matriz de Correlação de Spearman** foi escolhida por ser robusta para dados não normais e relações não lineares. O dataset foi dividido ao meio para facilitar a visualização dos heatmaps:

```python
colunas = df.columns.to_list()
targets = colunas[-2:]          # ['categoria_ataque', 'label']
metade = len(colunas) // 2

colunas_parte1 = colunas[:metade] + targets
colunas_parte2 = colunas[metade:]

# Heatmap - primeira metade
matriz_correlacao = df[colunas_parte1].corr(method='spearman')
plt.figure(figsize=(30, 30))
sns.heatmap(matriz_correlacao, annot=True, cmap='Blues')
plt.show()

# Heatmap - segunda metade
matriz_correlacao = df[colunas_parte2].corr(method='spearman')
plt.figure(figsize=(30, 30))
sns.heatmap(matriz_correlacao, annot=True, cmap='Blues')
plt.show()
```

A análise revelou o seguinte padrão de correlações com os targets:

| Feature | `categoria_ataque` | `label` | Tipo de Correlação |
|:---|:---:|:---:|:---|
| `tempo_synack_ack` | -0.26 | **0.40** | Forte positiva com label |
| `rtt_handshake_tcp` | -0.25 | **0.39** | Forte positiva com label |
| `tempo_syn_synack` | -0.25 | **0.38** | Forte positiva com label |
| `estado_conexao` | -0.23 | **0.37** | Forte positiva com label |
| `bytes_por_pacote_destino` | -0.16 | **0.32** | Moderada positiva |
| `var_lat_pacotes_origem` | -0.15 | **0.30** | Moderada positiva |
| `tempo_medio_pacote_origem` | -0.17 | **0.31** | Moderada positiva |
| `duracao_conexao_seg` | -0.21 | 0.28 | Moderada positiva |
| `carga_destino` | **0.26** | **-0.56** | Forte negativa com label |
| `tamanho_medio_pacotes_destino` | 0.07 | **-0.38** | Forte negativa com label |
| `taxa_pacote` | 0.16 | **-0.31** | Moderada negativa |
| `carga_origem` | 0.12 | **-0.29** | Moderada negativa |
| `total_bytes_destino` | 0.05 | -0.26 | Moderada negativa |
| `num_sequencia_tcp_origem` | -0.001 | 0.003 | Nula |
| `conexoes_recentes_ip_porta_destino` | -0.005 | -0.012 | Nula |
| `categoria_ataque` | 1 | -0.66 | Referência |
| `label` | -0.66 | 1 | Referência |

#### Correlações Fortes (|r| ≥ 0,35)

O maior destaque reside nas variáveis de temporização do handshake TCP. `tempo_synack_ack` (r = 0,40), `rtt_handshake_tcp` (r = 0,39) e `tempo_syn_synack` (r = 0,38) demonstram ser os indicadores mais robustos de anomalia — tentativas de invasão e ataques de negação de serviço causam gargalos imediatos no processo de estabelecimento de conexão, tornando a latência de handshake um preditor mais eficaz do que a simples duração total da sessão.

Na direção oposta, `carga_destino` (r = -0,56) apresenta a correlação negativa mais forte de todo o conjunto. Durante um evento de ataque, a eficiência na entrega de dados úteis cai severamente — possivelmente pela saturação do link com pacotes de controle ou pela interrupção de fluxos de aplicação.

#### Correlações Moderadas (0,20 ≤ |r| < 0,35)

`taxa_pacote` (-0,31), `var_lat_pacotes_origem` (0,30), `bytes_por_pacote_destino` (0,32) e `carga_origem` (-0,29) apresentam relevância estatística e devem compor o conjunto de features do modelo.

#### Correlações Fracas ou Nulas

`num_sequencia_tcp_origem`, `num_sequencia_tcp_destino`, `tamanho_janela_tcp_origem` e `conexoes_recentes_ip_porta_destino` exibem correlações próximas a zero, evidenciando baixo poder discriminativo isolado neste dataset.

### 2.3 Implicações para a Modelagem

A discrepância entre as correlações de `label` (binário) e `categoria_ataque` (multiclasse) é reveladora: os sinais de atraso e carga são excelentes para **detectar a existência de uma ameaça**, mas a distinção entre diferentes tipos de ataque exigirá combinações mais complexas de atributos.

Os metadados de protocolos HTTP (`profundidade_transacao_http`, `num_metodos_http`) e FTP (`ftp_autenticada`, `num_comandos_ftp`) apresentam correlações moderadas, mas serão essenciais para a especialização do modelo multiclasse. Diante disso, `label` se mostra como o target com maior previsibilidade imediata, enquanto `categoria_ataque` pode requerer algoritmos com maior capacidade de representação não linear.

---

## 3. Ferramentas Utilizadas

Todas as análises foram conduzidas com a linguagem **Python**, executadas em ambiente **Jupyter Notebook** para facilitar a iteração interativa e a visualização inline dos gráficos.

| Ferramenta / Biblioteca | Aplicação neste projeto |
|:---|:---|
| **Python 3.x** | Linguagem principal de toda a análise exploratória |
| **Pandas** | Criação e manipulação do DataFrame, renomeação de colunas, `value_counts`, filtragens |
| **NumPy** | Operações numéricas, cálculo de percentis e suporte matricial |
| **Matplotlib** | Geração de histogramas com KDE e curva de distribuição normal |
| **Seaborn** | Boxplots e heatmaps da Matriz de Correlação de Spearman |
| **SciPy (`stats.norm`)** | Cálculo e sobreposição da curva gaussiana nos histogramas |
| **scikit-learn (`OrdinalEncoder`)** | Encoding das variáveis categóricas para cálculo da correlação de Spearman |
| **Jupyter Notebook** | Ambiente de execução iterativa com visualização inline dos gráficos |

### Funções Customizadas Desenvolvidas

Para padronizar e automatizar a análise de todos os 36 atributos, foram desenvolvidas as seguintes funções auxiliares (código-fonte completo disponível em `src/`):

| Função | Descrição |
|:---|:---|
| `gerar_histograma(col)` | Histograma com KDE e curva normal via `scipy.stats.norm` |
| `gerar_boxplot(col)` | Boxplot horizontal com limites IQR |
| `calcular_tendencia_central(col)` | Imprime média, mediana e moda |
| `calcular_dispersao(col)` | Imprime desvio padrão, CV e amplitude |
| `calcular_quartis(col)` | Imprime Q1, Q2 (mediana) e Q3 |
| `detectar_outliers(col)` | Calcula limites IQR, conta e exibe percentual de outliers |
| `regra_ouro(col)` | Aplica a regra dos 68-95-99,7% e imprime os intervalos |

As funções de medição foram agrupadas em uma lista `funcoes_medidas` e aplicadas iterativamente sobre cada coluna, garantindo consistência metodológica em toda a análise.


