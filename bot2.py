from telebot import TeleBot
import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создание таблиц, если они еще не существуют
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                     id INT PRIMARY KEY,
                     firstname TEXT,
                     lastname TEXT,
                     username TEXT
                )''')

# Функция для регистрации пользователя
def register_user(firstname, lastname, username):
    cursor.execute("INSERT INTO users (id, firstname, lastname, username) VALUES (?, ?, ?, ?)",
                   (None, firstname, lastname, username))
    conn.commit()

# Функция для получения информации о пользователе
def get_user_info(user_id):
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    return cursor.fetchone()

# Создание экземпляра бота
bot = telebot.TeleBot ('7074490969:AAG6NZ22f0TOLTVhP_pKdXV2gxleK-KdEhs')

# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я могу помочь тебе с выбором профессии. Начни с введения своих данных.')

# Обработка команды /register
@bot.message_handler(commands=['register'])
def process_register(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    username = message.chat.username
    user_id = message.chat.id

    # Регистрация пользователя
    register_user(first_name, last_name, username)

    # Отправка подтверждения регистрации
    bot.reply_to(message, f'Ваш аккаунт успешно создан, {first_name}! Теперь мы можем начать профориентацию.')

# Обработка команды /prof
@bot.message_handler(commands=['prof'])
def start_prof(message):
    user_data = get_user_info(message.chat.id)
    if user_data is not None:
        firstname = user_data[1]
        lastname = user_data[2]
        username = user_data[3]
        bot.reply_to(message, f'Здравствуйте, {firstname} {lastname}! Давайте начнем профориентацию.')
    else:
        bot.reply_to(message, 'Пожалуйста, зарегистрируйтесь сначала.')

# Обработка команд для проведения профориентации
@bot.message_handler(content_types=['text'])
def prof_chat(message):
     
    pass

# Запуск бота
bot.infinity_polling()