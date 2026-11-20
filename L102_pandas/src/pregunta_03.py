from pathlib import Path
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "tbl0.tsv"

"""
Usando `data/tbl0.tsv`, cuente cuántos registros hay para cada categoría
de la columna `c1`. Retorne una Serie de Pandas cuyo índice son las
categorías, en orden alfabético, y cuyos valores son las cantidades.
Ejemplo del formato de la respuesta:
    c1
    A     8
    B     7
    C     5
    ...
"""

def pregunta_03():
    df = pd.read_csv(DATA_FILE, delimiter="\t")
    series = df["c1"].value_counts().sort_index(ascending=True)
    return series
