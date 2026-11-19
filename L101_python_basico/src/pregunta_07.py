import gzip
import csv
from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

"""
Para cada valor distinto de la segunda columna (`value`), construya la
lista de letras de la primera columna (`letter`) que aparecen con ese
valor. Conserve las letras repetidas y el orden en que aparecen en el
archivo. Retorne una lista de tuplas `(valor, letras)` ordenada por el
valor.
Ejemplo del formato de la respuesta:
[(0, ["C"]), (1, ["E", "B", "E"]), (2, ["A", "E"]), ...]
"""

def pregunta_07():
    register = dict()
    with gzip.open(INPUT_FILE, "rt", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        for row in csv_reader:
            num = int(row[1])
            letter = row[0]
            if num not in register:
                register[num] = list()
            register[num].append(letter)
    tuples = list((num, register[num]) for num in register)
    return sorted(tuples, key=lambda t: t[0])
