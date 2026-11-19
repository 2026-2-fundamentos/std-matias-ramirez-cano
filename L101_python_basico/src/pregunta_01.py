import gzip
import csv
from pathlib import Path

"""
Calcule la suma de los valores de la segunda columna (`value`) del
archivo `data/data.csv.gz` y retorne el resultado como un número entero.
Ejemplo del formato de la respuesta: 214 
"""

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

def pregunta_01():
    sum = 0
    with gzip.open(INPUT_FILE, "rt", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        for row in csv_reader:
            sum += int(row[1])
    return sum
