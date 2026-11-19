import gzip
import csv
from pathlib import Path

"""
Cuente cuántos registros hay para cada letra de la primera columna
(`letter`). Retorne una lista de tuplas `(letra, cantidad)` ordenada
alfabéticamente por la letra.
Ejemplo del formato de la respuesta:
    [("A", 8), ("B", 7), ("C", 5), ...]
"""

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

def pregunta_02():
    counts = dict()
    with gzip.open(INPUT_FILE, "rt", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        for row in csv_reader:
            letter = row[0]
            if letter not in counts:
                counts[letter] = 0
            counts[letter] += 1
    tuples = list((letter, counts[letter]) for letter in counts)
    return sorted(tuples, key=lambda t: t[0])
