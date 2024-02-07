from telebot import types;
import telebot;
import time;

bot = telebot.TeleBot('6842550234:AAEMaf-fHRaMudvrE6lPaWCtAqVe2-wTKf4')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "1":
        time.sleep(1)
        bot.send_message(message.from_user.id, "Привет! Я чат-бот Колледжа связи №54 ОП-5")
        time.sleep(1)
        bot.send_message(message.from_user.id, "Здесь ты сможешь заполнить анкету для поступления, узнать про специальности нашего подразделения, и еще что - то будет делать (пока хз))")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        
bot.polling(none_stop=True, interval=0)