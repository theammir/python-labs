# Загальне завдання
# 1) Встановити необхідні бібліотеки (openpyxl, pandas).
# 2) Створити структури даних у Python для роботи з файлами: словники,
# списки.
# 3) Виконати завдання з JSON:
# − зчитати дані з JSON-файлу;
# − обробити дані (додати, змінити, видалити записи);
# − записати змінені дані у новий JSON-файл.
# 4) Виконати завдання з CSV:
# − зчитати дані з CSV-файлу у список або DataFrame;
# − змінити дані, додати або видалити рядки;
# − зберегти результат у новий CSV-файл.
# 5) Виконати завдання з Excel:
# − зчитати дані з Excel-файлу у DataFrame;
# − виконати обробку даних (фільтрація, сортування);
# − записати оброблені дані у новий Excel-файл.
# Індивідуальні завдання
# 9) Розробити програму для конвертації даних з формату CSV у JSON і
# збереження результату в JSON-файл.

import csv
import json
import os
import sys
from typing import Any

INPUT_PATH = "students.csv"
OUTPUT_PATH = "output.json"


def convert_types(row: dict[str, str | Any]):
    for key, value in row.items():
        try:
            if value.isnumeric():
                row[key] = int(value)
            elif value.count(".") == 1 and value.replace(".", "").isnumeric():
                row[key] = float(value)
            elif value.lower() in ["true", "false"]:
                row[key] = bool(value)
            elif value == "null":
                row[key] = None
        except Exception:
            continue
    return row


if not os.path.exists(INPUT_PATH):
    print("Input file does not exist:", INPUT_PATH)
    sys.exit(1)

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    json_str = json.dumps([convert_types(row) for row in reader], indent=4)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(json_str)
