from pathlib import Path
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "tbl1.tsv"

"""
Usando `data/tbl1.tsv`, obtenga los valores distintos de la columna `c4`,
conviértalos a mayúsculas y retórnelos como una lista ordenada
alfabéticamente.
Ejemplo del formato de la respuesta:
    ["A", "B", "C", "D", "E", "F", "G"]
"""

def pregunta_06():
    df = pd.read_csv(DATA_FILE, delimiter="\t")
    series = df["c4"].drop_duplicates().apply(lambda s: s.upper())
    sorted_list = series.sort_values(ascending=True).to_list()
    return sorted_list
