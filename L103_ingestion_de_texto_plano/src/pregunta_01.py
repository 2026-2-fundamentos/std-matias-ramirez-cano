from pathlib import Path
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "clusters_report.txt"

"""
El archivo `data/clusters_report.txt` es un reporte de clústeres de
palabras clave pensado para ser leído por una persona, no por un programa:
los encabezados ocupan varias líneas, las columnas están alineadas con
espacios y la lista de palabras clave de un clúster continúa en las líneas
siguientes.
Su tarea es convertir ese reporte en un DataFrame de Pandas con una fila
por clúster y las columnas:
- `cluster`: número del clúster, como entero.
- `cantidad_de_palabras_clave`: como entero.
- `porcentaje_de_palabras_clave`: como número decimal; por ejemplo, el
  texto `15,9 %` debe quedar como `15.9`.
- `principales_palabras_clave`: todas las palabras clave del clúster en un
  solo texto, separadas por una coma y un único espacio.
Retorne el DataFrame.
Ejemplo del formato de la respuesta (se omite la última columna):
       cluster  cantidad_de_palabras_clave  porcentaje_de_palabras_clave
    0        1                         105                          15.9
    1        2                         102                          15.4
    ...
"""

def hack(s):
    if s == "":
        return "EMPTY"
    else:
        return " ".join(s.split())

def pregunta_01():
    
    column_names = [
        "cluster", 
        "cantidad_de_palabras_clave", 
        "porcentaje_de_palabras_clave", 
        "principales_palabras_clave"
        ]
    clean_data = list()
    
    content_str = None
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content_str = f.read()

    content_list = content_str.split("\n")
    content_list = content_list[4:-2]
    content_list = list(map(lambda s: hack(s.strip()), content_list))
    content_list = " ".join(content_list).split(" EMPTY ")

    for line in content_list:
        entries = line.split()
        cluster = entries[0]
        cantidad = entries[1]
        porcentaje = entries[2].replace(",", ".")
        palabras = " ".join(entries[4:]).removesuffix(".")
        row = [cluster, cantidad, porcentaje, palabras]
        clean_data.append(row)

    df = pd.DataFrame(clean_data, columns=column_names)
    df["cluster"] = df["cluster"].astype("int32")
    df["cantidad_de_palabras_clave"] = df["cantidad_de_palabras_clave"].astype("int32")
    df["porcentaje_de_palabras_clave"] = df["porcentaje_de_palabras_clave"].astype("float32")
    df["principales_palabras_clave"] = df["principales_palabras_clave"].astype("string")

    return df
