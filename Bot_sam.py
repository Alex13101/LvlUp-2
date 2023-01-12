import telebot
from telebot import types
#import time

# Создаем экземпляр бота
bot = telebot.TeleBot('5873420513:AAFGxzhyA1wdIOdVZ4xm_Cki23hTMSUecTg')
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
        bot.send_message(message.chat.id, 'Что бы Вы хотели предложить? Кидай ссылку')
        bot.register_next_step_handler(message, news_message)

    elif message.text.strip() == 'Дать совет.':
        bot.send_message(message.chat.id, 'Какой совет? Пишите')
        bot.register_next_step_handler(message, what_Council)
    else:
        bot.send_message(message.chat.id, 'Я такой команды не знаю! \n Кнопки внизу)')


def news_message(message):
    #@bot.message_handler(content_types=["text", "sticker", "pinned_message", "photo", "audio"])

    if message.content_type == 'text':
        bot.send_message(chanel_name, "Новость от\n*{name} {last}*\n{text}".format(name=message.chat.first_name,
                                                                                 last=message.chat.last_name,
                                                                                 text=message.text),
                            parse_mode="Markdown")  # от кого идет сообщение и его содержание
        bot.send_message(message.chat.id, "*{name}!*\n\nСпасибо за инфу \n \nХотели что-то еще? Кнопки внизу".format(name=message.chat.first_name,
                                                                                    last=message.chat.last_name,
                                                                                    text=message.text),
                            parse_mode="Markdown")  # то что пойдет юзеру после отправки сообщения
        bot.send_message(chanel_name, 'предложить новость напиши боту: @redirection_news_bot')
    elif message.content_type == 'photo':
        raw = message.photo[2].file_id
        tekst = message.caption
        name = raw + ".jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(name, 'wb') as new_file:
            new_file.write(downloaded_file)
        img = open(name, 'rb')
        bot.send_message(chanel_name,
                         "Новость от\n*{name} {last}*".format(name=message.chat.first_name, last=message.chat.last_name),
                         parse_mode="Markdown")  # от кого идет сообщение и его содержание
        bot.send_photo(chanel_name, img, caption=tekst)
        bot.send_message(message.chat.id, "*{name}!*\n\nСпасибо за инфу \n \nХотели что-то еще? Кнопки внизу".format(name=message.chat.first_name,
                                                                                last=message.chat.last_name,
                                                                                text=message.text),
                         parse_mode="Markdown")  # то что пойдет юзеру после отправки сообщения
        bot.send_message(chanel_name, 'предложить новость напиши боту: @redirection_news_bot')

def what_Council(message):
    accepted_text = message.text
    f = open('pork.txt', 'a', encoding='UTF-8')
    f.write(f" \n {message.chat.first_name} {message.chat.last_name} посоветовал - {accepted_text} ")
    bot.send_message(message.chat.id, f'Ваш совет: ' + message.text + ' передан')
    bot.send_message(message.chat.id, 'Хотели что-то еще? Кнопки внизу)')

# Запускаем бота
bot.polling(none_stop=True, interval=0)