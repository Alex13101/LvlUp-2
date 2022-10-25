"""В известной игре Эрудит (Scrabble™) каждой букве соответствует
определенное количество очков. Общая сумма очков, которую получает
игрок, составивший это слово, складывается из очков за каждую
букву, входящую в его состав. Чем более употребимой является
буква в языке, тем меньше очков начисляется за ее
использование. В таблице приведены все соответствия букв и
очков из английской версии игры

Очки	Буквы
1	A, E, I, L, N, O, R, S, T и U
2	D и G
3	B, C, M и P
4	F, H, V, W и Y
5	K
8	J и X
10	Q и Z
Входные данные:

Python
Вывести:

10"""
zh = {
list_1: ["A", "E", "I", "l", "n", "o", "r", "s", "t", "u"],
list_2:  ["d", "g"],
list_3: ["b", "c", "m", "p"],
list_4: ["f", "h", "v", "w", "y"],
list_5: ["k"],
list_8: ["j", "x"],
list_10: ["q","z"]}

word = [python]
x = len(word)

print(x)