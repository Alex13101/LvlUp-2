# d = frozenset([1, 2, 3, ])
# my_d = {d: "my_frozen_set"}
# print(my_d)



names = {"Тван", "Петр", "Вася"}
moneys = [1000, 1500, 1000]
shames = ["Петров", "Petrov", "uhrkjfej"]

for name, money in zip(names, moneys):
    print(f"Баланс пользователя {names} = {moneys}")

