class User:
    def __init__(self, login, password, mode="user"):
        self.login = login
        self.password = password
        self.mode = mode
    def __str__(self):
        return f'login: {self.login}, password: {self.password}, mode: {self.mode}'
admin = User("admin", "admin", "admin") # по условиям задачи пока что админ один
# 1. пользователь вводит программу
# 2. программа выбирает в зависимости от командыБ что делать (три if)
# 3
from utils import is_user_admin, is_user_exists, is_login_correct
users = [admin]

while True:
    command = input("введите команду: ")
    if command == "login":
        login = input("Введите имя пользователя: ")
        password = input("Ввведите пароль: ")
        if not is_user_exists(login, users):
            print("Пользователь не найден")
        elif not is_login_correct(login, password, users):
            print("Пароль не правильный")
        else:
            print("Ok")

    elif command == "register":
        login = input("Введите имя пользователя: ")
        if is_user_exists(login, users):
            print("Логин занят, придумайте другой!")
        else:
            password = input("Ввведите пароль: ")
            new_user = User(login, password)
            users.append(new_user)
            print("Ok")
    elif command == "all_users":
        login = input("Введите имя пользователя: ")
        password = input("Ввведите пароль: ")
        if is_user_admin(login, password, users):
            for user in users:
                print(user)
    elif command == "exit":
        break
    #else:
        #print(f"{command} не распознана")
