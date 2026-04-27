def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b


print("=== Простой калькулятор v2 ===")
print("Доступные операции: + (сложение), - (вычитание), / (деление)")

while True:
    try:
        x = float(input("Введите первое число: "))
        op = input("Введите операцию (+ или -): ")
        y = float(input("Введите второе число: "))

        if op == "+":
            print("Результат:", add(x, y))
        elif op == "-":
            print("Результат:", subtract(x, y))
        elif op == "/":
            print("Результат:", divide(x, y))
        else:
            print("Неизвестная операция")

        again = input("Продолжить? (y/n): ")
        if again.lower() != "y":
            break
    except ValueError:
        print("Ошибка: введите корректное число.")