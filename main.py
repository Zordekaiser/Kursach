import telebot
from telebot import types
import emoji
import pymongo


from sc_client.client import connect
url = "ws://localhost:8090/ws_json"
connect(url)

#:clown_face:
def extract_arg(arg):
    buffer = arg.split()
    bufferDict = {}
    for i in range(1, len(buffer), 2):
        bufferDict[buffer[i]] = buffer[i+1]
    return bufferDict

def underscoreToSpace(text):
    buffer = text.replace("_", " ")
    return buffer

def error(chatId):
    bot.send_message(chatId, emoji.emojize(":clown_face:"), parse_mode='html')

bot = telebot.TeleBot('6177377096:AAFZ8-jBiPYTvOpDxIIi9bIwjM4mqKymVv8')


db_client = pymongo.MongoClient("mongodb://localhost:27017/")

current_db = db_client["kursach"]
workCollection = current_db["workCollection"]
systemCollection = current_db["systemCollection"]
dataCollection = current_db["dataCollection"]

@bot.message_handler(commands=['start'])
def start(message):
    mess = "<i>Вас приветствует интеллектуальная система по мобильным телефонам!\nВыберите задачу:</i>"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Помоги подобрать телефон')
    button2 = types.KeyboardButton('Какие комплектующие телефона существуют?')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['work'])
def create(message):
    try:
        workCollection.insert_one(extract_arg(message.text))
    except:
        error(message.chat.id)
    else:
        bot.send_message(message.chat.id, emoji.emojize("<i>Успешно создан! :thumbs_up:</i>"), parse_mode='html')

@bot.message_handler(commands=['system'])
def create(message):
    try:
        systemCollection.insert_one(extract_arg(message.text))
    except:
        error(message.chat.id)
    else:
        bot.send_message(message.chat.id, emoji.emojize("<i>Успешно создан! :thumbs_up:</i>"), parse_mode='html')

@bot.message_handler(commands=['data'])
def create(message):
    try:
        dataCollection.insert_one(extract_arg(message.text))
    except:
        error(message.chat.id)
    else:
        bot.send_message(message.chat.id, emoji.emojize("<i>Успешно создан! :thumbs_up:</i>"), parse_mode='html')


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Вернуться в главное меню':
        mess = "<i>Выберите задачу:</i>"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Помоги подобрать телефон')
        button2 = types.KeyboardButton('Какие комплектующие телефона существуют?')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Помоги подобрать телефон':
        mess = "<i>Какой критерий у телефона важен?</i>"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Хочу делать красивые фотографии')
        button2 = types.KeyboardButton('Хочу смотреть фильмы и сериалы')
        button3 = types.KeyboardButton('Хочу играть в крутые игры')
        button4 = types.KeyboardButton('Хочу всё и сразу')
        button5 = types.KeyboardButton('Хочу просто звонить и иногда выходить в социальные сети')
        button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3, button4, button5, button)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Какие комплектующие телефона существуют?' or message.text == 'Вернуться к комплектующим':
        mess = "<i>Выберите интересующую комплектующую:</i>"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Процессор')
        button2 = types.KeyboardButton('Камера')
        button3 = types.KeyboardButton('Матрицы и их разновидности')
        button4 = types.KeyboardButton('Сенсоры и их разновидности')
        button5 = types.KeyboardButton('Операционные системы и их разновидности')
        button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3, button4, button5, button)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Процессор':
        defin = dataCollection.find({'_id': 'processor'})
        buffer = defin.next()
        text = buffer["definition"]
        mess = f'<i>{underscoreToSpace(text)}</i>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Вернуться к комплектующим')
        button2 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Камера':
        defin = dataCollection.find({'_id': 'camera'})
        buffer = defin.next()
        text = buffer["definition"]
        mess = f'<i>{underscoreToSpace(text)}</i>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Вернуться к комплектующим')
        button2 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Сенсоры и их разновидности' or message.text == 'Вернуться к сенсорам':
        defin = dataCollection.find({'_id': 'sensor'})
        buffer = defin.next()
        text = buffer["definition"]
        mess = f'<i>{underscoreToSpace(text)}</i>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Вернуться к комплектующим')
        button2 = types.KeyboardButton('Акселерометр')
        button3 = types.KeyboardButton('Гироскоп')
        button4 = types.KeyboardButton('Датчик освещённости')
        button5 = types.KeyboardButton('Датчик приближения')
        button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3, button4, button5, button)
        bot.send_message(message.chat.id, mess, parse_mode='html')
        mess = "<i>Выберите команду:</i>"
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Акселерометр':
        defin = dataCollection.find({'_id': 'accelerometer'})
        buffer = defin.next()
        text = buffer["definition"]
        mess = f'<i>{underscoreToSpace(text)}</i>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Вернуться к комплектующим')
        button2 = types.KeyboardButton('Вернуться к сенсорам')
        button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Гироскоп':
        defin = dataCollection.find({'_id': 'gyroscope'})
        buffer = defin.next()
        text = buffer["definition"]
        mess = f'<i>{underscoreToSpace(text)}</i>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Вернуться к комплектующим')
        button2 = types.KeyboardButton('Вернуться к сенсорам')
        button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Датчик освещённости':
        defin = dataCollection.find({'_id': 'light_sensor'})
        buffer = defin.next()
        text = buffer["definition"]
        mess = f'<i>{underscoreToSpace(text)}</i>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Вернуться к комплектующим')
        button2 = types.KeyboardButton('Вернуться к сенсорам')
        button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Датчик приближения':
        defin = dataCollection.find({'_id': 'proximity_sensor'})
        buffer = defin.next()
        text = buffer["definition"]
        mess = f'<i>{underscoreToSpace(text)}</i>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Вернуться к комплектующим')
        button2 = types.KeyboardButton('Вернуться к сенсорам')
        button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Матрицы и их разновидности':
        defin = dataCollection.find({'_id': 'matrix'})
        buffer = defin.next()
        text = buffer["definition"]
        mess = f'<i>{underscoreToSpace(text)}</i>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Вернуться к комплектующим')
        button2 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, mess, parse_mode='html')
        countOfMatrix = dataCollection.count_documents({'key': 'matrix'})
        matrixs = dataCollection.find({'key': 'matrix'})
        mess = 'Существуют следующие типы матриц '
        text = ''
        for i in range(0, countOfMatrix):
            buffer = matrixs.next()
            text += buffer["matrix"]
            if i != countOfMatrix - 1:
                text += ", "
            else:
                text += '.'
        bot.send_message(message.chat.id, mess+text, parse_mode='html', reply_markup=markup)
    elif message.text == 'Операционные системы и их разновидности':
        defin = dataCollection.find({'_id': 'OS'})
        buffer = defin.next()
        text = buffer["definition"]
        mess = f'<i>{underscoreToSpace(text)}</i>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Вернуться к комплектующим')
        button2 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, mess, parse_mode='html')
        countOfOS = dataCollection.count_documents({'key': 'OS'})
        OSs = dataCollection.find({'key': 'OS'})
        mess = 'Существуют следующие типы операционных систем '
        text = ''
        for i in range(0, countOfOS):
            buffer = OSs.next()
            text += buffer["name"]
            if i != countOfOS - 1:
                text += ", "
            else:
                text += '.'
        bot.send_message(message.chat.id, mess+text, parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)


