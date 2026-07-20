"""
Funções de plotagem usadas ao longo do notebook.

Cada função gera uma figura, salva em outputs/figures/ e exibe o gráfico.
"""

import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns  
import pandas as pd 

from src.config import FIGURES_DIR  


def _savefig(filename: str) -> None:
    """Salva a figura atual na pasta outputs/figures/."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)  # Cria a pasta de figuras
    plt.savefig(FIGURES_DIR / filename, bbox_inches="tight", dpi=150)  # Salva a figura com boa resolução


def plot_histogram(serie: pd.Series, titulo: str, filename: str) -> None:
    """Histograma com curva de densidade (KDE) de uma variável numérica."""
    fig, ax = plt.subplots(figsize=(9, 5))  # Cria a área do gráfico
    sns.histplot(serie, bins=60, kde=True, ax=ax, color="#2E7D32")  # Cria histograma com curva KDE
    ax.set_title(titulo)  # Define o título do gráfico
    plt.tight_layout()  # Ajusta os espaçamentos do gráfico
    _savefig(filename)  # Salva o gráfico na pasta outputs/figures
    plt.show()  # Exibe o gráfico no notebook


def plot_boxplots(df: pd.DataFrame, cols: list[str], filename: str) -> None:
    """Um boxplot por coluna, lado a lado - útil para inspeção visual de outliers."""
    fig, axes = plt.subplots(1, len(cols), figsize=(3.5 * len(cols), 4.5))  # Cria uma área para cada boxplot
    for ax, col in zip(axes, cols):  # Percorre cada eixo e cada coluna informada
        sns.boxplot(y=df[col], ax=ax, color="#9CCC65")  # Cria o boxplot da coluna atual
        ax.set_title(col)  # Define o título do boxplot com o nome da coluna
    plt.tight_layout()  # Ajusta os espaçamentos
    _savefig(filename)  # Salva o gráfico
    plt.show()  # Exibe o gráfico no notebook


def plot_scatter(df: pd.DataFrame, x: str, y: str, filename: str) -> None:
    """Dispersão entre duas variáveis numéricas."""
    fig, ax = plt.subplots(figsize=(7, 5))  # Cria a área do gráfico
    sns.scatterplot(data=df, x=x, y=y, alpha=0.25, s=15, ax=ax, color="#2E7D32")  # Cria o gráfico de dispersão
    ax.set_title(f"{x} x {y}")  # Define o título do gráfico
    plt.tight_layout()  # Ajusta os espaçamentos
    _savefig(filename)  # Salva o gráfico
    plt.show()  # Exibe o gráfico no notebook


def plot_correlation_heatmap(df: pd.DataFrame, filename: str) -> None:
    """Mapa de calor de correlação de Pearson entre variáveis numéricas."""
    corr = df.select_dtypes(include=np.number).corr()  # Calcula a correlação apenas entre colunas numéricas
    fig, ax = plt.subplots(figsize=(12, 10))  # Cria a área do gráfico
    sns.heatmap(corr, cmap="RdYlGn", center=0, ax=ax)  # Cria o heatmap de correlação
    ax.set_title("Correlação de Pearson entre variáveis numéricas")  # Define o título do gráfico
    plt.tight_layout()  # Ajusta os espaçamentos
    _savefig(filename)  # Salva o gráfico
    plt.show()  # Exibe o gráfico no notebook


def plot_observed_vs_predicted(y_true, y_pred, titulo: str, filename: str) -> None:
    """Valores reais x valores previstos - quanto mais perto da diagonal, melhor."""
    fig, ax = plt.subplots(figsize=(7, 6))  # Cria a área do gráfico
    ax.scatter(y_true, y_pred, alpha=0.25, s=15, color="#2E7D32")  # Plota valores reais contra previstos
    lims = [min(y_true.min(), y_pred.min()), max(y_true.max(), y_pred.max())]  # Define limites iguais para os eixos
    ax.plot(lims, lims, "--", color="#C62828", linewidth=1.5, label="Ajuste perfeito")  # Linha ideal
    ax.set_xlabel("Aluguel real (R$)")  # Define o rótulo do eixo X
    ax.set_ylabel("Aluguel previsto (R$)")  # Define o rótulo do eixo Y
    ax.set_title(titulo)  # Define o título do gráfico
    ax.legend()  # Exibe a legenda
    plt.tight_layout()  # Ajusta os espaçamentos
    _savefig(filename)  # Salva o gráfico
    plt.show()  # Exibe o gráfico no notebook


def plot_residuals(y_true, y_pred, titulo: str, filename: str) -> pd.Series:
    """Resíduos (real - previsto) versus valores previstos. Devolve os resíduos calculados."""
    residuos = y_true - y_pred  # Calcula os resíduos do modelo
    fig, ax = plt.subplots(figsize=(8, 5))  # Cria a área do gráfico
    ax.scatter(y_pred, residuos, alpha=0.7, color="#9CCC65")  # Plota resíduos contra valores previstos
    ax.axhline(0, color="#C62828", linestyle="--", linewidth=1.5)  # Linha horizontal no zero
    ax.set_xlabel("Aluguel previsto (R$)")  # Define o rótulo do eixo X
    ax.set_ylabel("Resíduo (real - previsto, em R$)")  # Define o rótulo do eixo Y
    ax.set_title(titulo)  # Define o título do gráfico
    plt.tight_layout()  # Ajusta os espaçamentos
    _savefig(filename)  # Salva o gráfico
    plt.show()  # Exibe o gráfico no notebook
    return residuos  # Retorna os resíduos calculados