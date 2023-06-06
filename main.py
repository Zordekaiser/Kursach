import telebot
from telebot import types
import emoji
import pymongo
from sc_client.client import connect, disconnect, create_elements
from sc_kpm.utils import get_element_by_norole_relation, get_link_content_data
from sc_kpm import ScKeynodes
from Foo import get_smartphones_addrs, get_processors_addrs, get_params_smartphone, get_params_app, get_params_processor, get_definition
from operator import itemgetter

url = "ws://localhost:8090/ws_json"
connect(url)

def get_processor():
    buffer = []
    idtf = get_processors_addrs()[1:]
    for i in idtf:
        buffer.append(get_params_processor(i))
    return buffer
def get_smartphones():
    buffer = []
    idtf = get_smartphones_addrs()[3:]
    for i in idtf:
        buffer.append(get_params_smartphone(i))
    return buffer

# def get_apps():
#     buffer = []
#     idtf = get_smartphones_idtf('concept_application')
#     for i in idtf:
#         buffer.append(get_params_app(i))
#     return buffer

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
    mess = "<i>Вас приветствует интеллектуальная справочная система по мобильным телефонам!\nВыберите задачу:</i>"
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

# print(get_smartphones())
class Smarphones:
    list_params = ['name', 'OS', 'processor', 'RAM', 'HDD', 'main_camera', 'front_camera', 'display_size', 'battery']
    buffer_smartphones = []
    buffer_smartphones_counter = 0

class Apps:
    list_params = ['name', 'definition']
    buffer_apps = []
    buffer_apps_counter = 0

class Processors:
    list_params = ['name', 'count_of_cores', 'frenquency', 'processor_manufacturer']
    buffer_processors = []
    buffer_processors_counter = 0

buf_smartphone = Smarphones
buf_app = Apps
buf_processor = Processors

@bot.message_handler(content_types=['text'])
def func(message):
    global buf_processor
    global buf_app
    global buf_smartphone
    if message.text == 'Вернуться в главное меню':

        buf_smartphone.buffer_smartphones =[]
        buf_smartphone.buffer_smartphones_counter = 0
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
        button4 = types.KeyboardButton('Хочу просто звонить и иногда выходить в социальные сети')
        button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3, button4, button)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Хочу делать красивые фотографии':
        mess = ""

        buf_smartphone.buffer_smartphones = sorted(get_smartphones(), key=itemgetter('main_camera', 'front_camera'))
        for i in buf_smartphone.list_params:
            mess += f"<i>{i}: {buf_smartphone.buffer_smartphones[buf_smartphone.buffer_smartphones_counter][i]}\n</i>"
        mess += "<i>Выберите дейтвие:</i>"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Следующий телефон')
        button2 = types.KeyboardButton('Предыдущий телефон')
        button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Хочу смотреть фильмы и сериалы':
        mess = ""

        buf_smartphone.buffer_smartphones = sorted(get_smartphones(), key=itemgetter('display_size'))
        for i in buf_smartphone.list_params:
            mess += f"<i>{i}: {buf_smartphone.buffer_smartphones[buf_smartphone.buffer_smartphones_counter][i]}\n</i>"
        mess += "<i>Выберите дейтвие:</i>"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Следующий телефон')
        button2 = types.KeyboardButton('Предыдущий телефон')
        button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Хочу играть в крутые игры':
        mess = ""

        buf_smartphone.buffer_smartphones = sorted(get_smartphones(), key=itemgetter('RAM', 'battery'))
        for i in buf_smartphone.list_params:
            mess += f"<i>{i}: {buf_smartphone.buffer_smartphones[buf_smartphone.buffer_smartphones_counter][i]}\n</i>"
        mess += "<i>Выберите дейтвие:</i>"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Следующий телефон')
        button2 = types.KeyboardButton('Предыдущий телефон')
        button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Хочу просто звонить и иногда выходить в социальные сети':
        mess = ""

        buf_smartphone.buffer_smartphones = sorted(get_smartphones(), key=itemgetter('battery'))
        for i in buf_smartphone.list_params:
            mess += f"<i>{i}: {buf_smartphone.buffer_smartphones[buf_smartphone.buffer_smartphones_counter][i]}\n</i>"
        mess += "<i>Выберите дейтвие:</i>"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Следующий телефон')
        button2 = types.KeyboardButton('Предыдущий телефон')
        button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Следующий телефон':

        if buf_smartphone.buffer_smartphones_counter < 15:
            buf_smartphone.buffer_smartphones_counter += 1
            mess = ""
            for i in buf_smartphone.list_params:
                mess += f"<i>{i}: {buf_smartphone.buffer_smartphones[buf_smartphone.buffer_smartphones_counter][i]}\n</i>"
            mess += "<i>Выберите дейтвие:</i>"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Следующий телефон')
            button2 = types.KeyboardButton('Предыдущий телефон')
            button = types.KeyboardButton('Вернуться в главное меню')
            markup.add(button1, button2, button)
            bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
        else:
            mess = "<i>Были представлены все смартфоны</i>"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Предыдущий телефон')
            button = types.KeyboardButton('Вернуться в главное меню')
            markup.add(button1, button)
            bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Предыдущий телефон':

        if buf_smartphone.buffer_smartphones_counter > 0:
            buf_smartphone.buffer_smartphones_counter -= 1
            mess = ""
            for i in buf_smartphone.list_params:
                mess += f"<i>{i}: {buf_smartphone.buffer_smartphones[buf_smartphone.buffer_smartphones_counter][i]}\n</i>"
            mess += "<i>Выберите дейтвие:</i>"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Следующий телефон')
            button2 = types.KeyboardButton('Предыдущий телефон')
            button = types.KeyboardButton('Вернуться в главное меню')
            markup.add(button1, button2, button)
            bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
        else:
            mess = "<i>Вы вернулись в начало списка</i>"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Следующий телефон')
            button = types.KeyboardButton('Вернуться в главное меню')
            markup.add(button1, button)
            bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Какие комплектующие телефона существуют?' or message.text == 'Вернуться к комплектующим':
        mess = "<i>Выберите интересующую комплектующую:</i>"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Процессор')
        button2 = types.KeyboardButton('Камера')
        button3 = types.KeyboardButton('Матрицы')
        button5 = types.KeyboardButton('Операционные системы и их разновидности')
        button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3, button5, button)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Процессор':
        text = get_definition('processor')
        mess = f'<i>{text}</i>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Какие процессоры сущесвтуют?')
        button2 = types.KeyboardButton('Вернуться к комплектующим')
        button3 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Какие процессоры сущесвтуют?':
        mess = ""

        buf_processor.buffer_processors = get_processor()
        for i in buf_processor.list_params:
            mess += f"<i>{i}: {buf_processor.buffer_processors[buf_processor.buffer_processors_counter][i]}\n</i>"
        mess += "<i>Выберите дейтвие:</i>"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Следующий процессор')
        button2 = types.KeyboardButton('Предыдущий процессор')
        button = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Следующий процессор':

        if buf_processor.buffer_processors_counter < len(buf_processor.buffer_processors):
            buf_processor.buffer_processors_counter += 1
            mess = ""
            for i in buf_processor.list_params:
                mess += f"<i>{i}: {buf_processor.buffer_processors[buf_processor.buffer_processors_counter][i]}\n</i>"
            mess += "<i>Выберите дейтвие:</i>"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Следующий процессор')
            button2 = types.KeyboardButton('Предыдущий процессор')
            button = types.KeyboardButton('Вернуться в главное меню')
            markup.add(button1, button2, button)
            bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
        else:
            mess = "<i>Вы пришли в конец списка</i>"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Предыдущий процессор')
            button = types.KeyboardButton('Вернуться в главное меню')
            markup.add(button1, button)
            bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Предыдущий процессор':

        if buf_processor.buffer_processors_counter > 0:
            buf_processor.buffer_processors_counter -= 1
            mess = ""
            for i in buf_processor.list_params:
                mess += f"<i>{i}: {buf_processor.buffer_processors[buf_processor.buffer_processors_counter][i]}\n</i>"
            mess += "<i>Выберите дейтвие:</i>"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Следующий процессор')
            button2 = types.KeyboardButton('Предыдущий процессор')
            button = types.KeyboardButton('Вернуться в главное меню')
            markup.add(button1, button2, button)
            bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
        else:
            mess = "<i>Вы вернулись в начало списка</i>"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Следующий процессор')
            button = types.KeyboardButton('Вернуться в главное меню')
            markup.add(button1, button)
            bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Камера':
        text = get_definition('main_camera')
        mess = f'<i>{text}</i>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Вернуться к комплектующим')
        button2 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    elif message.text == 'Матрицы':
        text = get_definition('matrix')
        mess = f'<i>{text}</i>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Вернуться к комплектующим')
        button2 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, mess, parse_mode='html')

    elif message.text == 'Операционные системы и их разновидности':
        text = get_definition('OS')
        mess = f'<i>{text}</i>'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Вернуться к комплектующим')
        button2 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2)
        mess += '\n<i>Существуют следующие типы операционных систем: Android, iOS.</i>'
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

    elif message.text == 'Следующее приложение':

        if buf_app.buffer_apps_counter < len(buf_app.buffer_apps):
            buf_app.buffer_apps_counter += 1
            mess = ""
            for i in buf_app.list_params:
                mess += f"<i>{i}: {buf_app.buffer_apps[buf_app.buffer_apps_counter][i]}\n</i>"
            mess += "<i>Выберите дейтвие:</i>"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Следующее приложение')
            button2 = types.KeyboardButton('Предыдущее приложение')
            button = types.KeyboardButton('Вернуться в главное меню')
            markup.add(button1, button2, button)
            bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
        else:
            mess = "<i>Были представлены все приложения</i>"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Предыдущее приложение')
            button = types.KeyboardButton('Вернуться в главное меню')
            markup.add(button1, button)
            bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

    elif message.text == 'Предыдущее приложение':

        if buf_app.buffer_apps_counter > 0:
            buf_app.buffer_apps_counter -= 1
            mess = ""
            for i in buf_app.list_params:
                mess += f"<i>{i}: {buf_app.buffer_apps[buf_app.buffer_apps_counter][i]}\n</i>"
            mess += "<i>Выберите дейтвие:</i>"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Следующее приложние')
            button2 = types.KeyboardButton('Предыдущее приложение')
            button = types.KeyboardButton('Вернуться в главное меню')
            markup.add(button1, button2, button)
            bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
        else:
            mess = "<i>Вы вернулись в начало списка</i>"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Следующее приложние')
            button = types.KeyboardButton('Вернуться в главное меню')
            markup.add(button1, button)
            bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)


