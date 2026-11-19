import gzip
import csv
from pathlib import Path
from collections import OrderedDict

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

"""
Para cada letra de la primera columna (`letter`), sume todos los valores
numéricos de los pares `clave:valor` de la quinta columna (`metrics`).
Retorne un diccionario `{letra: suma}` con las letras en orden alfabético.
Ejemplo del formato de la respuesta:
{"A": 177, "B": 187, "C": 114, ...}
"""

def pregunta_12():
    unique_keys = list()
    register = dict()
    with gzip.open(INPUT_FILE, "rt", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        for row in csv_reader:
            letter = row[0]
            metrics = row[4].split(",")
            values = map(lambda str: int(str.split(":")[1]), metrics)
            if letter not in register:
                unique_keys.append(letter)
                register[letter] = 0
            for value in values:
                register[letter] += value
    unique_keys.sort()
    ordered_register = OrderedDict((key, register[key]) for key in unique_keys)
    return ordered_register
