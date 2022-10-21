import json


qwest1 = input("Вопрос 5+6 :") #11
qwest2 = input("Вопрос 11-5 :") # Тут
qwest3 = input("Вопрос 3*3 :")  # Так

x = { "q1":qwest1, "q2":qwest2, "q3":qwest3 }



with open ("json_practic.json", "w", encoding="utf8") as json_file:
    json.dump(x, json_file)
    print(x)

import json

with open("json_practic.json", encoding="utf8") as json_file:
    d = json.load(json_file)
    print(d)
tot = 0
if d["q1"] == "11":
    tot +=1
if d["q2"] == "6":
    tot +=1
if d["q3"] =="9":
    tot +=1
print(tot)
if tot == 3:
    print("Оценка отлично!")

