from typing import Dict, Any

contacts = {"Вася": 123, "Петя": 223}

while True:


    print("exit", "get_contact \n",
        "add_contact","print", "delete" )
    command = input("Введите команду: ")
    if command == "exit":
        break
    elif command == "get_contact":
        name = input("Введите имя абонента: ")
        if name in contacts:
            print(contacts[name])

        else:
            print('Такого контакта не существует')
    elif command == "add_contact":

        name = input("Ведите имя: ")
        phone = int(input(" Ведите телефон: "))
        contacts[name] = phone

    elif command == "print":

        print(contacts)
    elif command == "delete":
        name = input("Введите имя абонента: ")
        if name in contacts:
            print("Удалено!")
            del contacts[name]
            print(contacts)
        else:
            print('Такой записи нет')
        # Здесь нужно реализовать добавление контакта в список контактов
        ...
    else:
        print("Command dont recognized")
print(contacts)