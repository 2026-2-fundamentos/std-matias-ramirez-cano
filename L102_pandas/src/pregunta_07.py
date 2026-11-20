from pathlib import Path
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "tbl0.tsv"

"""
Usando `data/tbl0.tsv`, sume los valores de la columna `c2` para cada
categoría de la columna `c1`. Retorne una Serie de Pandas cuyo índice son
las categorías, en orden alfabético, y cuyos valores son las sumas.
Ejemplo del formato de la respuesta:
    c1
    A    37
    B    36
    C    27
    ...
"""

def pregunta_07():
    df = pd.read_csv(DATA_FILE, delimiter="\t")
    series = df.groupby("c1", sort=True, as_index=True)["c2"].sum()
    return series
