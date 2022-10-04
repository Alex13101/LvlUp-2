"""n = int(input())
my_list = []
for i in range(n):
    number = int(input())
    my_list.append(number)

for i in my_list:
    print(i*i)"""
a = [int(input()) for i in range(int(input()))]
q = []
even = []
#a = [int(x) for x in input().split()]
for i in range(len(a)):
    t = a[i]
    q.append(t*t)
    if t%2 ==0:
        even.append(t)
print(q, even, sep = '\n')
   #print("Четные числа  ",n , "=", i)
