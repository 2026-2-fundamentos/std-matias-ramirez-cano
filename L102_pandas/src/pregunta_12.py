from pathlib import Path
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "tbl2.tsv"

"""
En `data/tbl2.tsv`, cada valor de la columna `c0` aparece en varias
filas. Construya un DataFrame con una fila por cada valor de `c0`, en
orden ascendente, y las columnas `c0` y `c5`. En `c5`, forme un texto
`c5a:c5b` para cada fila de ese `c0`, ordene esos textos alfabéticamente y
únalos separados por comas.
Ejemplo del formato de la respuesta:
        c0                             c5
    0    0  bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1    1        aaa:3,ccc:2,ddd:0,hhh:9
    2    2        ccc:6,ddd:2,ggg:5,jjj:1
    ...
"""
def aggregator(series):
    return series.sort_values().str.cat(sep=",")

def pregunta_12():
    df =pd.read_csv(DATA_FILE, delimiter="\t")
    df["c5a"] = df["c5a"].astype("string")
    df["c5b"] = df["c5b"].astype("string")
    df["c5"] = df["c5a"] + ":" + df["c5b"]
    res_df = df.groupby("c0", sort=True, as_index=False)[["c0", "c5"]].agg({"c5":aggregator})
    return res_df 
