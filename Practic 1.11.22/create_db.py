#Создание базы данных и таблицы

import sqlite3


if __name__ == "__main__":
    con = sqlite3.connect('../Practic 28.10.22/users.db')

    cur = con.cursor()
    cur.execute(
        """
            CREATE TABLE users 
            (
                telegram_id integer NOT NULL PRIMARY KEY, 
                name text,
                mail text
            )
        """
    )
    con.close()
