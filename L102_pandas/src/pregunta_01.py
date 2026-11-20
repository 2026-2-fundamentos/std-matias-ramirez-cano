from pathlib import Path
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "tbl0.tsv"

"""
¿Cuántos registros tiene la tabla `data/tbl0.tsv`? Retorne la cantidad
como un número entero.
Ejemplo del formato de la respuesta:
    40
"""

def pregunta_01():
    df = pd.read_csv(DATA_FILE, delimiter="\t")
    return int(len(df.index))
