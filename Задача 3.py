a=int(input("Введите целое число 1 "))
b=int(input("Введите целое число 2 "))
c=int(input("Введите целое число 3 "))
if a<=b<=c:
    print(a,b,c)
elif b<=c<=a:
    print(b,c,a)
elif c<=a<=b:
    print(c,a,b)
elif b<=a<=c:
    print(b,a,c)


