import telebot;

bot = telebot.TeleBot('6842550234:AAEMaf-fHRaMudvrE6lPaWCtAqVe2-wTKf4')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Привет! Я чат-бот Колледжа связи №54 ОП-5")
        bot.send_message(message.from_user.id, "Здесь ты сможешь заполнить анкету для поступления, ")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        
bot.polling(none_stop=True, interval=0)