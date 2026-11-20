from pathlib import Path
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ACTIVITY_DIR / "data" / "tbl0.tsv"

"""
Retorne la tabla `data/tbl0.tsv` completa con una columna adicional
llamada `suma`, al final, cuyo valor en cada fila es `c0 + c2`.
Ejemplo del formato de la respuesta:
        c0 c1  c2          c3  suma
    0    0  E   1  1999-02-28     1
    1    1  A   2  1999-10-28     3
    2    2  B   5  1998-05-02     7
    ...
"""

def pregunta_08():
    df = pd.read_csv(DATA_DIR, delimiter="\t")
    df["suma"] = df["c0"] + df["c2"]
    return df
