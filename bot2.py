import telebot
from telebot import types

bot = telebot.TeleBot ('7074490969:AAG6NZ22f0TOLTVhP_pKdXV2gxleK-KdEhs') # токен.


@bot.message_handler(commands=['start'])

def start(message):
    name = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, name, parse_mode='html')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://google.com"))
    bot.send_message(message.chat.id, "перейти на сайт", parse_mode='html', reply_markup=markup)

    
@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton("Сайт гугл")
    start = types.KeyboardButton("Старт")
    markup.add(website,start)
    bot.send_message(message.chat.id, "перейти на сайт", parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)