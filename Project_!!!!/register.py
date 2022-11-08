#Создание базы данных и таблицы

import sqlite3

def create_user(telegram_id, name, email):

#if __name__ == "__main__":
    con = sqlite3.connect('create_practice.db')
    cur = con.cursor()
    cur.execute(
        f"""
            INSERT INTO create_practice 
            ( telegram_id, name, mail)
            VALUES({telegram_id}, "{name}", "{email}");
            """

    )
    con.commit()
    con.close()
def is_user_exists(telegram_id):
    con = sqlite3.connect("create_practice.db")
    cur = con.cursor()

    res = cur.execute(
        f"""
        SELECT * FROM  create_practice WHERE telegram_id = {telegram_id};
        """

    )
    is_exists = res.fetchone() is not None
    con.close()
    return is_exists