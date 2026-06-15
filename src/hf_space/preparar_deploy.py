"""
preparar_deploy.py
------------------
Copia os artefatos binarios (modelo, escaladores e dataset de referencia)
para a pasta hf_space/, deixando-a pronta para subir ao Hugging Face Spaces.

Execute uma vez antes do push:
    python src/hf_space/preparar_deploy.py
"""
import os
import shutil

# Raiz do hf_space/ e raiz do src/
HF_DIR  = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.abspath(os.path.join(HF_DIR, '..'))

artefatos = [
    (
        os.path.join(SRC_DIR, 'modelos', 'persistencia', 'modelos_persistentes',
                     'stacking', 'stacking_3c.pkl'),
        os.path.join(HF_DIR, 'modelos', 'stacking_3c.pkl'),
    ),
    (
        os.path.join(SRC_DIR, 'analise_exploratoria_pre_processamento',
                     'escalonadores', 'escalonador_robusto.pkl'),
        os.path.join(HF_DIR, 'escalonadores', 'escalonador_robusto.pkl'),
    ),
    (
        os.path.join(SRC_DIR, 'analise_exploratoria_pre_processamento',
                     'escalonadores', 'escalonador_minmax.pkl'),
        os.path.join(HF_DIR, 'escalonadores', 'escalonador_minmax.pkl'),
    ),
    (
        os.path.join(SRC_DIR, 'dataset', 'pre_processado',
                     'treino_pp_sem_normalizacao.parquet'),
        os.path.join(HF_DIR, 'dados', 'treino_pp_sem_normalizacao.parquet'),
    ),
]

for origem, destino in artefatos:
    if not os.path.exists(origem):
        print(f'[ERRO] Arquivo nao encontrado: {origem}')
        continue
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    shutil.copy2(origem, destino)
    tamanho_mb = os.path.getsize(destino) / (1024 * 1024)
    print(f'[OK] {os.path.basename(origem):45s} -> {os.path.relpath(destino, HF_DIR)}  ({tamanho_mb:.2f} MB)')

print('\nArtefatos copiados. Estrutura do hf_space/ pronta para deploy.')
print('Proximos passos:')
print('  1. Crie um novo Space em huggingface.co (SDK: Streamlit)')
print('  2. Clone o repositorio do Space localmente')
print('  3. Copie o conteudo de src/hf_space/ para a raiz do clone')
print('  4. git add . && git commit -m "deploy inicial" && git push')
