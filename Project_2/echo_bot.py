import telebot
# Создаем экземпляр бота
bot = telebot.TeleBot('5766012834:AAHgsslpBBbumdkKCZ_b5X0HsJwc5FBsrH4')
chanel_name = '@project_chanel'
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    #bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
    bot.send_message(chanel_name, 'Я на связи. Напиши мне что-нибудь )')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    #bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
    bot.send_message(chanel_name, 'Вы написали в канал: ' + message.text)

# Запускаем бота
bot.polling(none_stop=True, interval=0)
