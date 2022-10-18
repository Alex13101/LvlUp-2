from typing import Dict, Any

contacts = {"Вася": 123, "Петя": 223}

while True:
    command = input()
    if command == "exit":
        break
    elif command == "get_contact":
        name = input("Введите имя абонента: ")
        if name in contacts:
            print(contacts[name])

        else:
            print("Такого контакта не существует")
    elif command == "add_contact":

        name = input("Ведите имя: ")
        phone = int(input(" Ведите телефон: "))
        contacts[name] = phone

        print(name)
        # Здесь нужно реализовать добавление контакта в список контактов
        ...
    else:
        print("Command dont recognized")
print(contacts)