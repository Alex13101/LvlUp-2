import telebot
# Импортируем функции создания и проверки пользователя
from utils_for_proba import is_user_exists, create_user
from utils_for_proba import is_email_valid  # Импортируем функцию проверки правильности введенной почты
import time

# Создаем экземпляр бота
bot = telebot.TeleBot('5766012834:AAHgsslpBBbumdkKCZ_b5X0HsJwc5FBsrH4')  # Токен от bot_father
chanel_name = '@project_chanel'  # Имя кнала Телеграмм куда будем транслировать новости.


@bot.message_handler(commands=['help'])
def register(message):
    bot.send_message(message.chat.id, 'Нажмите : /start /search')


# commands = ['start']


@bot.message_handler(commands=['start'])
def register(message):
    bot.send_message(chanel_name, 'Можете предложить свою новость\n Для этого напишите мне - @Levelraund1_bot')
    user_id = message.chat.id
    if is_user_exists(user_id):
        bot.send_message(user_id, 'Ты уже регистрировался! \nПредложите свою новость и я опубликую ее в канале.')

        # @bot.message_handler(commands=["searh"])
        # def search(m, res=False):
        #     bot.send_message(user_id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
        # Получение сообщений от юзера
        @bot.message_handler(content_types=["text", "audio", "video"])
        def handle_text(message):
            bot.send_message(message.chat.id, 'Вы предложили новость в канал: ' + message.text)
            bot.send_message(chanel_name, f'от пользователя {user_id} :  ' + message.text)
            # accepted_text = message
            # with open("pork.txt", "a") as f:
            #     f.write(accepted_text)

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
            bot.send_message(message.chat.id,
                                f'Спасибо за регистрацию! \nМожете предложить свою новость и я опубликую ее в канале. ')
            create_user(message.chat.id, name, email)

            @bot.message_handler(content_types=["text", "audio", "video"])
            def handle_text(message):
                user_id = message.chat.id
                bot.send_message(message.chat.id, 'Вы предложили новость в канал: ' + message.text)
                bot.send_message(chanel_name, f'от пользователя {user_id} : ' + message.text)
        else:
            bot.send_message(message.chat.id, f"Некорректная почта! Нажми /start")


# is_all = []
#
#
# @bot.message_handler(commands=['all_users'])
# def all_users(message):
#     # user_id = message.chat.id
#     if is_user_all():
#         bot.send_message(message.chat.id, is_user_all())
def send_message_timer():
    bot.send_message(chanel_name, 'Можете предложить свою новость\n Для этого напишите мне - @Levelraund1_bot')


# Запускаем бота
bot.polling(none_stop=True, interval=0)
