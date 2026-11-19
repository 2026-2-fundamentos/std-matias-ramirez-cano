import gzip
import csv
from pathlib import Path
from collections import OrderedDict

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

"""
La cuarta columna (`codes`) contiene letras minúsculas separadas por
comas. Para cada una de esas letras, sume los valores de la segunda
columna (`value`) de los registros en los que aparece. Retorne un
diccionario `{letra: suma}` con las letras en orden alfabético.
Ejemplo del formato de la respuesta:
{"a": 122, "b": 49, "c": 91, ...}
"""

def pregunta_11():
    unique_keys = list()
    register = dict()
    with gzip.open(INPUT_FILE, "rt", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        for row in csv_reader:
            codes = row[3].split(",")
            value = int(row[1])
            for code in codes:
                if code not in register:
                    unique_keys.append(code)
                    register[code] = 0
                register[code] += value
    unique_keys.sort()
    ordered_register = OrderedDict((key, register[key]) for key in unique_keys)
    return ordered_register
