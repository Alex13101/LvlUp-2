"""Напишите программу, которая будет запрашивать у пользователя числа,
пока он не пропустит ввод. Сначала на экран должно быть выведено
среднее значение введенного ряда чисел, после этого друг за другом не-
обходимо вывести список чисел ниже среднего, равных ему (если такие
найдутся) и выше среднего. Каждый список должен предваряться соот-
ветствующим заголовкоm"""
# from utils import read_input
# my_list=read_input()
# print(my_list)

def read_input():
    n = int(input("введите число"))
    my_list = []
    for i in range(n):
      number = int(input())
      my_list.append(number)
    return my_list
if __name__ == "__main__":
    my_list = read_input()
    import statistics
    mean_number = statistics.mean(my_list)
    print("Среднее значение", mean_number)

    for i in my_list:
        if i >= mean_number:
            print("Выше среднего", i)
        elif i < mean_number:
            print("Ниже среднего", i)