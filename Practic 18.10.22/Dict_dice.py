
"""В данном упражнении мы будем симулировать 1000
выбрасываний игральных костей. Начнем с написания
функции, выполняющей случайное выбрасывание двух обычных шестигранных костей. Эта функция не будет принимать входных параметров, а возвращать должна число, выпавшее в сумме на двух костях. В основной программе реализуйте симуляцию тысячи выбрасываний костей. Программа должна хранить все результаты с частотой их выпадения. После завершения процесса должна быть показана итоговая таблица с результатами. Выразите частоту выпадения каждого из чисел в процентах.

Дополнительно: Так же вывести ожидаемый результатат
согласно теории вероятностей.
Вывод должен выглядеть так

Результат	Результат симуляции
2	3.1
3	6.7
4	9.1
5	10.4
6	14.2
7	15.1
8	13.2
9	11.2
10	10.4
11	6.7
12	3.1
Мобильное сообщение
Если помните, на старых мобильных телефонах текстовые
сообщения набирались при помощи цифровых кнопок.
Однократное нажатие приводило к появлению первой буквы
в соответствующем этой кнопке списке, последующие
нажатия меняли ее на следующую. Список символов,
ассоциированных с цифровой панелью, приведен
в таблице"""

import random


def dice():
    result = random.randint(1, 6)
    result_2 = random.randint(1, 6)
    total = result + result_2
    #print(result, "+", result_2, "=", total)
    return (total)


d = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
finish = {}
# print(result_2)
for i in range(1000):
    z = dice()
    d[z] = d[z] + 1

y=0

for i,v in d.items(): #Идем в цикле по ключам и значениям
    d[i]=v/1000*100
print("Результат \t Результат симуляции")
for i,v in d.items():
    print(f" {i}            {v:.2f}")  #Округление до 2-х знаков
    y+=d[i]                                 # после запятой
print(f"Всего {y}  %")