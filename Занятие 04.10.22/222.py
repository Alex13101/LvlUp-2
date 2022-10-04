def read_input ():
    n = int(input())
    my_list = []
    for i in range(n):
        number = int(input())
        my_list.append(number)
    return my_list
my_list=read_input()
for i in my_list:
        print(i*i)
