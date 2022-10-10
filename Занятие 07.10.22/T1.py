
"""Напишите функцию change(lst), которая
принимает список и меняет местами его первый и
последний элемент.В исходном списке минимум 2 элемента."""



def change (my_list):
    my_list[0], my_list[-1]=my_list[-1], my_list[0]
    print(my_list)

n=int(input())
my_list=[]
for i in range(n):
    number=int(input())
    my_list.append(number)
print(my_list)
change(my_list)