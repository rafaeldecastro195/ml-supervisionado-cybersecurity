# Preparação dos dados

Nesta etapa, aplicamos diversas técnicas de pré-processamento e tratamento para garantir a qualidade dos dados inseridos no modelo:

* **Limpeza e Adequação de Dados:** Os valores ausentes foram checados e tratados, além da remoção de dados duplicados (`df.drop_duplicates()`). Foi realizada a adequação dos nomes das colunas e a correta tipagem dos dados numéricos e categóricos.
* **Remoção de Outliers:** Utilizando uma abordagem interquartil, identificamos os percentis 25% e 75% para estipular os limites inferiores e superiores de cada feature contínua. Registros fora destes limites foram removidos usando a função customizada `drop_outlier`.
* **Transformação e Codificação de Dados:**
  * **Ordinal Encoder:** As variáveis categóricas foram transformadas em formato numérico via `OrdinalEncoder` para que pudessem ser operadas pelos modelos de classificação, com a vantagem de não aumentar a dimensionalidade do dataset.
  * **Normalização (Robust Scaler):** Dado que os atributos apresentavam variações bruscas de valores e distribuição não-normal, optou-se por utilizar o `RobustScaler`. Ele é eficiente e lida bem com os eventuais *outliers* remanescentes.
* **Feature Engineering:** Aplicou-se a classe `PolynomialFeatures` para capturar as interações não-lineares entre variáveis.
* **Tratamento de Dados Desbalanceados:** Foi empregada a técnica de _oversampling_ com a biblioteca `SMOTE` (`Synthetic Minority Over-sampling Technique`) sobre os dados de treinamento, visando equilibrar as classes do alvo (especialmente ao lidar com o atributo `categoria_ataque`).
* **Separação dos Dados:** Os dados foram separados adequadamente em conjuntos de treino e teste, evitando vazamento de dados (*data leakage*), especialmente garantindo que transformações como o `SMOTE` afetem exclusivamente o dataset de treinamento.

# Descrição do modelo

O modelo selecionado para este problema foi a **Regressão Logística** (Logistic Regression). Apesar de ser um modelo inicialmente linear, ele se adapta bem à predição de probabilidades e, em conjunto com as `PolynomialFeatures`, é capaz de traçar fronteiras de decisão complexas para o nosso objetivo primário de detecção de anomalias e ataques cibernéticos. 

O algoritmo foi ajustado utilizando a implementação do `Scikit-Learn` sob os seguintes hiperparâmetros configurados durante a experimentação:
* `max_iter=3000`: Para garantir a convergência do algoritmo dada a grande dimensão dos dados.
* `solver='saga'`: Um otimizador eficiente para grandes datasets, suportando regularizações flexíveis.
* `penalty='elasticnet'`: Combinação das penalidades L1 e L2 para evitar o overfitting e lidar com multicolinearidade.
* `l1_ratio=0.5`: Define o balanço exato (50/50) entre as penalidades L1 e L2 na regularização Elastic-Net.
* `C=5.0`: O parâmetro inverso da força de regularização, concedendo mais peso aos dados de treinamento.

# Avaliação dos modelos criados

## Métricas utilizadas

Para mensurar o desempenho do modelo de classificação, além da pontuação base, utilizamos um conjunto amplo de métricas derivadas da **Matriz de Confusão** e do **Relatório de Classificação**:
* **Acurácia (Accuracy):** Mede o total de predições corretas em relação ao todo.
* **Precisão (Precision):** Focada na confiabilidade dos eventos apontados como "Ataque", mitigando **falsos positivos** (alarmes falsos).
* **Revocação (Recall):** Fundamental em segurança cibernética, indica o quão bom o modelo é em capturar todos os eventos críticos, ou seja, em evitar **falsos negativos** (deixar passar um ataque real).
* **F1-Score:** A média harmônica entre a precisão e a revocação, oferecendo um único valor que resume a utilidade geral do classificador em lidar com o desbalanço entre alarmes falsos e ameaças ignoradas.

## Discussão dos resultados obtidos

Ao aplicarmos as predições no conjunto de teste (aproximadamente 49.971 instâncias), o modelo retornou os seguintes resultados práticos:

* **Matriz de Confusão:**
  * **Verdadeiros Negativos (TN):** 34.70% (17.339 instâncias normais detectadas corretamente).
  * **Verdadeiros Positivos (TP):** 32.41% (16.195 ataques cibernéticos diagnosticados adequadamente).
  * **Falsos Negativos (FN):** 4.33% (2.166 casos de ameaça ignorados incorretamente).
  * **Falsos Positivos (FP):** 28.56% (14.271 alarmes falsos registrados).

* **Desempenho por Classe (Relatório):**
  * O modelo apresentou uma **Acurácia Geral** de 67.11%, com o modelo acertando a classificação de 2 a cada 3 conexões da rede.
  * O **Recall** para a classe de interesse (ataque, classe 1.0) foi bastante elevado, na casa dos **0.88 (88%)**. No escopo de segurança da informação, isso é excelente, visto que a pior falha de segurança seria um baixo Recall (resultando em alto índice de vulnerabilidades ativas na rede que passariam despercebidas). O modelo focou em ser cauteloso com falsos negativos.
  * Em contraponto, o alto índice de falsos positivos fez a **Precisão** para a classe de ataque diminuir para **0.53 (53%)**, sinalizando que muitos alertas falsos podem acabar sobrecarregando o analista de redes da empresa. 
  * O **F1-Score** em ambas as classes de ataque (0.66) e tráfego legítimo (0.68) se mostrou balanceado, evidenciando uma coerência estatística por parte do modelo.

Estes achados respondem ao objetivo da pesquisa ao provar a aplicabilidade técnica de algoritmos supervisionados em fluxos de rede, mas apontam a necessidade de eventual calibração para se ter um limiar de probabilidade que reduza os alarmes falsos sem prejudicar a detecção massiva das ameaças.

# Pipeline de pesquisa e análise de dados

Nosso pipeline de experimentação foi estruturado e metodológico. Ele se baseou nas seguintes etapas:
1. **Coleta e Organização:** Extração de dados brutos e padronização do repositório em seções coerentes de projeto de Ciência de Dados.
2. **Pré-Processamento:** Aplicação modular de tratamento de dados (`preproc.py` e `metricas.py`), incluindo imputação de valores, conversão do formato dos atributos, normalização com escalonadores robustos aos outliers (*Robust Scaler*), e expansão polinomial.
3. **Engenharia de Amostragem:** Correção proativa de dados não-balanceados na classe de ataques via geração sintética (`SMOTE`).
4. **Treino e Inferência do Modelo:** Uso da Regressão Logística em ambiente computacional com separação de dados de treino e teste.
5. **Avaliação Crítica e Interpretação:** Cálculo numérico da matriz de confusão para dar contexto real para negócios (quantos alarmes falsos ocorrerão versus falhas críticas permitidas).
