import gzip
import csv
from pathlib import Path

"""
Cuente cuántos registros hay en cada mes, usando la fecha de la tercera
columna (`date`). Represente el mes como un texto de dos dígitos y retorne
una lista de tuplas `(mes, cantidad)` ordenada por el mes.
Ejemplo del formato de la respuesta:
[("01", 3), ("02", 4), ("03", 2), ...]
"""

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

def pregunta_04():
    counts = dict()
    with gzip.open(INPUT_FILE, "rt", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        for row in csv_reader:
            date = row[2]
            month = date[5:7]
            if month not in counts:
                counts[month] = 0
            counts[month] += 1
    tuples = list((month, counts[month]) for month in counts)
    return sorted(tuples, key=lambda t: t[0])
