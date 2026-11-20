from pathlib import Path
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE_A = ACTIVITY_DIR / "data" / "tbl0.tsv"
DATA_FILE_B = ACTIVITY_DIR / "data" / "tbl2.tsv"

"""
Combine las tablas `data/tbl0.tsv` y `data/tbl2.tsv` usando la columna
`c0`, que ambas comparten. Luego, sume los valores de la columna `c5b`
para cada categoría de la columna `c1`. Retorne una Serie de Pandas cuyo
índice son las categorías, en orden alfabético, y cuyos valores son las
sumas.
Ejemplo del formato de la respuesta:
    c1
    A    146
    B    134
    C     81
    ...
"""

def pregunta_13():
    df_a = pd.read_csv(DATA_FILE_A, delimiter="\t")
    df_b = pd.read_csv(DATA_FILE_B, delimiter="\t")
    df = pd.merge(df_a, df_b, how="inner", on="c0")
    series = df.groupby("c1", sort=True, as_index=True)["c5b"].sum()
    return series
