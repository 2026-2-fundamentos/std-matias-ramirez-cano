from pathlib import Path
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "tbl0.tsv"

"""
¿Cuántas columnas tiene la tabla `data/tbl0.tsv`? Retorne la cantidad
como un número entero.
Ejemplo del formato de la respuesta:
    4
"""

def pregunta_02():
    df = pd.read_csv(DATA_FILE, delimiter="\t")
    return int(len(df.columns))
