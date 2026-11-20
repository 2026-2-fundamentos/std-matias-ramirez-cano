from pathlib import Path
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "tbl0.tsv"

"""
Usando `data/tbl0.tsv`, encuentre el valor máximo de la columna `c2` para
cada categoría de la columna `c1`. Retorne una Serie de Pandas cuyo índice
son las categorías, en orden alfabético, y cuyos valores son los máximos.
Ejemplo del formato de la respuesta:
    c1
    A    9
    B    9
    C    9
    ...
"""

def pregunta_05():
    df = pd.read_csv(DATA_FILE, delimiter="\t")
    series = df.groupby("c1", sort=True, as_index=True)["c2"].max()
    return series
