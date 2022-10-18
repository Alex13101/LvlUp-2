"""Если помните, на старых мобильных телефонах текстовые сообщения набирались
при помощи цифровых кнопок. Однократное нажатие приводило к появлению первой
буквы в соответствующем этой кнопке списке, последующие нажатия меняли ее на
следующую. Список символов, ассоциированных с цифровой панелью, приведен в
таблице

Кнопка	Символы
1	. , ? ! :
2	A B C
3	D E F
4	G H I
5	J K L
6	M N O
7	P Q R S
8	T U V
9	W X Y Z
0	Пробел
Входные данные

2 8
1 2
3 4
Вывести:

UAI"""

phone_number = {
1: [".", ",", "?", "!", ':']
2: ["A", "B",  "C"]
3: ["D", "E", "F"]
4: ["G", "H", "I"]
5: ["J", "K", "L"]
6: ["M", "N", "O"]
7: ["P", "Q", "R", "S"]
8: ["T", "U", "V"]
9: ["W", "X", "Y", "Z"]
0: [" "]
}
#n -= 1 уменьшаем на 1
    #a = ["G", "H", "I"]
    #l = len(a) + 1 = 4
    #1 % l




def get_button_symbol(button_n, n):
    letters = phone_buttons[button_n]
    n -= 1
    l = len(letters)
    return letters[n % l]
