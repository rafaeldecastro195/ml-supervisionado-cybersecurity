# Instruções de utilização

O sistema é uma aplicação web de detecção de ameaças cibernéticas desenvolvida em Python com Streamlit, que utiliza um modelo de Machine Learning (Stacking Ensemble) para classificar conexões de rede como tráfego normal ou ataque.

## Acesso à aplicação publicada

A aplicação está hospedada no Hugging Face Spaces e pode ser acessada diretamente pelo navegador, sem necessidade de instalação:

**https://huggingface.co/spaces/vitoriasoares/deteccao-ameacas-ciberneticas**

## Execução local

Para executar a aplicação localmente, é necessário ter o Python 3.10 ou superior instalado.

### 1. Instalar as dependências
pip install -r src/hf_space/requirements.txt

### 2. Preparar os artefatos do modelo
python src/hf_space/preparar_deploy.py

### 3. Executar a aplicação
streamlit run src/app/app_streamlit.py

A aplicação abrirá automaticamente no navegador em `http://localhost:8501`.

## Como utilizar

1. Preencha os campos com os dados de uma conexão de rede (protocolo, serviço, estado, métricas de fluxo e pacotes).
2. Os campos já vêm preenchidos com valores padrão (mediana do conjunto de treino), podendo ser ajustados.
3. Clique em **Classificar conexão**.
4. O sistema retorna a classificação (NORMAL ou ATAQUE), a probabilidade de ataque e o threshold utilizado.

## Tecnologias utilizadas

- **Python** — linguagem principal
- **Streamlit** — interface web
- **Scikit-learn / XGBoost** — modelos de Machine Learning
- **Docker** — empacotamento para deploy
- **Hugging Face Spaces** — hospedagem em nuvem

## Histórico de versões

### [1.0.0] - 2026

Adicionado:
- Interface web em Streamlit para inferência dinâmica
- Modelo Stacking Ensemble (MLP 3 camadas) em produção
- Deploy em nuvem via Hugging Face Spaces
- Documentação completa do processo de implantação
