

# n = int(input(" число строк"))
# b = set()
# t = {}
# for i in range(n):
#     b.update(input("Введи строку :").split())
#     if i in b:
#         t = t + b[i]
#
# # for i in range(n):
# #     if b[i] == b[i+1]:
# #         t +=b[i]
# print(len(t))
#



#Метод 1.

import random
def generate_random_list(n):
    l=[]
    for i in range(n):
        l.append((random.randint(1,1000)))

# Метод 2.

def is_sublist(a, b):
    # является ли b подсписком a
   for i in b:
       if i not in a:
           return False
list1 = generate_random_list(1000000)
list2 = list1[:-1]
start = datetime.now()
print(is_sublist(list1, list2))
print(datetime.now() - start)


