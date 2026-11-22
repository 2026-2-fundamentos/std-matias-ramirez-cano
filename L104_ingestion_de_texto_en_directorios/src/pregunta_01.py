from pathlib import Path
import csv

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_DIR_A = ACTIVITY_DIR / "data" / "train"
INPUT_DIR_B = ACTIVITY_DIR / "data" / "test"
OUTPUT_FILE_A = ACTIVITY_DIR / "submission" / "train_dataset.csv"
OUTPUT_FILE_B = ACTIVITY_DIR / "submission" / "test_dataset.csv"

"""
Las frases de este laboratorio no están en una tabla, sino en miles de
archivos de texto organizados en carpetas. Dentro de `data/` hay dos
carpetas, `train/` y `test/`, y cada una contiene las carpetas
`negative/`, `neutral/` y `positive/`. Cada archivo `.txt` contiene una
frase, y la carpeta donde se encuentra indica su sentimiento.
Su tarea es construir un dataset para cada división y guardarlo en:
- `submission/train_dataset.csv`
- `submission/test_dataset.csv`
Cada archivo debe tener dos columnas: `phrase`, con el texto de la frase,
y `target`, con el nombre de la carpeta de sentimiento (`negative`,
`neutral` o `positive`). Recorra las carpetas y los archivos en orden
alfabético, de modo que el resultado sea siempre el mismo. No guarde el
índice de Pandas en el CSV.
Ejemplo del formato de cada archivo:
    phrase,target
    "The real estate company posted a net loss ...",negative
    ...
    "Cardona slowed her vehicle , turned around ...",neutral
    ...
"""

def pregunta_01():
    dicc = {INPUT_DIR_A:OUTPUT_FILE_A, INPUT_DIR_B:OUTPUT_FILE_B}
    for input_dir in dicc:
        data = list()
        data.append(["phrase", "target"])
        directories = list()
        for dir in input_dir.iterdir():
            directories.append(dir)
        directories.sort(key=lambda dir: dir.name)
        for dir in directories:
            dir_name = dir.name
            text_files = list()
            for file in dir.iterdir():
                text_files.append(file)
            text_files.sort(key=lambda file: file.stem)
            for file in text_files:
                phrase = file.read_text(encoding="utf-8").strip()
                data.append([phrase, dir_name])
        with open(dicc[input_dir], "w", encoding="utf-8", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(data)
