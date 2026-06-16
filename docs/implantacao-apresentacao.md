# Etapa 5 — Implantação da Solução

## 1. Visão Geral

Esta etapa descreve o processo de implantacao do sistema de deteccao de ameacas ciberneticas em ambiente de computacao em nuvem. A solucao realiza **inferencia dinamica** sobre os modelos treinados nas etapas anteriores: o usuario fornece os dados de uma conexao de rede por meio de uma interface web, e o sistema retorna a classificacao em tempo de execucao — sem nenhum reprocessamento ou retreinamento.

- **Modelo em producao:** Stacking Ensemble com MLP de tres camadas ocultas (`stacking_3c.pkl`)  
- **Interface:** Streamlit  
- **Provedor de nuvem:** Hugging Face Spaces  
- **Threshold de classificacao:** 0.7453 (otimizado para F1, acuracia de 89,73%)  
- **Aplicacao publicada:** https://huggingface.co/spaces/vitoriasoares/deteccao-ameacas-ciberneticas
- **Relatório do desenvolvimento do projeto:** https://docs.google.com/document/d/1ni0YwOBFEJzJ2LEP2fw3aMofTzHM7MeyWrmDk_6yb4o/edit?tab=t.0

---

## 2. Avaliação dos Provedores de Nuvem

Para selecionar o ambiente de deploy, foram avaliados quatro provedores com base nos criterios relevantes para um prototipo academico de inferencia com ML.

### 2.1 Critérios de Avaliação

| Critério | Peso | Descrição |
|---|---|---|
| Custo para protótipo | Alto | Viabilidade financeira para um projeto acadêmico sem patrocínio |
| Tempo de configuração | Alto | Horas necessárias atá o primeiro deploy funcional |
| Suporte nativo a Streamlit | Médio | Capacidade de servir apps Streamlit sem container manual |
| Recursos de compute | Médio | CPU e RAM disponiveis no tier gratuito |
| Escalabilidade futura | Baixo | Possibilidade de crescimento para uso real |
| Curva de aprendizado | Alto | Requisito de conhecimento previo em cloud |

### 2.2 Comparativo

| Critério | AWS SageMaker | Azure ML | GCP Vertex AI | **HF Spaces** |
|---|---|---|---|---|
| Custo (prototipo) | ~US$50+/mes | ~US$50+/mes | ~US$50+/mes | **Gratuito** |
| Tempo de configuracao | 2–5 dias | 2–5 dias | 2–5 dias | **< 1 hora** |
| Suporte a Streamlit | Via container | Via container | Via container | **Nativo** |
| Compute gratuito | Limitado/pago | Limitado/pago | Limitado/pago | **2 vCPU, 16 GB RAM** |
| Escalabilidade | Alta | Alta | Alta | Limitada |
| Curva de aprendizado | Alta | Alta | Alta | **Baixa** |
| Cartão de credito | Obrigatório | Obrigatório | Obrigatório | **Não necessário** |

### 2.3 Análise por Provedor

**AWS SageMaker**  
Oferece endpoints gerenciados de ML com alta disponibilidade e integração com o ecossistema AWS (S3, Lambda, CloudWatch). Para um protótipo acadêmico, porém, a configuração exige criação de roles IAM, VPCs, buckets S3 e configuraçãoo de endpoints — processo que consome vários dias e requer conhecimento avançado de cloud. O custo de uma instância ml.t3.medium para servir o modelo seria de aproximadamente US$0,05/hora, acumulando custos mesmo sem uso.

**Azure Machine Learning**  
Similar ao AWS em complexidade. O Azure ML oferece pipelines gerenciados e integração com Azure DevOps, mas exige configuração de workspace, registro de modelos no Azure Container Registry e autenticação via Azure Active Directory. Adequado para organizações com infraestrutura Azure existente, não para projetos acadêmicos pontuais.

**Google Cloud Vertex AI**  
Plataforma robusta com suporte a Scikit-Learn e XGBoost nativos via endpoints gerenciados. O modelo Stacking seria servido como um Custom Prediction Routine. A curva de aprendizado e semelhante a AWS e Azure, com custos de instância a partir de US$0,046/hora para n1-standard-2.

**Hugging Face Spaces**  
Plataforma de hospedagem de aplicações ML que oferece suporte nativo ao Streamlit SDK. O deploy e feito via push em um repositório git gerenciado pela plataforma. O tier gratuito disponibiliza 2 vCPUs e 16 GB de RAM, sem necessidade de cartão de credito. Ideal para protótipos acadêmicos e demos publicas.

---

## 3. Justificativa da Escolha: Hugging Face Spaces

A escolha do Hugging Face Spaces como provedor de deploy foi fundamentada em três eixos:

### 3.1 Adequação ao Escopo

O sistema de detecção de ameacas cibernéticas desenvolvido e um **protótipo acadêmico de demonstração**. O objetivo da Etapa 5 e demonstrar que o modelo treinado consegue realizar inferência dinâmica em produção — não construir infraestrutura de produção corporativa. Para esse propósito, o HF Spaces e a escolha mais direta e eficiente.

### 3.2 Custo-Benefício

O tier gratuito do HF Spaces oferece:
- **2 vCPUs** — suficientes para servir múltiplas predições simultâneas (ver Seção 5)
- **16 GB de RAM** — capacidade muito superior ao necessário (modelo + escaladores + dados de referência: < 500 MB)
- **Disponibilidade 24/7** sem custo
- **Sem cobranca** por requisição ou tempo de execução

Qualquer provedor cloud tradicional (AWS, Azure, GCP) geraria custo mínimo de US$30–60/mes para servico equivalente.

### 3.3 Tempo de Entrega e Reprodutibilidade

O deploy no HF Spaces e realizado em menos de uma hora:
1. Criar o Space (interface web, 2 minutos)
2. Executar `preparar_deploy.py` para copiar os artefatos (< 1 minuto)
3. Fazer push do conteudo de `hf_space/` para o repositório do Space (< 5 minutos)
4. O HF Spaces constroi e sobe o container automaticamente (< 5 minutos)

Toda a equipe consegue replicar o processo sem conta em provedor cloud, sem configuracao de IAM/VPC e sem conhecimento previo de DevOps.

---

## 4. Estrutura de Implantação

### 4.1 Arquivos do Deploy

A pasta `src/hf_space/` contém todos os arquivos necessarios para o deploy:

```
hf_space/
├── Dockerfile                    <- Define a imagem Docker; roda Streamlit na porta 7860
├── README.md                     <- Frontmatter lido pelo HF Spaces (sdk: docker, app_port: 7860)
├── app.py                        <- Ponto de entrada do Streamlit (raiz do Space)
├── requirements.txt              <- Dependências com versões fixadas
├── predexan/
│   ├── __init__.py
│   ├── deploy.py                 <- Classe Feature para processamento de entrada
│   └── preproc.py                <- Funcão de normalizacao
├── modelos/
│   └── stacking_3c.pkl           <- Copiado por preparar_deploy.py
├── escalonadores/
│   ├── escalonador_robusto.pkl   <- Copiado por preparar_deploy.py
│   └── escalonador_minmax.pkl    <- Copiado por preparar_deploy.py
└── dados/
    └── treino_pp_sem_normalizacao.parquet  <- Copiado por preparar_deploy.py
```

O `Dockerfile` usa `python:3.12-slim` como imagem base, cria um usuário nao-root com uid 1000 (exigido pelo HF Spaces), instala as dependências em uma camada separada do codigo-fonte para aproveitar o cache de build, e inicializa o Streamlit com `--server.port=7860 --server.address=0.0.0.0`. Ao receber o push, o HF Spaces constrói a imagem automaticamente e sobe o container.

### 4.2 Dependências

```
streamlit>=1.31.0
pandas==3.0.2
numpy==2.4.4
scikit-learn==1.8.0
xgboost==3.2.0
joblib==1.5.3
pyarrow==23.0.1
scipy==1.17.1
```

As versões de `scikit-learn` e `xgboost` foram fixadas nas mesmas versões usadas no treinamento para garantir compatibilidade com os arquivos `.pkl` gerados pelo `joblib`. Divergência de versão nessas bibliotecas pode causar falha no `joblib.load()`.

### 4.3 Pipeline de Inferência Dinâmica

O `app.py` implementa o seguinte fluxo em tempo de execucao:

```
Entrada do usuario (formulario Streamlit)
        |
        v
Dados numericos contínuos (21 features)  -->  RobustScaler.transform()  -->  DataFrame normalizado
Dados numericos limitados (10 features)  -->  MinMaxScaler.transform()  -->  DataFrame normalizado
Selecoes categoricas (3 dropdowns)       -->  One-hot encoding manual   -->  DataFrame binario
        |
        v
pd.concat() + reordenacao pela ordem_original do treino
        |
        v
stacking_3c.predict_proba() --> probabilidade de ataque [0, 1]
        |
        v
Threshold 0.7453 --> "ATAQUE" ou "NORMAL"
        |
        v
Exibicao: metrica de probabilidade, classificacao colorida, barra de progresso
```

O modelo e os escaladores sao carregados uma unica vez na inicializacao do servidor (`@st.cache_resource`) e reutilizados em todas as requisicoes subsequentes.

---

## 5. Planejamento de Capacidade

### 5.1 Dados de Consumo de Recursos (medidos nos notebooks)

Os dados abaixo foram obtidos nos notebooks de avaliacao dos modelos (`escolha_modelo.ipynb`), medindo o consumo de CPU durante a execucao do conjunto de teste (49.971 amostras):

| Modelo | Acuracia (F1-otimizado) | CPU (%) | RAM adicional |
|---|---|---|---|
| XGBoost | 89,87% | 100% (referencia) | ~200 MB |
| **Stacking 3-layer** | **89,73%** | **30,7%** | ~220 MB |
| Stacking 2-layer | 88,01% | 71,2% | ~210 MB |
| MLP 3-layer | 83,86% | 22,4% | ~190 MB |
| MLP 2-layer | 88,03% | 27,0% | ~185 MB |
| Regressao Logistica | 67,93% | < 5% | ~50 MB |

O Stacking 3-layer foi escolhido por apresentar a segunda maior acuracia (apenas 0,14% abaixo do XGBoost) com apenas 30,7% do consumo de CPU do XGBoost — economia de 69,3% em compute.

### 5.2 Modelagem de Capacidade para o HF Spaces

**Ambiente disponivel:** 2 vCPUs logicas, 16 GB RAM

**Premissas do modelo:**
- 1 predicao consome aproximadamente 30,7% de 1 vCPU durante o processamento
- O tempo de inferencia e muito menor que 1 segundo (operacao sobre 1 amostra)
- O gargalo e CPU, nao memoria (modelo + dados: ~500 MB de 16 GB disponíveis)

**Capacidade teorica por nucleo:**

```
1 vCPU disponivel por nucleo
Consumo por predicao = 0,307 de 1 vCPU

Requisicoes simultaneas por nucleo = 1 / 0,307 ≈ 3,26 requisicoes
```

**Com 2 vCPUs:**

```
Capacidade total = 2 × 3,26 ≈ 6,5 requisicoes simultaneas
```

**Conclusao:** o tier gratuito do HF Spaces suporta aproximadamente **6 a 7 usuarios simultaneos** sem degradacao de performance. Para um uso academico de demonstracao (tipicamente < 5 usuarios concorrentes), a capacidade e adequada com margem de seguranca.

### 5.3 Projecao para Escala de Producao Real

Para um cenario de producao corporativa (ex: monitoramento de rede com 1.000 eventos/segundo):

| Requisito | Calculo | Instancia equivalente |
|---|---|---|
| 1.000 req/s | 1.000 × 0,307 = 307 vCPUs | ~80 instancias c5.4xlarge (AWS) |
| 100 req/s | 100 × 0,307 = 30,7 vCPUs | ~8 instancias c5.4xlarge (AWS) |
| 10 req/s | 10 × 0,307 = 3,07 vCPUs | 1 instancia c5.xlarge (AWS) |

Para escala real, a recomendacao seria:
1. Implantar o modelo em **AWS SageMaker** ou **GCP Vertex AI** com auto-scaling
2. Usar instancias otimizadas para CPU (familia `c5` na AWS ou `c2` no GCP)
3. Configurar o threshold de auto-scaling em 70% de utilizacao de CPU
4. Monitorar latencia de predicao via CloudWatch/Cloud Monitoring

---

## 6. Monitoramento e Observabilidade

### 6.1 Monitoramento no HF Spaces

O Hugging Face Spaces oferece observabilidade basica diretamente no painel do Space:

- **Status do Space:** indicador visual com tres estados — `Building` (construindo a imagem Docker), `Running` (container ativo e respondendo) e `Error` (falha no build ou no processo do container). Qualquer mudanca de estado e imediatamente visivel na interface web.
- **Aba "Logs" — Build Logs:** exibe a saida completa do `docker build`, incluindo instalacao de dependencias e erros de compilacao. Util para diagnosticar falhas causadas por incompatibilidade de versoes ou artefatos faltando.
- **Aba "Logs" — Container Logs:** exibe a saida do processo Streamlit em tempo real (stdout/stderr do container). Permite detectar erros de inferencia, traceback de excecoes e mensagens de degradacao de performance enquanto o Space esta em execucao.

### 6.2 Limitacoes do Tier Gratuito

O plano gratuito do HF Spaces **nao oferece**:
- Metricas historicas de CPU, memoria ou latencia
- Alertas automaticos por email ou webhook em caso de falha
- Dashboard de utilizacao com graficos temporais
- SLA de disponibilidade garantida

O monitoramento fica restrito a observacao manual dos logs. Spaces inativos por periodo prolongado podem ser pausados automaticamente pela plataforma.

### 6.3 Estrategia para Producao Real

Em um ambiente de producao corporativa, recomenda-se a seguinte arquitetura de observabilidade:

**Alertas e metricas (AWS CloudWatch ou GCP Cloud Monitoring)**
- Alerta de CPU > 70% por mais de 5 minutos → escalar horizontalmente
- Alerta de latencia de inferencia > 2 segundos → investigar gargalo
- Alerta de taxa de erro HTTP > 1% → verificar saude do container

**Auto-scaling**
- Configurar politica de scaling baseada em CPU (threshold: 70%)
- Minimo de 1 instancia, maximo definido pelo orcamento e SLA
- Cooldown de 3 minutos para evitar flapping

**Logging estruturado para auditoria**
- Registrar em log cada predicao: timestamp, features de entrada (anonimizadas), probabilidade retornada, classificacao final e tempo de resposta
- Armazenar logs em S3/GCS com retencao de 90 dias
- Monitorar distribuicao das probabilidades ao longo do tempo para detectar **drift do modelo**: se a distribuicao se afastar significativamente da distribuicao observada no conjunto de teste (UNSW-NB15), pode indicar mudanca no padrao do trafego de rede e necessidade de retreinamento

**Health checks**
- Configurar endpoint `/health` ou verificacao periodica do formulario de predicao a cada 60 segundos
- Remover instancias nao-responsivas do load balancer automaticamente

---

## 7. Guia de Deploy no Hugging Face Spaces

### Requisitos
- Conta gratuita em [huggingface.co](https://huggingface.co)
- Python 3.10+ instalado localmente
- Git instalado

### Passo a Passo

**1. Preparar os artefatos binarios**

Execute a partir da raiz do repositorio:
```bash
python src/hf_space/preparar_deploy.py
```

O script copia automaticamente os arquivos `.pkl` e o `.parquet` para `src/hf_space/`.

**2. Criar o Space no Hugging Face**

- Acesse huggingface.co e faca login
- Clique em "New Space"
- Preencha: nome do Space, visibilidade (Public), SDK: **Docker (template Blank)**
- Clique em "Create Space"

**3. Clonar e subir o conteudo**

```bash
# Clonar o repositorio do Space
git clone https://huggingface.co/spaces/SEU_USUARIO/NOME_DO_SPACE

# Copiar o conteudo de hf_space/ para o clone
cp -r src/hf_space/* NOME_DO_SPACE/

# Commit e push (o Dockerfile e enviado junto com os demais arquivos)
cd NOME_DO_SPACE
git add .
git commit -m "deploy inicial - stacking_3c"
git push
```

O push dispara automaticamente a construcao da imagem Docker pelo HF Spaces. Nenhuma configuracao adicional de container e necessaria.

**4. Acompanhar o build**

No painel do Space, a aba "Logs" mostra o progresso da construcao da imagem Docker e da inicializacao do Streamlit. O Space fica disponivel em:

```
https://huggingface.co/spaces/SEU_USUARIO/NOME_DO_SPACE
```

### Metadata do Space (README.md)

O HF Spaces le o frontmatter do `README.md` para configurar o Space. Crie o arquivo com:

```yaml
---
title: Deteccao de Ameacas Ciberneticas
colorFrom: red
colorTo: blue
sdk: docker
app_port: 7860
pinned: false
---
```

---

## 8. Testes de Funcionamento

### 8.1 Teste Local

Para testar o app localmente antes do deploy:

```bash
pip install streamlit>=1.31.0
cd src/app
streamlit run app_streamlit.py
```

O app abre no navegador em `http://localhost:8501`.

### 8.2 Casos de Teste

**Caso 1 — Trafego normal (valores tipicos de conexao HTTP)**

| Feature | Valor |
|---|---|
| Protocolo | tcp |
| Servico | http |
| Estado | FIN |
| Duracao | 0.05 seg |
| Total bytes origem | 1500 bytes |
| Total bytes destino | 8000 bytes |

Resultado esperado: **NORMAL** (probabilidade de ataque < 74,53%)

**Caso 2 — Possivel ataque DoS (alto volume de pacotes, curta duracao)**

| Feature | Valor |
|---|---|
| Protocolo | tcp |
| Servico | outros |
| Estado | CON |
| Duracao | 0.001 seg |
| Num pacotes origem | valor alto (proximo ao maximo) |
| Taxa de pacote | valor alto |

Resultado esperado: **ATAQUE** (probabilidade >= 74,53%)

### 8.3 Validacao da Inferencia Dinamica

A inferencia e dinamica quando:
- O modelo nao e retreinado a cada predicao (verificavel pelo tempo de resposta < 1s)
- O usuario pode fornecer qualquer combinacao valida de valores dentro dos limites do dataset
- A resposta muda conforme os valores de entrada mudam (sem cache de predicao)

---

## 9. Conclusoes

O deploy no Hugging Face Spaces atende integralmente aos requisitos da Etapa 5:

- **Inferencia dinamica:** o modelo `stacking_3c.pkl` e carregado uma vez e realiza predicoes em tempo real para qualquer entrada fornecida pelo usuario
- **Interface de entrada:** formulario Streamlit com 31 campos numericos e 3 selecoes categoricas, com limites validados automaticamente a partir do dataset de treinamento
- **Sem retreinamento:** os escaladores e o modelo sao apenas chamados via `.transform()` e `.predict_proba()` — nenhuma escrita ou atualizacao de modelo ocorre
- **Custo zero:** o tier gratuito do HF Spaces e suficiente para o escopo academico
- **Capacidade adequada:** ~6-7 usuarios simultaneos com os 2 vCPUs disponiveis, contra uma demanda esperada de < 5 no contexto de demonstracao

Para producao real em escala de rede corporativa, a recomendacao e migrar para AWS SageMaker ou GCP Vertex AI com auto-scaling baseado em CPU, com custo estimado de US$0,046–0,05/hora por instancia de compute otimizado.
