from telebot import types;
import telebot;
import time;

bot = telebot.TeleBot('6842550234:AAEMaf-fHRaMudvrE6lPaWCtAqVe2-wTKf4')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    time.sleep(1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я чат-бот Колледжа связи №54 ОП-5".format(message.from_user), reply_markup=markup)
    time.sleep(1)
    bot.send_message(message.chat.id, text="Здесь ты сможешь заполнить анкету для поступления, узнать про специальности нашего подразделения, и еще что - то будет делать (пока хз))".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет..!)")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Пока ничего нету")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        
bot.polling(none_stop=True, interval=0)