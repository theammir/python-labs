# Загальне завдання
# Написати програму, яка:
# − зчитує два числа з клавіатури;
# − виконує операції додавання, віднімання, множення та ділення;
# − виводить результати обчислень на екран.
# Індивідуальні завдання
# 9) Програма для перевірки, чи є одне число дільником іншого.

a = float(input("Enter a: "))
b = float(input("Enter b: "))
print()
print(f"{a + b = }")
print(f"{a - b = }")
print(f"{a * b = }")
print(f"{a / b = }" if b != 0 else "a / b = undefined")

if b != 0 and a % b == 0:
    print("a is divisible by b")
else:
    print("a is not divisible by b")

if a != 0 and b % a == 0:
    print("b is divisible by a")
else:
    print("b is not divisible by a")
