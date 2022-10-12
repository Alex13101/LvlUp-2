"""Написать программу, считывающую список чисел и выводящую:
!Дополнительно: Реализовать функцию для поиска среднего арифметического,
 принимающую на вход список и возвращающую число:

def mean(my_list):
    # тут код
    return mean_number
a. минимальное число (подсказка)
б. максимальное число (подсказка)
в. среднее арифметическое чисел из списка (подсказка)
г. отсортированный список (подсказка)"""

from utils import read_input

my_list = read_input()
print(my_list)


def arithmetic_mean():
    mean_lst = []
    a = 0

    for i in range(len(my_list)):
        a = a + my_list[i]
    mean_number = a / len(my_list)
    print("Сумма чисел = ", a)
    print("Среднеарифметич ==:", mean_number)
    return mean_number

c=arithmetic_mean()


print("Среднеарифметич ==:", c)
print("Минимальный = ", min(my_list))
print("Максимальный = ", max(my_list))
