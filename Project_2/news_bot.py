
import telebot
# Импортируем функции создания и проверки пользователя
from register import is_user_exists, create_user
from utils import is_email_valid

# Создаем экземпляр бота
bot = telebot.TeleBot('_________________') #Токен от bot_father

@bot.message_handler(commands=['help'])
def register(message):
    bot.send_message(message.chat.id, 'Я умею: /start /add_money /my_balance')

@bot.message_handler(commands=['start'])
def register(message):
    user_id = message.chat.id
    if is_user_exists(user_id):
        bot.send_message(user_id, 'Ты уже регистрировался!')
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
        bot.send_message(message.chat.id, f"Спасибо за регистрацию")
        create_user(message.chat.id, name, email)
    else:
        bot.send_message(message.chat.id, f"Некорректная почта")
# Запускаем бота
bot.polling(none_stop=True, interval=0)
