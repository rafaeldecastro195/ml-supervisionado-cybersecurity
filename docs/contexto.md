# Detecção de Ameaças Cibernéticas com Aprendizado de Máquina

---

# Introdução

A segurança da informação tornou-se um dos maiores desafios da era digital. Com o crescimento exponencial da conectividade e da dependência de sistemas digitais por parte de empresas, governos e cidadãos, os ataques cibernéticos tornaram-se mais frequentes, sofisticados e prejudiciais. Organizações de todos os portes são alvos constantes de ameaças como ataques de força bruta, injeção de SQL, varreduras de portas, negação de serviço (DDoS) e comunicações com servidores de comando e controle (C2).

Este projeto propõe o desenvolvimento de um sistema de detecção de ameaças cibernéticas baseado em aprendizado de máquina, capaz de analisar o tráfego de rede e classificar automaticamente conexões como legítimas ou maliciosas. A iniciativa se insere no contexto da segurança cibernética aplicada, área de atuação crescente tanto no mercado profissional quanto na pesquisa acadêmica.

**Objetivos gerais:** desenvolver um modelos de Aprendizado Supervisionado para classificação automática de ameaças em tráfego de rede, aplicando um pipeline completo de ciência de dados — da preparação dos dados até a avaliação dos modelos.

**Justificativa:** o avanço das ameaças cibernéticas torna inviável a detecção exclusivamente manual. Sistemas baseados em IA conseguem identificar padrões complexos em grandes volumes de dados em tempo real, complementando e potencializando as capacidades das equipes de segurança.

**Público-alvo:** equipes de segurança da informação, administradores de redes, pesquisadores da área e gestores de TI que precisam de ferramentas automatizadas para monitoramento e resposta a incidentes.

---

## Problema

O volume de tráfego de rede gerado por organizações modernas é imenso e cresce a cada ano. Monitorar manualmente cada conexão para identificar possíveis ameaças é humanamente impossível, mesmo para equipes de segurança experientes. Ferramentas tradicionais baseadas em assinaturas (como firewalls e antivírus convencionais) dependem de padrões de ataques já conhecidos, tornando-as ineficazes contra ameaças novas ou variantes de ataques existentes.

O problema central deste projeto é: **como classificar automaticamente o tráfego de rede para identificar se uma conexão representa uma ameaça cibernética — e qual tipo de ataque está ocorrendo — de forma precisa e escalável?**

Ataques como brute-force, port-scan, SQL injection, XSS, DDoS, command injection, credential stuffing e comunicações C2 (Command & Control) possuem características comportamentais distintas que se manifestam em variáveis como volume de bytes transferidos, portas utilizadas, protocolo de comunicação, horário da conexão e origem do tráfego. A combinação dessas variáveis, analisada por modelos de aprendizado de máquina, permite identificar padrões que seriam imperceptíveis a um analista humano em tempo real.

O contexto de aplicação é diretamente ligado a ambientes corporativos de segurança da informação, onde ferramentas como SIEM (Security Information and Event Management) e IDS (Intrusion Detection Systems) são utilizadas para monitoramento contínuo de redes. O modelo desenvolvido neste projeto simula a camada de inteligência que alimentaria esse tipo de sistema.

## Questão de Pesquisa

*É possível, utilizando técnicas de aprendizado de máquina aplicadas a dados de tráfego de rede, classificar automaticamente conexões como legítimas ou maliciosas com alta taxa de detecção e baixa taxa de falsos alarmes, identificando ainda o tipo específico de ameaça presente?*

Ao final do projeto, espera-se que o modelo treinado seja capaz de responder a essa pergunta.
## Objetivos preliminares

Objetivo geral: experimentar e comparar técnicas de desenvolvimento de modelos de aprendizado supervisionado de máquina para classificação e detecção automática de ameaças cibernéticas em tráfego de rede, identificando qual abordagem oferece o melhor equilíbrio entre taxas de detecção e taxas de falsos positivos.

Objetivo específico 1: aplicar um pipeline completo de ciência de dados sobre o conjunto de dados de tráfego de rede — incluindo limpeza, pré-processamento, engenharia de recursos, balanceamento e divisão estratificada entre treino e teste — garantindo a qualidade dos dados para o treinamento dos modelos.

Objetivo específico 2: treinar o modelo de classificação (Árvore de Decisão e XGBoost), avaliando seu desempenho por meio de detalhes específicos para dados desequilibrados (F1-Score, ROC-AUC, Precision e Recall da classe de ataque), de modo que o modelo possa apresentar melhor capacidade de generalização para detecção de ameaças.

## Justificativa

A escolha do tema de detecção de ameaças cibernéticas é motivada tanto pela relevância prática e atual do problema quanto pela disponibilidade de dados estruturados adequados para aplicação de técnicas de aprendizado de máquina.

Do ponto de vista do impacto econômico e social, os números são expressivos. Segundo o relatório IBM Cost of a Data Breach 2025 , o custo médio global de uma violação de dados atingiu US$ 4,4 milhões em 2025 . No Brasil , o custo médio por violação foi de R$ 7,19 milhões . O mesmo relatório aponta que ataques de credenciais comprometidos — categoria diretamente relacionada a ataques de força bruta e preenchimento de credenciais presentes no conjunto de dados deste projeto — são o vetor de entrada mais comum.

Além disso, segundo o relatório Cybersecurity Ventures , os danos globais causados ​​por crimes cibernéticos deverão atingir US$ 10,5 trilhões anuais até 2025 , o que representa a maior transferência de riqueza da história da humanidade. No Brasil, a Check Point Research registrou um aumento de 30% nos ataques cibernéticos no segundo trimestre de 2024 em comparação ao mesmo período do ano anterior, colocando o país entre os mais atacados da América Latina.

Por fim, a relevância do tema é evidenciada pela grande quantidade de publicações e conteúdos que abordam detecção de intrusão com aprendizado de máquina, confirmando que esta é uma área ativa e com lacunas de pesquisa a serem exploradas.

## Público-Alvo

O projeto é relevante para diferentes perfis de usuários e partes interessadas:

Analistas de Segurança da Informação (Analistas SOC): profissionais com conhecimento técnico avançado em redes e segurança, familiarizados com ferramentas SIEM e IDS. São os usuários finais diretos de um sistema conforme o proposto. Possuem alto nível de familiaridade com recursos digitais e reuniões de ferramentas que reduzem o volume de alertas falsos e priorizam ameaças reais.

Administradores de Redes e Infraestrutura: responsáveis ​​pela gestão do tráfego de rede em empresas. Possuem conhecimento técnico intermediário a avançado e precisam de dashboards e relatórios que traduzam os resultados do modelo em ações práticas de resposta a incidentes.

Gestores de TI e CISO (Chief Information Security Officer): tomadores de decisão com visão estratégica sobre riscos de segurança. Possuo menor familiaridade técnica com os modelos em si, mas analisamos considerações claras de desempenho para avaliar o retorno sobre o investimento em ferramentas de segurança.

Pesquisadores e Estudantes da área de Segurança e Ciência de Dados: específicos em metodologias de detecção de intrusão, benchmarks de modelos e reprodutibilidade de experimentos. Beneficiam-se da documentação completa do pipeline e das escolhas metodológicas do projeto.

## Estado da Arte

### Trabalho 1

**Título:** *Machine Learning for Cybersecurity: Web Attack Detection (Brute Force, XSS, SQL Injection)*  
**Publicação:** InPrime: Indonesian Journal of Pure and Applied Mathematics, v. 7, n. 1, 2025  
**URL:** https://journal.uinjkt.ac.id/index.php/inprime/article/view/41025

**Problema e contexto:** detecção de ataques web — especificamente Brute Force, XSS e SQL Injection — em tráfego de rede, contexto diretamente alinhado ao dataset deste projeto.

**Dataset:** os autores utilizaram os datasets CICIDS2017 e CSE-CICIDS2018, contendo tráfego de rede rotulado em quatro categorias: Benign, Brute Force, XSS e SQL Injection. Para tratar o desbalanceamento, aplicaram SMOTE em conjunto com Análise de Componentes Principais (PCA).

**Abordagens de ML:** os modelos avaliados incluíram Random Forest, KNN e algoritmos de boosting como XGBoost e LightGBM, com validação por K-Fold Cross Validation. A avaliação de modelos foi feita usando técnicas como K-Fold Cross Validation, onde tanto Random Forest quanto KNN demonstraram estabilidade, com pequenas flutuações de acurácia entre os diferentes subconjuntos de dados.

**Métricas:** Accuracy, Precision, Recall, F1-Score e ROC-AUC.

**Principais resultados:** Random Forest e KNN apresentaram resultados estáveis. XGBoost e LightGBM apresentaram bom desempenho geral, com leve variação indicando necessidade de ajuste fino de hiperparâmetros. O estudo identificou que o tratamento do desbalanceamento com SMOTE foi essencial para resultados confiáveis.

---

### Trabalho 2

**Título:** *Network Intrusion Detection System Using XGBoost and Random Forest Algorithms*  
**Autores:** Onyebueke, A. E.; David, A. A.; Munu, S.  
**Publicação:** Asian Journal of Pure and Applied Mathematics, v. 5, n. 1, p. 321–335, 2023  
**URL:** https://jofmath.com/index.php/AJPAM/article/view/18

**Problema e contexto:** desenvolvimento de um sistema de detecção de intrusão em redes utilizando XGBoost e Random Forest, com foco em identificar anomalias e acessos não autorizados.

**Dataset:** o estudo utilizou os datasets UNSW-NB15 2017 e KDD, disponíveis no Kaggle, com aplicação de normalização, seleção de features e SMOTE para balanceamento.

**Abordagens de ML:** XGBoost e Random Forest, com pré-processamento de normalização, seleção de features e SMOTE.

**Métricas:** Accuracy, Precision, Recall e F1-Score.

**Principais resultados:** o XGBoost obteve 100% de acurácia, precisão e recall no dataset UNSW-NB15, com F1-Score perfeito. No dataset KDD, ambos os algoritmos atingiram acurácia próxima de perfeição — 99% para XGBoost e 98% para Random Forest — após as etapas de pré-processamento e balanceamento com SMOTE.

---

### Trabalho 3

**Título:** *The Improved Network Intrusion Detection Techniques Using the Feature Engineering Approach with Boosting Classifiers*  
**Publicação:** Mathematics (MDPI), v. 12, n. 24, 2024  
**URL:** https://www.mdpi.com/2227-7390/12/24/3909

**Problema e contexto:** melhoria na detecção de intrusões em redes por meio de engenharia de features avançada combinada com classificadores de boosting.

**Dataset:** dataset de detecção de intrusão em redes com registros de tráfego normal e anômalo, com 70% para treino e 30% para teste.

**Abordagens de ML:** o estudo incorporou classificadores convencionais (Naive Bayes, Regressão Logística e SVC) e classificadores de boosting (CatBoost, LightGBM, HistGradientBoosting e XGBoost), com validação por 10-Fold Cross Validation e avaliação por múltiplas métricas incluindo Accuracy, F1-Score, AUC-ROC e Precision.

**Métricas:** Accuracy, F1-Score, AUC-ROC, Precision e Recall.

**Principais resultados:** o modelo XGBoost produziu o melhor desempenho geral, com valores médios de 99,54% de acurácia, 99,53% de precisão, 99,54% de recall e F1-Score de 99,53%. Todos os classificadores de boosting obtiveram valor AUC perfeito igual a 1.

---

### Trabalho 4

**Título:** *Deep Learning-Based Intrusion Detection for IoT Networks: A Scalable and Efficient Approach*  
**Publicação:** Journal on Information Security (Springer Nature), 2025  
**URL:** https://link.springer.com/article/10.1186/s13635-025-00202-w

**Problema e contexto:** detecção de intrusão em redes IoT utilizando modelos de deep learning, contexto que compartilha os mesmos tipos de ataque do dataset deste projeto.

**Dataset:** o estudo utilizou o dataset CIC IoT-DIAD 2024, contendo tráfego de rede de 105 dispositivos IoT sob condições benignas e de ataque, cobrindo 33 tipos diferentes de ataques categorizados em sete classes principais: DDoS, DoS, Brute Force, Spoofing, ataques web, SQL Injection e ataques Mirai. O dataset possui 84 features distintas capturando características de fluxo de rede.

**Abordagens de ML:** modelos de deep learning como CNNs 1D, redes LSTM, RNNs e MLPs para detecção de ameaças em tempo real.

**Métricas:** Accuracy, Precision, Recall, F1-Score e AUC-ROC.

**Principais resultados:** os modelos de deep learning superaram abordagens tradicionais de ML para dados sequenciais de tráfego IoT. LSTM e CNN 1D apresentaram os melhores resultados para captura de padrões temporais em fluxos de rede. O estudo evidenciou que a arquitetura do modelo deve ser escolhida considerando a natureza sequencial dos dados de rede.

---

### Trabalho 5

**Título:** *Top-K Feature Selection for IoT Intrusion Detection: Contributions of XGBoost, LightGBM, and Random Forest*  
**Publicação:** Future Internet (MDPI), v. 17, n. 11, 2025  
**URL:** https://www.mdpi.com/1999-5903/17/11/529

**Problema e contexto:** otimização da detecção de intrusão em redes IoT por meio de seleção de features Top-K combinada com modelos ensemble, abordando o desafio de espaços de features grandes e complexos.

**Dataset:** CICIoMT2024, avaliado com três configurações de features: Top-10, Top-15 e conjunto completo.

**Abordagens de ML:** três algoritmos foram treinados e testados: XGBoost, LightGBM e Random Forest, cada um avaliado nas três configurações de features. Além das métricas padrão, foram reportadas a Taxa de Falso Alarme (FAR), Taxa de Falso Positivo (FPR) e Taxa de Detecção (DR).

**Métricas:** Accuracy, Precision, Recall, F1-Score, FAR, FPR e Detection Rate.

**Principais resultados:** o modelo Random Forest apresentou o melhor equilíbrio entre acurácia e eficiência computacional, atingindo 91,7% de acurácia e F1-Score de 93% com o subconjunto Top-10, reduzindo o tempo de processamento em 35%. O estudo demonstrou que a seleção de features não apenas melhora o desempenho, mas também aumenta a interpretabilidade do modelo — relevante para ambientes de segurança onde a explicabilidade das decisões é importante.

---

### Síntese Crítica dos Trabalhos Relacionados

Os cinco estudos analisados apresentam forte convergência em torno de algumas conclusões fundamentais. Em primeiro lugar, todos concordam que **algoritmos de ensemble — especialmente Random Forest e XGBoost — consistentemente superam modelos mais simples** como Regressão Logística e Naive Bayes em tarefas de detecção de intrusão. Em segundo lugar, o **desbalanceamento de classes é unanimemente identificado como o principal desafio técnico** da área, e o SMOTE é a técnica de reamostragem mais amplamente adotada e validada para seu tratamento. Em terceiro lugar, a **engenharia de features** é reconhecida como etapa determinante: a seleção das variáveis mais relevantes melhora tanto o desempenho quanto a eficiência computacional dos modelos.

As principais divergências entre os estudos referem-se à escolha das métricas de avaliação e ao conjunto de dados utilizado. Alguns trabalhos reportam acurácia como métrica principal — o que pode ser enganoso em dados desbalanceados — enquanto outros priorizam F1-Score, Recall e Detection Rate, mais adequados para o contexto de detecção de ataques. Essa inconsistência metodológica dificulta comparações diretas entre estudos.

As lacunas identificadas na literatura incluem: (1) a maioria dos estudos utiliza datasets históricos e bem conhecidos como CICIDS2017 e NSL-KDD, com pouca exploração de datasets mais recentes e diversificados; (2) poucos trabalhos abordam explicitamente o impacto dos falsos positivos para equipes de segurança operacionais; (3) a interpretabilidade dos modelos — saber **por que** uma conexão foi classificada como ataque — ainda é pouco explorada na literatura.

Este projeto se alinha com os estudos identificados ao adotar os mesmos algoritmos consagrados (Regressão Logística como baseline, Random Forest e XGBoost como modelos principais), aplicar SMOTE para tratamento do desbalanceamento e avaliar os modelos com métricas adequadas ao contexto (F1-Score, Recall e ROC-AUC). Diferencia-se ao utilizar um dataset com maior diversidade de tipos de ataque e ao explorar a engenharia de features sobre variáveis temporais e de protocolo, aspectos menos explorados nos trabalhos levantados.

# Descrição do Dataset Selecionado

## Identificação e Origem

| Atributo | Informação |
|---|---|
| **Nome** | Cybersecurity Threat Detection Dataset |
| **Fonte** | Kaggle — usuário dhrubangtalukdar |
| **URL** | https://www.kaggle.com/datasets/dhrubangtalukdar/cybersecurity-threat-detection-dataset |
| **Licença** | Verificar na página do Kaggle |
| **Formato** | CSV único (cybersecurity.csv) |
| **Tamanho** | ~2 MB |

## Visão Geral

O dataset contém registros de conexões de rede rotulados entre tráfego benigno e diferentes tipos de ataques cibernéticos. Cada registro representa uma única conexão de rede com informações sobre origem, destino, protocolo, volume de dados transferidos e classificação de segurança.

| Métrica | Valor |
|---|---|
| **Total de registros** | 10.000 |
| **Total de atributos** | 13 colunas |
| **Tráfego benigno (label = 0)** | 9.600 registros (96%) |
| **Tráfego malicioso (label = 1)** | 400 registros (4%) |
| **Valores nulos** | 3.232 (apenas na coluna `url`) |
| **Duplicatas** | Nenhuma |
| **Período** | Outubro de 2025 (dado sintético/simulado) |

## Distribuição dos Tipos de Ataque

| Tipo de Ataque | Registros | Descrição |
|---|---|---|
| benign | 9.600 | Tráfego legítimo normal |
| brute-force | 108 | Tentativas repetidas de autenticação |
| port-scan | 81 | Varredura de portas abertas |
| sql-injection | 64 | Injeção de comandos SQL maliciosos |
| xss | 34 | Cross-Site Scripting |
| credential-stuffing | 28 | Uso de credenciais vazadas |
| ddos | 27 | Negação de serviço distribuída |
| command-injection | 26 | Injeção de comandos no sistema |
| exploit-attempt | 22 | Tentativa de exploração de vulnerabilidades |
| c2 | 10 | Comunicação com servidor Command & Control |

## Descrição dos Atributos

| Coluna | Tipo | Descrição | Valores Ausentes | Exemplos |
|---|---|---|---|---|
| `timestamp` | String (datetime) | Data e hora da conexão. Permite extração de features temporais como hora do dia e dia da semana. | Nenhum | 2025-10-01 00:12:54 |
| `src_ip` | String | Endereço IP de origem da conexão. Identificador de rede, não utilizado diretamente como feature preditiva. | Nenhum | 188.176.27.165 |
| `dst_ip` | String | Endereço IP de destino da conexão. | Nenhum | 10.0.0.5 |
| `src_port` | Inteiro | Porta de origem da conexão. Varia de 21 a 65.524. | Nenhum | 45231 |
| `dst_port` | Inteiro | Porta de destino da conexão. Portas como 80 (HTTP), 443 (HTTPS) e 22 (SSH) são comuns. | Nenhum | 443 |
| `protocol` | String | Protocolo de comunicação utilizado: TCP, UDP ou ICMP. | Nenhum | TCP (77,65%), UDP (19,1%), ICMP (3,25%) |
| `bytes_sent` | Inteiro | Volume de bytes enviados na conexão. Varia de 17 a 139.170.400. | Nenhum | 22.000 |
| `bytes_received` | Inteiro | Volume de bytes recebidos na conexão. Varia de 3 a 291.483.000. | Nenhum | 37.473 |
| `user_agent` | String | Agente de usuário HTTP da conexão. Indica o navegador ou ferramenta utilizada. | Nenhum | Mozilla/5.0 (Windows NT 10.0...) |
| `url` | String | URL acessada na conexão. Ausente para conexões UDP e ICMP que não geram requisições HTTP. | **3.232 (32,32%)** | https://webmail.corp/login |
| `is_internal_traffic` | Booleano | Indica se a conexão é interna à rede (True) ou externa (False). | Nenhum | False (84,66%), True (15,34%) |
| `label` | Inteiro (0 ou 1) | **Variável-alvo binária.** 0 = tráfego legítimo, 1 = ataque cibernético. | Nenhum | 0, 1 |
| `attack_type` | String | **Variável-alvo multiclasse.** Especifica o tipo de ataque ou "benign". Usada para análise, não como feature preditiva. | Nenhum | benign, brute-force, ddos... |

## Qualidade dos Dados

**Pontos positivos:**
- Nenhuma duplicata identificada.
- Apenas uma coluna com valores ausentes (`url`), com justificativa técnica clara, já que algumas conexões não geram URL.
- Variáveis-alvo, label e attack_type, bem definida em duas granularidades (binária e multiclasse).
- Distribuição de protocolos realista (TCP dominante, seguido de UDP e ICMP).

**Desafios identificados e tratamentos planejados:**

| Problema | Descrição | Tratamento Planejado |
|---|---|---|
| **Valores nulos em `url`** | 3.232 registros sem URL (conexões UDP/ICMP) | Substituir por `'sem_url'` — ausência de URL é informação relevante |
| **Colunas textuais não numéricas** | `src_ip`, `dst_ip`, `user_agent`, `url` | Tranformar os valores correspondentes em features numéricas |
| **`timestamp` não numérico** | Data/hora em formato string | Extração de `hora` e `dia_semana` como features numéricas |
| **`is_internal_traffic` booleano** | True/False | Conversão para 1/0 |
| **`attack_type` como feature** | Seria vazamento de informação (data leakage) | Utilizada apenas para análise exploratória, removida do modelo |

## Critérios de Qualidade Atendidos

| Critério (orientações do projeto) | Avaliação |
|---|---|
| **Representatividade** | Cobre 9 tipos de ataque relevantes e modernos |
| **Qualidade dos dados** | Sem duplicatas; único problema de nulos tem solução clara |
| **Contexto e significado** | Todas as colunas têm significado técnico claro em segurança de redes |
| **Ética e privacidade** | IPs e dados de usuário são sintéticos/simulados; sem dados pessoais reais |
| **Atualidade e relevância** | Tipos de ataque modernos (C2, credential-stuffing, XSS) |
| **Tamanho do dataset** | 10.000 registros — atende ao mínimo exigido |

---
# Canvas analítico

![CanvaAnalitico](/docs/img/canvaanlitico.png)

# Vídeo de apresentação da Etapa 01

A apresentação poderá ser vista pelo seguinte link: [Link no youtube](https://youtu.be/Zv_VfYV-ZCk)


# Referências

ONYEBUEKE, A. E.; DAVID, A. A.; MUNU, S. **Network Intrusion Detection System Using XGBoost and Random Forest Algorithms.** Asian Journal of Pure and Applied Mathematics, v. 5, n. 1, p. 321–335, 2023. Disponível em: https://jofmath.com/index.php/AJPAM/article/view/18

ANONYMOUS. **Machine Learning for Cybersecurity: Web Attack Detection (Brute Force, XSS, SQL Injection).** InPrime: Indonesian Journal of Pure and Applied Mathematics, v. 7, n. 1, p. 1–15, 2025. Disponível em: https://journal.uinjkt.ac.id/index.php/inprime/article/view/41025

MDPI. **The Improved Network Intrusion Detection Techniques Using the Feature Engineering Approach with Boosting Classifiers.** Mathematics, v. 12, n. 24, art. 3909, 2024. Disponível em: https://www.mdpi.com/2227-7390/12/24/3909

SPRINGER NATURE. **Deep Learning-Based Intrusion Detection for IoT Networks: A Scalable and Efficient Approach.** Journal on Information Security, 2025. Disponível em: https://link.springer.com/article/10.1186/s13635-025-00202-w

MDPI. **Top-K Feature Selection for IoT Intrusion Detection: Contributions of XGBoost, LightGBM, and Random Forest.** Future Internet, v. 17, n. 11, art. 529, 2025. Disponível em: https://www.mdpi.com/1999-5903/17/11/529

SHARAFALDIN, I.; LASHKARI, A. H.; GHORBANI, A. A. **Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization.** In: INTERNATIONAL CONFERENCE ON INFORMATION SYSTEMS SECURITY AND PRIVACY (ICISSP), 4., 2018. Anais [...]. [S. l.]: SCITEPRESS, 2018. p. 108–116. DOI: 10.5220/0006639801080116.

IBM SECURITY. **Cost of a Data Breach Report 2023.** Armonk: IBM Corporation, 2023. Disponível em: https://www.ibm.com/reports/data-breach

CYBERSECURITY VENTURES. **Cybercrime to cost the world $10.5 trillion annually by 2025.** 2022. Disponível em: https://cybersecurityventures.com/hackerpocalypse-cybercrime-report-2016/
