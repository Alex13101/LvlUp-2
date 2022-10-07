text=input("Введите строку :")
print("Original String : " + text)
num = 0
num_list=[]
for c in text:
    if c.isdigit():
        num += int(c)
        num_list.append(c)
print(num)
if text.count("-")>0 and int(num):
    print("Число отрицательное")
elif num>0:
    print("Число положительное")
elif num==0:
    print("Число равно 0")
print("извлеченные цифры : ", num_list)