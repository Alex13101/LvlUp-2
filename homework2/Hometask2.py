"""Написать свой модуль калькулятор , модуль должен содержать функции
1. чтение из консоли
2. парсинг и арифметическая операция над данными
Входные данные - ЧИСЛО ЗНАК ЧИСЛО, например
5 + 6
10 / 3
6 / 0
Выходные данные - Ответ в формате
5 + 6 = 0
10 / 3 = 3.33333 # Можно округлять как удобно
6 / 0 - на ноль делить нельзя """


def read_input():
    a, c, b = input("Введите пример в формате х+у: ")
    a = int(a)
    b = int(b)
    return a, c, b


def calculate(a, c, b):
    if c == "+":
        print(f" {a} + {b} = ",  round((a+b),2))
    elif c == "-":
        print(f"{a} - {b} = ", a-b)
    elif c == "*":
        print(f"{a} * {b} = ", a*b)
    elif c == "/":
        if b == 0:
            print("На ноль делить нельзя")
        else:
            print(f"{a} / {b} = ", round((a/b),2))


a, c, b = read_input()
#print(read_input())
calculate(a, c, b)
