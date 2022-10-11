def read_input():
    n = input("Ведите кол-во чисел через пробел: ").split()
    lst = []
    for i in range(len(n)):
        lst.append(int(n[i]))
    return lst
#lst=read_input()
#print(lst)
from tqdm import tqdm
def find_dividers(n):
    dividers=[]
    for i in tqdm(range(2,n)):
        if n%i==0:
            dividers.append(i)
    print(dividers)


def resolve_try_type(a,b,c):
    if a==c==b:
        return("Треугольник равноcторонний")
    elif a==b!=c or b==c!=a or b!=a==c or c!=a==b:
        return ("Треугольник равнобедренный")
    elif a!=b!=c!=a:
        return ("разносторонний")
    else:
        return ("разносторонний")