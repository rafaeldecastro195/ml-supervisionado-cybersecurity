# Preparação dos dados

Nesta etapa, estruturamos o pipeline de pré-processamento aplicado aos conjuntos de treino (treino_pre_proc.ipynb) e de teste (teste_pre_proc.ipynb), adaptando os dados de tráfego de rede para os modelos preditivos de cibersegurança.
    • Limpeza de Dados: Validamos a consistência e a integridade das variáveis. Registos duplicados foram tratados na fase de saneamento por meio de remoção estruturada , eliminando ruídos que pudessem prejudicar o treino.
    • Transformação e Normalização: Atributos numéricos de tráfego de rede (como taxas de pacotes, bytes transmitidos e contadores de portas) costumam apresentar amplitudes muito discrepantes. Para evitar que variáveis de grande magnitude distorcessem os cálculos de distância e gradiente, os dados foram normalizados em uma escala uniforme. Além disso, atributos categóricos tinham suas categorias com tipagem "string", o que comprometia a Análise Exploratória de Dados e processamento para treino dos modelos preditivos. A solução veio com  a aplicação de One-Hot Encoding, dividindo as categorias em novas colunas binárias. 
    • Engenharia de Atributos e Redução de Dimensionalidade (RFE): Utilizamos a eliminação recursiva de atributos (RFE) para descartar dados redundantes e otimizar o custo computacional. A seleção isolou os atributos estatisticamente mais relevantes para diferenciar um tráfego legítimo de um ataque.
    • Ajuste de Dados Desbalanceados: Como os ataques são raros no tráfego real, calibramos os limiares de decisão (thresholds) dos notebooks para lidar com o desbalanceamento. Avaliamos três abordagens: Sensibilidade (focada em capturar o máximo de ameaças, aceitando mais alarmes falsos), Equilíbrio (balanço entre Falsos Positivos e Falsos Negativos) e Precisão (focada em reduzir alarmes falsos, ainda que aumentando os Falsos Negativos).
    • Separação dos Dados: Isolamos rigidamente a preparação em dois fluxos independentes (treino_pre_proc e teste_pre_proc), gerando arquivos .parquet distintos. Isso garantiu que os dados de teste permanecessem inéditos para o modelo, evitando o vazamento de dados (data leakage).

# Descrição dos modelos

Desenvolvemos e analisamos quatro abordagens distintas para resolver o problema de classificação binária (tráfego legítimo vs. ataque):
Algoritmo 1: Regressão Logística (regressao_logistica.ipynb)
    • Conceito: Modelo linear estatístico que mapeia a combinação dos atributos em uma probabilidade entre 0 e 1 usando a função sigmóide.
    • Prós e Contras: É um modelo leve, rápido de treinar e de fácil interpretação. No entanto, apresentou o menor potencial do projeto por não conseguir capturar as relações não-lineares complexas típicas deste dataset.
    • Hiperparâmetros: Testado em sua versão padrão e combinado com o RFE. Também avaliamos variações com os parâmetros 'l1_ratio': [0.2, 0.5, 0.8] e 'C': [0.1, 1.0, 10.0], utilizando Grid Search.
Algoritmo 2: XGBoost Classifier (xgboost.ipynb)
    • Conceito: Baseado em árvores de decisão impulsionadas por gradiente (Gradient Boosted Decision Trees), onde cada nova árvore corrige os erros cometidos pelas anteriores.
    • Prós e Contras: Entrega alta precisão e lida bem com interações não-lineares, além de possuir regularização interna (L1/L2) contra o sobreajuste (overfitting). A desvantagem é o maior custo computacional e a complexidade de ajuste.
    • Hiperparâmetros: Buscando o "Modelo Campeão", comparamos o desempenho com e sem RFE, variando os parâmetros: 'learning_rate': [0.05, 0.1, 0.2], 'max_depth': [3, 4, 5] e 'n_estimators': [50, 100, 150].
Algoritmo 3: Multi-Layer Perceptron - MLP (mlp_2c.ipynb, mlp_3c.ipynb, mlp_5c.ipynb)
    • Conceito: Rede neural artificial feedforward composta por camadas de entrada, ocultas (testamos arquiteturas com 2, 3 e 5 camadas) e de saída, utilizando backpropagation para ajuste de pesos.
    • Prós e Contras: Excelente para mapear padrões ocultos e complexos de ciberataques. Por outro lado, exige grande volume de dados para convergir e funciona como uma "caixa-preta", dificultando a explicação do motivo pelo qual um tráfego foi classificado como malicioso.
Algoritmo 4: Stacking Ensemble (stacking_2c.ipynb)
    • Conceito: Abordagem de meta-aprendizado que combina as previsões de múltiplos modelos de bases diferentes (MLP de duas camadas, XGBoost e Regressão Logística) usando um meta-classificador final.
    • Prós e Contras: Maximiza a robustez ao unir as forças de cada arquitetura (a linearidade da Regressão Logística, a estrutura do XGBoost e a profundidade da MLP). O ponto negativo é o aumento expressivo no tempo de execução e na manutenção do código.

# Avaliação dos modelos criados

## Métricas utilizadas

A escolha das métricas foi guiada pelas necessidades reais de um cenário de segurança digital:
    • Precisão (Precision): Indica a proporção de alarmes que eram de fato ataques. Uma precisão baixa gera excesso de Falsos Positivos, sobrecarregando os analistas de Seguraça da Informação.
    • Sensibilidade (Recall) — Métrica Crítica: Mede a capacidade de detectar os ataques reais. Um Recall baixo resulta em Falsos Negativos (ameaças que passam despercebidas), o que pode causar invasões ou vazamentos críticos.
    • F1-Score: Média harmônica entre Precisão e Sensibilidade, usada como indicador principal para avaliar o equilíbrio geral dos modelos. 

## Discussão dos resultados obtidos

Os testes mostraram que a transição para modelos mais robustos trouxe um ganho substancial. A Regressão Logística não acompanhou a não-linearidade dos dados, padrão que o XGBoost e as redes MLP capturaram com maior eficácia.
Ao testar as variações da MLP, notamos que aumentar a profundidade para 5 camadas não necessariamente traz ganho linear de performance, podendo levar ao overfitting sem uma regularização rígida. O Stacking Ensemble pode ser o modelo mais resiliente: pode reduzir a taxa de Falsos Positivos e Negativos ao equilibrar as previsões da MLP com os gradientes do XGBoost, atendendo com segurança aos requisitos de proteção definidos na análise exploratória.

# Revisão do pipeline de pesquisa e análise de dados

Após a execução dos notebooks, refinamos o pipeline original para torná-lo mais eficiente e modular. As principais alterações foram:
    • Isolamento do Pipeline de Teste: Separamos o pré-processamento em scripts paralelos independentes (treino_pre_proc e teste_pre_proc). Isso garante que os parâmetros de normalização gerados no treino sejam apenas aplicados no teste, sem recalculá-los.
    • Seleção Dinâmica com RFE: Inserimos um bloco modular focado exclusivamente em Feature Selection logo antes do envio dos dados para a suite de algoritmos.
    • Diretório de Persistência: Incluímos uma etapa de salvamento automatizado usando a biblioteca joblib, organizando os arquivos gerados no diretório ../persistencia/modelos_persistentes/.
Justificativa: Essas mudanças tornaram o pipeline genérico para outros contextos de detecção de anomalias. Com essa arquitetura modular, novos logs de segurança ou assinaturas de ataques podem ser processados de ponta a ponta sem a necessidade de reescrever o código principal dos classificadores.
