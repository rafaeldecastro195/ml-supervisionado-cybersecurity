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

Ataques como Exploits, DoS, Reconnaissance, Backdoor, Shellcode, Fuzzers e Worms possuem características comportamentais distintas que se manifestam em variáveis como duração da conexão, volume de bytes transferidos, jitter, taxa de perda de pacotes e estado da conexão TCP. A combinação dessas variáveis, analisada por modelos de aprendizado de máquina, permite identificar padrões que seriam imperceptíveis a um analista humano em tempo real.

O contexto de aplicação é diretamente ligado a ambientes corporativos de segurança da informação, onde ferramentas como SIEM (Security Information and Event Management) e IDS (Intrusion Detection Systems) são utilizadas para monitoramento contínuo de redes. O modelo desenvolvido neste projeto simula a camada de inteligência que alimentaria esse tipo de sistema.

---

## Questão de Pesquisa

*É possível, utilizando técnicas de aprendizado de máquina aplicadas a dados de tráfego de rede, classificar automaticamente conexões como legítimas ou maliciosas com alta taxa de detecção e baixa taxa de falsos alarmes, identificando ainda o tipo específico de ameaça presente?*

Ao final do projeto, espera-se que o modelo treinado seja capaz de responder a essa pergunta.

---

## Objetivos Preliminares

**Objetivo geral:** experimentar e comparar técnicas de desenvolvimento de modelos de aprendizado supervisionado de máquina para  classificação e detecção automática de ameaças cibernéticas em tráfego de rede, identificando qual abordagem oferece o melhor equilíbrio entre taxa de detecção e taxa de falsos positivos.

**Objetivo específico 1:** aplicar um pipeline completo de ciência de dados sobre o dataset de tráfego de rede — incluindo limpeza, pré-processamento, engenharia de features, balanceamento  e divisão estratificada entre treino e teste — garantindo a qualidade dos dados para o treinamento dos modelos.

**Objetivo específico 2:** treinar o modelo de classificação (Árvore de Decisão e XGBoost), avaliando seu desempenho por meio de métricas adequadas para dados desbalanceados (F1-Score, ROC-AUC, Precision e Recall da classe de ataque), de modo que o modelo possa apresentar melhor capacidade de generalização para detecção de ameaças.

---

## Justificativa

A escolha do tema de detecção de ameaças cibernéticas é motivada tanto pela relevância prática e atual do problema quanto pela disponibilidade de dados estruturados adequados para aplicação de técnicas de aprendizado de máquina.

Do ponto de vista do impacto econômico e social, os números são expressivos. Segundo o relatório [IBM Cost of a Data Breach 2025](https://www.ibm.com/reports/data-breach), o custo médio global de uma violação de dados atingiu **US$ 4,4 milhões em 2025**. [No Brasil](https://brasil.newsroom.ibm.com/2025-07-30-Relatorio-da-IBM-Custo-medio-de-uma-violacao-de-dados-no-Brasil-atinge-R-7,19-milhoes), o custo médio por violação foi de **R$ 7,19 milhões**. O mesmo relatório aponta que ataques de credenciais comprometidas — categoria diretamente relacionada a ataques de brute-force e credential-stuffing presentes no dataset deste projeto — são o vetor de entrada mais comum.

Adicionalmente, segundo o relatório [Cybersecurity Ventures](https://cybersecurityventures.com/cybercrime-damage-costs-10-trillion-by-2025/), os danos globais causados por crimes cibernéticos devem atingir **US$ 10,5 trilhões anuais até 2025**, o que representa a maior transferência de riqueza da história da humanidade. No Brasil, a [Check Point Research](https://blog.checkpoint.com/research/check-point-research-reports-highest-increase-of-global-cyber-attacks-seen-in-last-two-years-a-30-increase-in-q2-2024-global-cyber-attacks/) registrou um **aumento de 30% nos ataques cibernéticos no segundo trimestre de 2024** em comparação ao mesmo período do ano anterior, colocando o país entre os mais atacados da América Latina.

Por fim, a relevância do tema é evidenciada pela grande quantidade de publicações e conteúdos que abordam detecção de intrusão com machine learning, confirmando que esta é uma área ativa e com lacunas de pesquisa a serem exploradas.

---

## Público-Alvo

O projeto é relevante para diferentes perfis de usuários e partes interessadas:

**Analistas de Segurança da Informação (SOC Analysts):** profissionais com conhecimento técnico avançado em redes e segurança, familiarizados com ferramentas SIEM e IDS. São os usuários finais diretos de um sistema como o proposto. Possuem alto nível de familiaridade com recursos digitais e necessitam de ferramentas que reduzam o volume de alertas falsos e priorizem ameaças reais.

**Administradores de Redes e Infraestrutura:** responsáveis pela gestão do tráfego de rede em empresas. Possuem conhecimento técnico intermediário a avançado e precisam de dashboards e relatórios que traduzam os resultados do modelo em ações práticas de resposta a incidentes.

**Gestores de TI e CISO (Chief Information Security Officer):** tomadores de decisão com visão estratégica sobre riscos de segurança. Possuem menor familiaridade técnica com os modelos em si, mas necessitam de métricas claras de desempenho para avaliar o retorno sobre o investimento em ferramentas de segurança.

**Pesquisadores e Estudantes da área de Segurança e Ciência de Dados:** interessados em metodologias de detecção de intrusão, benchmarks de modelos e reprodutibilidade de experimentos. Beneficiam-se da documentação completa do pipeline e das escolhas metodológicas do projeto.

---

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

---

# Descrição do Dataset Selecionado

## Identificação e Origem

| Atributo | Informação |
|---|---|
| **Nome** | UNSW-NB15 |
| **Instituição** | University of New South Wales (UNSW), Austrália |
| **Publicação** | IEEE Military Communications Conference (MILCOM), 2015 |
| **Fonte Kaggle** | https://www.kaggle.com/datasets/dhoogla/unswnb15 |
| **Licença** | Uso acadêmico e de pesquisa |
| **Formato** | Parquet (treino e teste separados) |
| **Tamanho** | ~4,54 MB |

## Visão Geral
 
O UNSW-NB15 foi criado pelo Cyber Range Lab da UNSW usando a ferramenta IXIA PerfectStorm para gerar tráfego de ataque realista combinado com tráfego normal capturado em ambiente de laboratório controlado. É amplamente utilizado como benchmark em pesquisas de detecção de intrusão.
 
| Métrica | Valor |
|---|---|
| **Total de registros (bruto)** | 257.673 |
| **Treino (bruto)** | 175.341 |
| **Teste (bruto)** | 82.332 |
| **Total após limpeza** | 146.793 |
| **Treino após limpeza** | 96.822 |
| **Teste após limpeza** | 49.971 |
| **Atributos** | 36 colunas |
| **Valores nulos** | Nenhum  |
| **Duplicatas identificadas** | 110.880 (a remover) |
 

## Distribuição das Classes
 
| Conjunto | Normal | Ataque | Observação |
|---|---|---|---|
| **Treino (após limpeza)** | 48.894 (50,5%) | 47.928 (49,5%) | Praticamente balanceado |
| **Teste (após limpeza)** | 31.610 (63,3%) | 18.361 (36,7%) | Distribuição diferente do treino |
 
## Categorias de Ataque
 
| Categoria | Registros (treino) | Descrição |
|---|---|---|
| Normal | 56.000 | Tráfego legítimo |
| Generic | 40.000 | Ataques genéricos a cifras de bloco |
| Exploits | 33.393 | Exploração de vulnerabilidades conhecidas |
| Fuzzers | 18.184 | Envio de dados aleatórios para encontrar falhas |
| DoS | 12.264 | Negação de serviço |
| Reconnaissance | 10.491 | Varredura e coleta de informações |
| Analysis | 2.000 | Análise de portas e e-mails maliciosos |
| Backdoor | 1.746 | Acesso não autorizado persistente |
| Shellcode | 1.133 | Execução de código malicioso |
| Worms | 130 | Propagação automática de malware |
 
## Descrição dos Atributos
 
| Coluna | Tipo | Descrição |
|---|---|---|
| `dur` | Float | Duração da conexão em segundos |
| `proto` | Categórico | Protocolo de rede (tcp, udp, arp, ospf...) |
| `service` | Categórico | Serviço da conexão (http, dns, ftp, smtp, ssh...) |
| `state` | Categórico | Estado da conexão (FIN, INT, CON, REQ, RST...) |
| `spkts` | Inteiro | Número de pacotes enviados pela origem |
| `dpkts` | Inteiro | Número de pacotes enviados pelo destino |
| `sbytes` | Inteiro | Total de bytes enviados pela origem |
| `dbytes` | Inteiro | Total de bytes enviados pelo destino |
| `rate` | Float | Taxa de pacotes por segundo da conexão |
| `sload` | Float | Carga de bits por segundo da origem |
| `dload` | Float | Carga de bits por segundo do destino |
| `sloss` | Inteiro | Pacotes retransmitidos ou perdidos pela origem |
| `dloss` | Inteiro | Pacotes retransmitidos ou perdidos pelo destino |
| `sinpkt` | Float | Tempo médio entre pacotes da origem (ms) |
| `dinpkt` | Float | Tempo médio entre pacotes do destino (ms) |
| `sjit` | Float | Jitter (variação de latência) da origem |
| `djit` | Float | Jitter (variação de latência) do destino |
| `swin` | Inteiro | Tamanho da janela TCP da origem |
| `stcpb` | Inteiro | Número de sequência TCP da origem |
| `dtcpb` | Inteiro | Número de sequência TCP do destino |
| `dwin` | Inteiro | Tamanho da janela TCP do destino |
| `tcprtt` | Float | Round-trip time (RTT) do handshake TCP |
| `synack` | Float | Tempo entre pacotes SYN e SYN-ACK |
| `ackdat` | Float | Tempo entre pacotes SYN-ACK e ACK |
| `smean` | Inteiro | Tamanho médio dos pacotes da origem (bytes) |
| `dmean` | Inteiro | Tamanho médio dos pacotes do destino (bytes) |
| `trans_depth` | Inteiro | Profundidade da transação HTTP |
| `response_body_len` | Inteiro | Tamanho do corpo da resposta HTTP |
| `ct_src_dport_ltm` | Inteiro | Conexões recentes do mesmo IP/porta de destino |
| `ct_dst_sport_ltm` | Inteiro | Conexões recentes ao mesmo IP/porta de origem |
| `is_ftp_login` | Binário | Indica se a sessão FTP foi autenticada (1/0) |
| `ct_ftp_cmd` | Inteiro | Número de comandos FTP na sessão |
| `ct_flw_http_mthd` | Inteiro | Número de métodos HTTP (GET, POST) na conexão |
| `is_sm_ips_ports` | Binário | IPs e portas de origem/destino iguais (1/0) |
| `attack_cat` | Categórico | **Variável-alvo multiclasse** — tipo de ataque ou Normal |
| `label` | Binário (0/1) | **Variável-alvo binária** — 0 = Normal, 1 = Ataque |
 
## Qualidade dos Dados
 
**Pontos positivos:**
- Nenhum valor nulo em nenhuma coluna.
- Dataset publicado em conferência IEEE, amplamente validado pela comunidade científica.
- Treino e teste separados oficialmente, permitindo comparação com literatura.
- Features ricas com significado técnico claro em segurança de redes.
 
**Desafios identificados e tratamentos planejados:**
 
| Problema | Descrição | Tratamento Planejado |
|---|---|---|
| **Duplicatas** | 110.880 registros duplicados (43% do total) | Remoção antes do treinamento |
| **Variáveis categóricas** | `proto`, `service`, `state` são texto | One-Hot Encoding ou Label Encoding |
| **Distribuição treino ≠ teste** | Treino: 50/50 — Teste: 63/37 | Avaliação com métricas robustas (F1, ROC-AUC) |
| **Outliers em features numéricas** | `rate` chega a 1.000.000 e `sload` a ~6 bilhões | Normalização com StandardScaler ou RobustScaler |
| **`attack_cat` como feature** | Seria vazamento de informação (data leakage) | Usada apenas para análise, removida do modelo |
 
## Critérios de Qualidade Atendidos
 
| Critério | Avaliação |
|---|---|
| **Representatividade** |  Tráfego real capturado em laboratório da UNSW com ataques simulados realisticamente |
| **Qualidade dos dados** |  Sem valores nulos; duplicatas identificadas e removíveis |
| **Contexto e significado** |  Todas as 36 colunas têm significado técnico documentado |
| **Ética e privacidade** |  Dados de laboratório controlado; sem dados pessoais reais |
| **Atualidade e relevância** |  Tipos de ataque relevantes; dataset referência na literatura atual |
| **Credibilidade acadêmica** |  Publicado em IEEE, citado em centenas de artigos científicos |
| **Tamanho do dataset** |  146.793 registros após limpeza — muito acima do mínimo exigido |
 
---

# Canvas Analítico

![CanvaAnalitico](/docs/img/novocanvaanalitco.png)

# Referências

MOUSTAFA, N.; SLAY, J. **UNSW-NB15: a comprehensive data set for network intrusion detection systems.** In: MILITARY COMMUNICATIONS AND INFORMATION SYSTEMS CONFERENCE (MilCIS), 2015, Canberra. Anais [...]. IEEE, 2015. DOI: 10.1109/MilCIS.2015.7348942.
 
ONYEBUEKE, A. E.; DAVID, A. A.; MUNU, S. **Network Intrusion Detection System Using XGBoost and Random Forest Algorithms.** Asian Journal of Pure and Applied Mathematics, v. 5, n. 1, p. 321–335, 2023. Disponível em: https://jofmath.com/index.php/AJPAM/article/view/18
 
ANONYMOUS. **Machine Learning for Cybersecurity: Web Attack Detection (Brute Force, XSS, SQL Injection).** InPrime: Indonesian Journal of Pure and Applied Mathematics, v. 7, n. 1, 2025. Disponível em: https://journal.uinjkt.ac.id/index.php/inprime/article/view/41025
 
MDPI. **The Improved Network Intrusion Detection Techniques Using the Feature Engineering Approach with Boosting Classifiers.** Mathematics, v. 12, n. 24, art. 3909, 2024. Disponível em: https://www.mdpi.com/2227-7390/12/24/3909
 
SPRINGER NATURE. **Deep Learning-Based Intrusion Detection for IoT Networks: A Scalable and Efficient Approach.** Journal on Information Security, 2025. Disponível em: https://link.springer.com/article/10.1186/s13635-025-00202-w
 
MDPI. **Top-K Feature Selection for IoT Intrusion Detection: Contributions of XGBoost, LightGBM, and Random Forest.** Future Internet, v. 17, n. 11, art. 529, 2025. Disponível em: https://www.mdpi.com/1999-5903/17/11/529
 
IBM SECURITY. **Cost of a Data Breach Report 2023.** Armonk: IBM Corporation, 2023. Disponível em: https://www.ibm.com/reports/data-breach
 
CYBERSECURITY VENTURES. **Cybercrime to cost the world $10.5 trillion annually by 2025.** 2022. Disponível em: https://cybersecurityventures.com/hackerpocalypse-cybercrime-report-2016/

---