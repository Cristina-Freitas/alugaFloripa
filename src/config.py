"""
Caminhos e parâmetros centrais do projeto, usados pelo notebook e pelos
módulos de src/.
"""

from pathlib import Path  # Importa Path para trabalhar com caminhos de arquivos e pastas


ROOT_DIR = Path(__file__).resolve().parent.parent  # Define a raiz do projeto a partir da pasta src

RAW_FILE = ROOT_DIR / "data" / "raw" / "full_history.csv"  # Caminho do arquivo bruto original

PROCESSED_DIR = ROOT_DIR / "data" / "processed"  # Caminho da pasta onde será salvo o dataset tratado
PROCESSED_FILE = PROCESSED_DIR / "aluguel_floripa_processed.csv"  # Caminho do arquivo tratado

FINAL_DIR = ROOT_DIR / "data" / "final"  # pasta do dataset final para modelagem
FINAL_FILE = FINAL_DIR / "aluguel_floripa_final.csv"  # arquivo final usado na modelagem

FIGURES_DIR = ROOT_DIR / "outputs" / "figures"  # pasta onde os gráficos serão salvos

MODEL_DIR = ROOT_DIR / "models" / "v1"  # pasta onde será salvo o modelo versão 1
MODEL_FILE = MODEL_DIR / "modelo_regressao_v1.pkl"  # arquivo do modelo de regressão v1
METRICS_FILE = MODEL_DIR / "metricas_v1.json"  # arquivo JSON com as métricas do modelo v1

TARGET_COL = "valor"  # variável-alvo do projeto, ou seja, o valor do aluguel

FEATURE_COLS = [  
    "bairro",  
    "tipo",  
    "area",  
    "quartos",  
    "banheiros",  
    "vagas",  
    "condominio",  
]

TEST_SIZE = 0.2  # 20% para teste
RANDOM_STATE = 42  # Garante que a divisão treino/teste seja sempre igual ao reexecutar o notebook