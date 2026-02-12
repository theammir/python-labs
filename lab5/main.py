# Загальне завдання
# Написати програму, яка зчитує дані з текстового файлу та записує їх у новий
# файл, виконуючи певні перетворення (наприклад, переведення всіх літер у
# нижній регістр).
# Індивідуальні завдання
# 9) Видалити всі порожні рядки з файлу.

import os
import sys

INPUT_PATH = "input.txt"
OUTPUT_PATH = "output.txt"

if not os.path.exists(INPUT_PATH):
    print("The file does not exist:", INPUT_PATH)
    sys.exit(1)

output = open(OUTPUT_PATH, "w", encoding="utf-8")
with open(INPUT_PATH, "r", encoding="utf-8") as f:
    content = f.readlines()
    output.writelines([line for line in content if line.strip() != ""])
output.close()
