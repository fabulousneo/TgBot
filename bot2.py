import telebot
from telebot import types

bot = telebot.TeleBot ('7074490969:AAG6NZ22f0TOLTVhP_pKdXV2gxleK-KdEhs') # токен.


@bot.message_handler(commands=['start'])

def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать!")
    name = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u>. Это бот колледжа связи №54. Данный бот предоставляет возможность пройти профориентацию и узнать какое направление подойдет именно тебе!</b>'
    markup.add(btn1)
    bot.send_message(message.chat.id, name, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def message (message):
    if  message.text == ('Начать!'):
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn1 = types.KeyboardButton("Информационные системы и программирование")
        btn2 = types.KeyboardButton("Обеспечение информационной безопасности телекоммуникационных систем")
        btn3 = types.KeyboardButton("Обеспечение информационной безопасности автоматизированных систем")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text ="Выбери специальность, которая тебя привлекает: ", reply_markup=markup)
    elif message.text == "Информационные системы и программирование":
        bot.send_message(message.chat.id, text='Вы выбрали информационные системы и программирование')
    elif message.text == "Обеспечение информационной безопасности телекоммуникационных систем":
        bot.send_message(message.chat.id, text="Вы выбрали обеспечение информационной безопасности телекоммуникационных систем")
    elif message.text == "Обеспечение информационной безопасности автоматизированных систем":
        bot.send_message(message.chat.id, text = "Вы выбрали обеспечение информационной безопасности автоматизированных систем")
    else:
        bot.send_message(message.chat.id, text= "Вы ничего не выбрали, сделайте выбор!")



bot.polling(none_stop=True)