import math

#n = int(input("Введите целое число "))
#for i in range(0, n+1, 2):
   # print("Четные числа в диапазоне от 0 до ",n , "=", i)

#Задача 2

n = int(input("Введите целое число "))

for i in range(1,n,1):
    if n%i==0:
        print("Делители числа ",n,"= ", i)