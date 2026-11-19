import gzip
import csv
from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

"""
Repita la pregunta 7, pero ahora cada lista de letras debe contener cada
letra una sola vez y estar ordenada alfabéticamente. Retorne una lista de
tuplas `(valor, letras)` ordenada por el valor.
Ejemplo del formato de la respuesta:
[(0, ["C"]), (1, ["B", "E"]), (2, ["A", "E"]), ...]
"""

def pregunta_08():
    register = dict()
    with gzip.open(INPUT_FILE, "rt", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        for row in csv_reader:
            num = int(row[1])
            letter = row[0]
            if num not in register:
                register[num] = set()
            register[num].add(letter)
    tuples = list((num, sorted(list(register[num]))) for num in register)
    return sorted(tuples, key=lambda t: t[0])
