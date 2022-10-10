"""Дан список, упорядоченный по неубыванию элементов в
нем. Определите, сколько в нем различных элементов."""




# n=input("Ведите кол-во чисел через пробел: ").split()
# lst=[]
# for i in range (len(n)):
#     lst.append(int(n[i]))
#     lst.count(i)

from utils import read_input
lst=read_input()
lst.sort()
print(lst)
a=0
saw=[]
for i in lst:
    if i not in saw:
        a+=1
        saw.append(i)
print(a)
for i in saw:
    print(f"Элемент {i} встречается {lst.count(i)} раз")







#     print(lst.count(i))
#     if lst.count(i)==1:
#         a+=1
#         print(i,"Встречается один раз")
#     elif lst.count(i)>1:
#         print(i,"Встречается много раз")
# print(a,"уникальных элементов")
