import gzip
import csv
from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

"""
Para cada registro del archivo, en el mismo orden en que aparecen,
retorne una tupla con la letra de la primera columna (`letter`), la
cantidad de elementos de la cuarta columna (`codes`) y la cantidad de
pares de la quinta columna (`metrics`). El resultado es una lista con una
tupla por registro.
Ejemplo del formato de la respuesta:
[("E", 3, 5), ("A", 3, 4), ("B", 4, 4), ...]
"""

def pregunta_10():
    tuples = list()
    with gzip.open(INPUT_FILE, "rt", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        for row in csv_reader:
            letter = row[0]
            codes = len(row[3].split(","))
            metrics = len(row[4].split(","))
            tuples.append((letter, codes, metrics))
    return tuples
