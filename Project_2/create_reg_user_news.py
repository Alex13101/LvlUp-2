#Создание базы данных и таблицы

import sqlite3


if __name__ == "__main__":
    con = sqlite3.connect('reg_user_news.db')

    cur = con.cursor()
    cur.execute(
        """
            CREATE TABLE reg_user_news 
            (
                telegram_id integer NOT NULL PRIMARY KEY, 
                name text,
                mail text
            )
        """
    )
    con.close()
