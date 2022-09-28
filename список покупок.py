# Это мой список покупок
shopList = ['яблоки ', ' манго ', ' морковь ', ' бананы']
print(' Я должен сделать ', len(shopList), 'покупки.')
print('Покупки: ', end='')
for item in shopList:
    print(item, end='')

adding = int(input("\nХотите добавить\удалить покупку? Добавить - 1, Удалить - 2:"))
while adding == 1:  # Начинаем цикл
    shopList.append(input("Введите что нужно купить:"))
    adding = int(input("Хотите продолжить? Удалить- 2, Добавить-1:"))
else:
    print()

# while adding==2:


print(' Теперь мой список покупок таков:', shopList)

print('\nТакже нужно купить риса.')

print(' Отсортирую-ка я свой список')
shopList.sort()
print('Отсортированный список покупок выглядит так:', shopList)

print('Первое, что мне нужно купить, это ', shopList[0])
olditem = shopList[int(input("Введите позицию, которую купили:"))]
del shopList[olditem]
print(' Я купил', olditem)
print(' Теперь мой список покупок:', shopList)1