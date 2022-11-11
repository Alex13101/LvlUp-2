import telebot
# Импортируем функции создания и проверки пользователя
from register import is_user_exists, create_user
from utills import is_email_valid #Импортируем функцию проверки правильности введенной почты
from utills import getwiki # Импортируем функцию для Википедии


# Создаем экземпляр бота
bot = telebot.TeleBot('5766012834:AAHgsslpBBbumdkKCZ_b5X0HsJwc5FBsrH4') #Токен от bot_father

@bot.message_handler(commands=['help'])
def register(message):
    bot.send_message(message.chat.id, 'Я умею: /start /search')

@bot.message_handler(commands=['start'])
def register(message):
    user_id = message.chat.id
    if is_user_exists(user_id):
        bot.send_message(user_id, 'Ты уже регистрировался! \nОтправьте мне любое слово, и я \nнайду его значение на Wikipedia')
        @bot.message_handler(commands=["searh"])
        def search(m, res=False):
            bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
            # Получение сообщений от юзера
        @bot.message_handler(content_types=["text"])
        def handle_text(message):
            bot.send_message(message.chat.id, getwiki(message.text))
            # Запускаем бота
    else:
        bot.send_message(message.chat.id, 'Введи пожалуйста свое имя и фамилию')
        bot.register_next_step_handler(message, read_name)

def read_name(message):
    name = message.text
    bot.send_message(message.chat.id, f"Введи пожалуйста свою почту")
    bot.register_next_step_handler(message, read_email, name)



def read_email(message, name):
    email = message.text
    if is_email_valid(email):
        bot.send_message(message.chat.id, f'Спасибо за регистрацию! \nОтправьте мне любое слово, и я найду его значение на Wikipedia ')
        create_user(message.chat.id, name, email)
        @bot.message_handler(commands=["searh"])
        def search(m, res=False):
            bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я \nнайду его значение на Wikipedia')
            # Получение сообщений от юзера
        @bot.message_handler(content_types=["text"])
        def handle_text(message):
            bot.send_message(message.chat.id, getwiki(message.text))
    else:
        bot.send_message(message.chat.id, f"Некорректная почта! Нажми /start")

# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов


# Запускаем бота
bot.polling(none_stop=True, interval=0)
