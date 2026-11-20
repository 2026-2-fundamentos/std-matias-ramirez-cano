from pathlib import Path
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "tbl0.tsv"

"""
Usando `data/tbl0.tsv`, calcule el promedio de la columna `c2` para cada
categoría de la columna `c1`. Retorne una Serie de Pandas cuyo índice son
las categorías, en orden alfabético, y cuyos valores son los promedios.
Ejemplo del formato de la respuesta:
    c1
    A    4.6250
    B    5.1429
    C    5.4000
    ...
"""

def pregunta_04():
    df = pd.read_csv(DATA_FILE, delimiter="\t")
    series = df.groupby("c1", sort=True, as_index=True)["c2"].mean()
    return series
