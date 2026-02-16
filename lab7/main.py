# Загальне завдання
# Розробити програму, яка виконує дії, згідно індивідуального варіанту.
# Передбачити можливість виникнення та реалізувати коректну обробку винятків.
# Інформацію про виникнення винятків необхідно виводити на екран та зберігати
# у логфайл.
# Індивідуальні завдання
# 9) Створити програму, яка зчитує дані з файлу та перевіряє їх відповідність
# заданому формату.
import sys

# INPUT_PATH = "input.txt"
INPUT_PATH = "input_nonexistent.txt"

content: str
try:
    f = open(INPUT_PATH, "r", encoding="utf-8")
    content = f.read().strip()
except IOError as e:
    print("OS error occured while reading the file:", e)
    sys.exit(1)
except Exception as e:
    print(f"Unknown error occured: {e.__class__.__name__}: {e}")
    sys.exit(1)

if content.isnumeric():
    print("The file only contains a number.")
else:
    print("The file does not only contain a number.")
