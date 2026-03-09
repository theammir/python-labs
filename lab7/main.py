# Загальне завдання
# Розробити програму, яка виконує дії, згідно індивідуального варіанту.
# Передбачити можливість виникнення та реалізувати коректну обробку винятків.
# Інформацію про виникнення винятків необхідно виводити на екран та зберігати
# у логфайл.
# Індивідуальні завдання
# 9) Створити програму, яка зчитує дані з файлу та перевіряє їх відповідність
# заданому формату.

import sys
from typing import Iterable, TextIO

# INPUT_PATH = "input_nonexistent.txt"
INPUT_PATH = "input.txt"
LOG_FILE = open("error.log", "w")


def log(line: str, streams: Iterable[TextIO] = (LOG_FILE, sys.stdout)) -> None:
    for stream in streams:
        stream.write(line + "\n")


content: str
try:
    f = open(INPUT_PATH, "r", encoding="utf-8")
    content = f.read().strip()
except IOError as e:
    log(f"OS error occured while reading the file: {e}")
    sys.exit(1)
except Exception as e:
    log(f"Unknown error occured: {e.__class__.__name__}: {e}")
    sys.exit(1)

for line in content.splitlines():
    error = False
    name, age = line.split(":", 2)
    if not name or not age:
        error = True
    if not name.isalpha() or not age.isnumeric():
        error = True

    if error:
        print("Помилка нижче:")
    print(name)
