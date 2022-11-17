import openpyxl
import telebot
from tqdm import tqdm
from utils_for_skd import is_user

bot = telebot.TeleBot('5766012834:AAHgsslpBBbumdkKCZ_b5X0HsJwc5FBsrH4')  # Токен от bot_father



@bot.message_handler(commands=['help'])
def register(message):
    bot.send_message(message.chat.id, 'Поиск по позициям на В1. Нажмите : /start')


@bot.message_handler(commands=['start'])
def register(message):
#     bot.send_message(message.chat.id, 'Ввелите пароль! ')
#
#
#
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#
#
#     if is_user(message):
    bot.send_message(message.chat.id, 'Что ищем? ')
    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        excel_file = openpyxl.load_workbook('skl_b1.xlsx')
        sheet_sheet = excel_file['Лист1']  # Выбираем лист в файле exel
        search = message.text

        for x in tqdm(range(1, sheet_sheet.max_row + 1)):  # Печать всех значений из столбца
            found = sheet_sheet.cell(row=x, column=2).value
            if search in sheet_sheet.cell(row=x, column=2).value:
                quantity = sheet_sheet.cell(row=x, column=3).value
                print(f" {found} имеется в количестве {quantity} шт. ")
                bot.send_message(message.chat.id,
                            f" {sheet_sheet.cell(row=x, column=2).value} в наличии {sheet_sheet.cell(row=x, column=3).value} шт.")
                                # bot.send_message(message.chat.id,
                                #                  f" {get_search(message)} в наличии {get_search(quantity)} шт.")
                                #
            else:

                if x == sheet_sheet.max_row:
                    print("Not found!")
                    bot.send_message(message.chat.id, " Search complited")

        excel_file.close()
        # else:
        #     bot.send_message(message.chat.id, " Попробуйте еще раз: /start")




# print(f" {search} имеется в количестве {quantity} шт. ")
bot.polling(none_stop=True, interval=0)
