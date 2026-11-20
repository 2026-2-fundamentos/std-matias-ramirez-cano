from pathlib import Path
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "tbl0.tsv"

"""
Usando `data/tbl0.tsv`, construya para cada categoría de la columna `c1`
un texto con todos sus valores de la columna `c2`, ordenados de menor a
mayor y separados por `:`. Retorne un DataFrame cuyo índice son las
categorías, en orden alfabético, con una única columna llamada `c2`.
Ejemplo del formato de la respuesta:
                       c2
    c1
    A     1:1:2:3:6:7:8:9
    B       1:3:4:5:6:8:9
    C           0:5:6:7:9
    ...
"""

def aggregator(series):
    series = series.sort_values(ascending=True).astype("string")
    return series.str.cat(sep=":")
    
def pregunta_10():
    df = pd.read_csv(DATA_FILE, delimiter="\t")
    series = df.groupby("c1", sort=True, as_index=True)["c2"].agg(aggregator)
    return series.to_frame(name="c2")
