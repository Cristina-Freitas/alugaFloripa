"""
Limpeza, engenharia de atributos e preparação para modelagem (Fases 2, 3 e 4 do notebook).
"""

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicatas completas, aplica o recorte do problema e imputa valores ausentes pela mediana."""
    df = df.copy()
    df = df.drop_duplicates()

    df["data"] = pd.to_datetime(df["data"], errors="coerce")

    df = df[
        (df["categoria"] == "Residencial") &
        (df["periodicidade"] == "Mês")
    ].copy()

    tipos_residenciais = [
        "Apartamento",
        "Casa",
        "Kitnet/Conjugado",
        "Loft",
        "Flat",
        "Fazenda/Sítio/Chácara",
    ]

    df = df[df["tipo"].isin(tipos_residenciais)].copy()    

    df = df.sort_values("data")
    df = df.drop_duplicates(subset=["id"], keep="last")

    df["qtd_banheiros"] = df["qtd_banheiros"].fillna(df["qtd_banheiros"].median())
    df["qtd_quartos"] = df["qtd_quartos"].fillna(df["qtd_quartos"].median())
    df["qtd_vagas"] = df["qtd_vagas"].fillna(df["qtd_vagas"].median())

    return df.reset_index(drop=True)


def cap_iqr(serie: pd.Series, fator: float = 1.5) -> pd.Series:
    """Winsorização por IQR: valores fora de [Q1 - fator*IQR, Q3 + fator*IQR]
    são limitados ao limite mais próximo, em vez de removidos."""
    q1, q3 = serie.quantile(0.25), serie.quantile(0.75)
    iqr = q3 - q1
    limite_inf, limite_sup = q1 - fator * iqr, q3 + fator * iqr
    return serie.clip(limite_inf, limite_sup)


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Cria colunas derivadas para auxiliar a modelagem."""
    df = df.copy()
    df["area_por_quarto"] = df["area"] / df["qtd_quartos"].replace(0, pd.NA)
    df["area_por_quarto"] = df["area_por_quarto"].fillna(df["area_por_quarto"].median())
    df["tem_vaga"] = (df["qtd_vagas"] > 0).astype(int)
    return df


def select_final_columns(df: pd.DataFrame, feature_cols: list[str], target_col: str) -> pd.DataFrame:
    """Seleciona apenas as variáveis explicativas e o alvo usadas na modelagem."""
    return df[feature_cols + [target_col]].copy()