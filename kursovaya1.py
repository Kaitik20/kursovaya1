def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


print("=== Простой калькулятор ===")
print("Доступные операции: + (сложение), - (вычитание), * (умножение)")

while True:
    try:
        x = float(input("Введите первое число: "))
        op = input("Введите операцию (+ или -): ")
        y = float(input("Введите второе число: "))

        if op == "+":
            print(f"{x} + {y} = {add(x, y)}")
        elif op == "-":
            print(f"{x} - {y} = {subtract(x, y)}")
        elif op == "*":
            print(f"{x} * {y} = {multiply(x, y)}")
        else:
            print("Неизвестная операция")

        again = input("Продолжить? (y/n): ")
        if again.lower() != "y":
            break
    except ValueError:
        print("Ошибка: введите корректное число.")