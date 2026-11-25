from pathlib import Path
import gzip
import json
import re
import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ACTIVITY_DIR / "data" / "ventas.csv.gz"
OUTPUT_FILE = ACTIVITY_DIR / "submission" / "data_quality_report.json"

REQUIRED_COLUMNS = {"supplier_id", "supplier", "country", "city", "purchase_date",
  "amount", "discount", "weight", "units", "unit_price", "contact_email"}

EMAIL_PATTERN = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$"

def is_not_valid_email(email):
    correspondence = re.search(EMAIL_PATTERN, email)
    return correspondence is None

def is_not_valid_unit(x):
    return (x == int(x) and x >= 0) is False

def main():
    
    with gzip.open(DATA_FILE, mode="rt", encoding="utf-8") as csv_file:
        df = pd.read_csv(csv_file, keep_default_na=True)

    df = df.rename(columns=lambda s: s.strip().lower().replace(" ", "_"))

    row_count, column_count = df.shape

    missing_required_columns = sorted(list(REQUIRED_COLUMNS - set(df.columns)))

    unexpected_columns = sorted(list(set(df.columns) - REQUIRED_COLUMNS))

    duplicate_row_count = int(df.duplicated().sum())

    duplicate_supplier_id_row_count = len(df.groupby("supplier_id").filter(lambda group: len(group) > 1))

    missing_value_count_by_column = dict((col, int(df[col].isna().sum())) for col in df.columns)

    invalid_email_count = int(df["contact_email"].apply(is_not_valid_email).astype("bool").sum())

    invalid_unit_count = int(df["units"].dropna().apply(is_not_valid_unit).astype("bool").sum())

    country_values = sorted(df["country"].unique().tolist())

    report = {
        "row_count":row_count,
        "column_count":column_count,
        "missing_required_columns":missing_required_columns,
        "unexpected_columns":unexpected_columns,
        "duplicate_row_count":duplicate_row_count,
        "duplicate_supplier_id_row_count":duplicate_supplier_id_row_count,
        "missing_value_count_by_column":missing_value_count_by_column,
        "invalid_email_count":invalid_email_count,
        "invalid_unit_count":invalid_unit_count,
        "country_values":country_values
    }

    with open(OUTPUT_FILE, mode="w", encoding="utf-8") as json_file:
        json.dump(report, json_file, indent=4, ensure_ascii=False)
        
    return report


"""
Antes de limpiar o analizar un conjunto de datos, un analista debe
documentar qué problemas tiene. En este laboratorio usted no va a limpiar
"data/ventas.csv.gz": va a construir un reporte de calidad que deje evidencia
de sus problemas, tal como están en el archivo.
Lea "data/ventas.csv.gz" sin modificar sus valores. Para trabajar con los
encabezados, normalícelos: páselos a minúsculas, elimine los espacios al
inicio y al final (y cualquier marca BOM) y reemplace los espacios
internos por "_". Las columnas requeridas son "supplier_id", "supplier",
"country", "city", "purchase_date", "amount", "discount", "weight",
"units", "unit_price" y "contact_email".
Escriba el reporte en "submission/data_quality_report.json" con estas
claves:
- "row_count": cantidad de filas de datos.
- "column_count": cantidad de columnas.
- "missing_required_columns": lista ordenada de columnas requeridas que no
  están en el archivo.
- "unexpected_columns": lista ordenada de columnas del archivo que no son
  requeridas.
- "duplicate_row_count": cantidad de filas idénticas a una fila anterior.
- "duplicate_supplier_id_row_count": cantidad de filas cuyo "supplier_id"
  aparece más de una vez (cuente todas esas filas, no solo las
  repetidas).
- "missing_value_count_by_column": diccionario con la cantidad de valores
  faltantes de cada columna. Considere faltantes las celdas vacías y las
  que contienen "N/A".
- "invalid_email_count": cantidad de valores de "contact_email" que no
  tienen la forma "usuario@dominio.extension".
- "invalid_unit_count": cantidad de valores numéricos de "units" que no son
  enteros positivos. Los valores faltantes no se cuentan aquí.
- "country_values": lista ordenada de los valores distintos de "country",
  escritos exactamente como aparecen en el archivo.
La función también debe retornar el reporte como un diccionario.
Ejemplo del formato del reporte:
    {
      "row_count": 103,
      "column_count": 11,
      "missing_required_columns": [],
      ...
      "country_values": [" Colombia ", "CO", ...]
    }
"""