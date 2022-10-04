"""На вход программы поступает н чисел
Выведите их сумму
Пример ввода
3
5
6
7

"""
n=int(input())
my_list=[]
for i in range(n):
    number=int(input())
    my_list.append(number)
print([my_list])
