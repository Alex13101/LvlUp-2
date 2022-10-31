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