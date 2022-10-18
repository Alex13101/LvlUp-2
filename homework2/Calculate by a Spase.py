def read_input():
    n = input("Ведите Ваш пример через пробел: ").split()
    lst = []
    for i in range(len(n)):
        lst.append(n[i])
    a = int(lst[0])
    c = lst[1]
    b = int(lst[2])
    #print(a, c, b)
    return a, c, b


def calculate(a, c, b):
    if c == "+":
        print(f" {a} + {b} = ", round((a + b), 2))
    elif c == "-":
        print(f"{a} - {b} = ", a - b)
    elif c == "*":
        print(f"{a} * {b} = ", a * b)
    elif c == "/":
        if b == 0:
            print("На ноль делить нельзя")
        else:
            print(f"{a} / {b} = ", round((a / b), 2))
    else:
        print("Такой операции нет")

a, c, b = read_input()
calculate(a, c, b)
