import gzip
import csv
from pathlib import Path
from collections import OrderedDict

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

"""
Cuente cuántas veces aparece cada clave en la quinta columna (`metrics`)
de todo el archivo. Retorne un diccionario `{clave: cantidad}` con las
claves en orden alfabético.
Ejemplo del formato de la respuesta:
{"aaa": 13, "bbb": 16, "ccc": 23, ...}
"""

def pregunta_09():
    unique_keys = list()
    register = dict()
    with gzip.open(INPUT_FILE, "rt", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        for row in csv_reader:
            metrics = row[4].split(",")
            keys = map(lambda str: str.split(":")[0], metrics)
            for key in keys:
                if key not in register:
                    unique_keys.append(key)
                    register[key] = 0
                register[key] += 1
    unique_keys.sort()
    ordered_register = OrderedDict((key, register[key]) for key in unique_keys)
    return ordered_register
