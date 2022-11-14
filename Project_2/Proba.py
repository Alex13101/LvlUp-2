import telebot
from telebot import types
import time

# Создаем экземпляр бота
bot = telebot.TeleBot('5766012834:AAHgsslpBBbumdkKCZ_b5X0HsJwc5FBsrH4')
chanel_name = '@project_chanel'


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')




    # Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Предложить новость.")
    item2 = types.KeyboardButton("Дать совет.")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id,
                     'Нажми: \nПредложить новость, чтобы предложить новость\nДать совет  — дать совет! ',
                     reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        if message.text.strip() == 'Предложить новость.':
            @bot.message_handler(content_types=["text"])
            def handle_text(message):
                bot.send_message(chanel_name, 'Вы предложили новость в канал: ' + message.text)
                bot.send_message(chanel_name, 'Вы предложили новость в канал: ' + message.text)
                bot.send_message(chanel_name, 'https://habr.com/ru/news/')
            # @bot.message_handler(content_types=["text"])
            # def handle_text(message):
            #     bot.send_message(chanel_name, 'Вы предложили новость в канал: ' + message.text)

        elif message.text.strip() == 'Дать совет.':
            @bot.message_handler(content_types=["text"])
            def handle_text(message):
                accepted_text = message
                f = open('pork.txt', 'w', encoding='UTF-8')
                f.write(accepted_text)


    # bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


# Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     # bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
#     bot.send_message(chanel_name, 'Вы написали в канал: ' + message.text)


# Запускаем бота
bot.polling(none_stop=True, interval=0)