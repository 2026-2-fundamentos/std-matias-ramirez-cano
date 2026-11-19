import gzip
import csv
from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "data.csv.gz"

"""
La quinta columna (`metrics`) contiene pares `clave:valor` separados por
comas. Para cada clave, encuentre el valor mínimo y el valor máximo que
aparecen en todo el archivo. Retorne una lista de tuplas
`(clave, mínimo, máximo)` ordenada alfabéticamente por la clave.
Observe que el orden es mínimo y luego máximo, al contrario de la
pregunta 5.
Ejemplo del formato de la respuesta:
[("aaa", 1, 9), ("bbb", 1, 9), ...]
"""

def pregunta_06():
    register = dict()
    with gzip.open(INPUT_FILE, "rt", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        for row in csv_reader:
            metrics = row[4].split(",")
            pairs = map(lambda str: str.split(":"), metrics)
            for pair in pairs:
                key = pair[0]
                num = int(pair[1])
                if key not in register:
                    register[key] = (num, num)
                else:
                    min, max = register[key]
                    if num < min:
                        register[key] = (num, max)
                    if num > max:
                        register[key] = (min, num)
    tuples = list((key, register[key][0], register[key][1]) for key in register)
    return sorted(tuples, key=lambda t: t[0])
