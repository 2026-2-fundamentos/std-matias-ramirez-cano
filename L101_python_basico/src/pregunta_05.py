import gzip
import csv
from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

"""
Para cada letra de la primera columna (`letter`), encuentre el valor
máximo y el valor mínimo de la segunda columna (`value`). Retorne una lista
de tuplas `(letra, máximo, mínimo)` ordenada alfabéticamente por la letra.
Ejemplo del formato de la respuesta:
[("A", 9, 2), ("B", 9, 1), ...]
"""

def pregunta_05():
    register = dict()
    with gzip.open(INPUT_FILE, "rt", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        for row in csv_reader:
            letter = row[0]
            num = int(row[1])
            if letter not in register:
                register[letter] = (num, num)
            else:
                max, min = register[letter]
                if num < min:
                    register[letter] = (max, num)
                if num > max:
                    register[letter] = (num, min)
    tuples = list((letter, register[letter][0], register[letter][1]) for letter in register)
    return sorted(tuples, key=lambda t: t[0])
