import telebot
from telebot import types
import config
# import to_buy
# from to_buy import build_menu
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🗄 Мои предложения")
    btn2 = types.KeyboardButton("💰 Поиск предложений")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Здравствуйте, {0.first_name}! Я тестовый бот для продажи покупки проектов!".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def main_menu_handler(message):
    if (message.text == "🗄 Мои предложения"):
        '''
        ВИКИН КОД (вызваешь функцию из файла to_sell)
        '''
        bot.send_message(message.chat.id, text="VIKA...")



    elif (message.text == "💰 Поиск предложений"):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bt1 = types.KeyboardButton("Выбрать категорию")
        bt2 = types.KeyboardButton("Выбрать ценовой диапазон")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(bt1, bt2, back)
        bot.send_message(message.chat.id, text="Выберите действие", reply_markup=markup)
    elif message.text == "Выбрать категорию":

        ##########
        # список кнопок
        button_list = [
            types.InlineKeyboardButton(text="Category 1", callback_data='fjnd'),
            types.InlineKeyboardButton(text="Category 2", callback_data='dujfd'),
            types.InlineKeyboardButton(text="Category 3",callback_data='fcjdsu')
        ]

        # сборка клавиатуры из кнопок `InlineKeyboardButton`
        reply_markup = types.InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        # отправка клавиатуры в чат
        bot.send_message(message.chat.id, text="Меню Категорий", reply_markup=reply_markup)

        ##########

    elif message.text == "Выбрать ценовой диапазон":

        ##########
        bot.send_message(message.chat.id, "...........В разработке..................")
        ##########

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("🗄 Мои предложения")
        button2 = types.KeyboardButton("💰 Поиск предложений")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")

        # bot.send_message(message.chat.id, text="IRISHKA...")
def build_menu(buttons, n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

bot.polling(non_stop=True)
