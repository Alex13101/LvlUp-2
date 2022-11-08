import sqlite3


if __name__ == "__main__":
    con = sqlite3.connect('create_practice.db')

    cur = con.cursor()
    cur.execute(
        f"""
            CREATE TABLE create_practice
            (
                telegram_id integer NOT NULL PRIMARY KEY, 
                name text,
                mail text
            )
        """
    )
    con.close()
