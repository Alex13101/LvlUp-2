word=input("Ведите что-нибудь:")
D={}
a=" "
for i in word:
    a= word.count(i)
    print(" Значение ",i," встречается", a, "раз" )
    if i not in (D):
        D[i]=a
print(D)
for i,v in D.items():
    print(f"Значение {i} встречаетс {v} раз")
