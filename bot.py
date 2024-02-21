from telebot import types;
import telebot;
import time;

bot = telebot.TeleBot('6842550234:AAEMaf-fHRaMudvrE6lPaWCtAqVe2-wTKf4')

name = ''
age = 0
surname = ''

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("Регистрация ")
    markup.add(btn1, btn2)
    time.sleep(1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я чат-бот Колледжа связи №54 ОП-5".format(message.from_user), reply_markup=markup)
    time.sleep(1)
    bot.send_message(message.chat.id, text="Здесь ты сможешь заполнить анкету для поступления, узнать про специальности нашего подразделения, и еще что - то будет делать (пока хз))".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="whats uuuuuuuppppppppppp!!!!!!maaaaaaan!!!!!)")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Заполнить анкету")
        btn2 = types.KeyboardButton("Подробнее о специальностях")
        btn3 = types.KeyboardButton("Что - то будет")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back) 
        bot.send_message(message.chat.id, text="Выбери чем хочешь заняться)", reply_markup=markup)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Пока ничего нету")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Поздороваться")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    elif (message.text == "Заполнить анкету"):
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name); 
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, get_surname)
def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "сколько тебе лет? ")
    bot.register_next_step_handler(message, get_age)
def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Цифрами пожалуйста!")
        bot.send_message(message.from_user.id, "Тебе " + str(age) + " лет, тебя зовут " + name + " " + surname + "?")
        

bot.polling(none_stop=True, interval=0)