from email_validator import validate_email, EmailNotValidError
import sqlite3
# def get_news(s):
#     news_text2 = s
#         # Возвращаем текстовую строку
#     return news_text2

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

def is_email_valid(email):
    try:
        email = validate_email(email).email
        return True
    except EmailNotValidError as e:
        return False
