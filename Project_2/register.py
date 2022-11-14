# Создание базы данных и таблицы

import sqlite3
from typing import List, Any


def create_user(telegram_id, name, email):
    # if __name__ == "__main__":
    con = sqlite3.connect('reg_user_news.db')
    cur = con.cursor()
    cur.execute(
        f"""
            INSERT INTO reg_user_news 
            ( telegram_id, name, mail)
            VALUES({telegram_id}, "{name}", "{email}");
            """

    )
    con.commit()
    con.close()


def is_user_exists(telegram_id):
    con = sqlite3.connect("reg_user_news.db")
    cur = con.cursor()

    res = cur.execute(
        f"""
        SELECT * FROM  reg_user_news WHERE telegram_id = {telegram_id};
        """

    )
    is_exists = res.fetchone() is not None
    con.close()
    return is_exists












# def is_user_all():
#     con = sqlite3.connect('create_practice.db')
#     cur = con.cursor()
#     res = cur.execute(
#         f"""SELECT * FROM create_practice ;
#         """
#     )
#
#     #is_all = {}
#     while True:
#         is_all = res.fetchall()
#         if is_all in res.fetchone():
#             print(is_all)
#             is_all.append(is_all)
#
#         else:
#             break
#
#         #is_all: {} =  #is not None



        con.close()
        

    return is





