def read_input():
    a = int(input("введите сумму "))
    b = int(input("Введите срок  "))
    c=float(input("Введите процент "))
    return a,b,c

def operations(a,b,c):
    d=a*c*b
    print("Ваша сумма через ",b,"лет будет ", d)

a,b,c=read_input()
operations(a,b,c)