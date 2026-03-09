# 9.7 Загальне завдання
# Написати програму, яка:
# − вводить початкові дані (з файлу або з клавіатури);
# − формує результат з використанням регулярних виразів;
# − виводить результат на екран або зберігає у файл.
# Індивідуальні завдання
# 9) Створити програму для перевірки, чи є рядок валідною IP-адресою.

import re

# I wrote it myself: https://regex101.com/r/wCN9LB/1
# Didn't give it *too* much thought, but it should correctly check
# that octets are within 0-255, and there are no redundant zeroes
IPV4_PATTERN = re.compile(
    r"^((([0-9]|[1-9][0-9])|([1-2][0-4][0-9])|(25[0-5]))\.){3}(([0-9]|[1-9][0-9])|([1-2][0-4][0-9])|(25[0-5]))$"
)

if re.match(IPV4_PATTERN, input("Enter an IPv4 address: ").strip()):
    print("This is a valid IPv4 address. (True)")
else:
    print("This is NOT a valid IPv4 address. (False)")
