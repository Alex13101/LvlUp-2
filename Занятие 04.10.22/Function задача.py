def read_input ():
    a=int(input())
    b=int(input())
    c=input()
    return a,b,c

def calculate (a,b,c):

    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="*":
        print(a*b)
    elif c=="/":
        if b==0:
            print("На ноль делить нельзя")
        else:
            print(a / b)
a,b,c=read_input()
calculate(a,b,c)



my_list=read_input()
my_list2=read_input()