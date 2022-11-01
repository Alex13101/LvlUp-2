def is_user_admin(login, password, users):
    for user in users:
        if user.login == login \
                and user.password == password \
                and user.mode == "admin":
            return True
    return False

def is_user_exists(login, users):
    for user in users:
        if user.login == login:
            return True
    return False

def is_login_correct(login, password, users):
    for user in users:
        if user.login == login \
                and user.password == password:
            return True
    return False


def save_users (login, password):
    with open("data.txt", "a") as f:
        if not is_login_correct(login, password):
            f.write(login, password)


def get_users():
    with open("data.txt", "r") as f:
        lines = f.readlines()
        # login password mode
        for line in lines:
            splited_line = line.split() #["login", "password", "mode"]
            login = splited_line[0]
            User(login, password, mode)

