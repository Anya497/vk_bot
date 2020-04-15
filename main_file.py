import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import config
import json
import keyboards
import datetime
from course import Dollar, Hryvnia, Euro

month = {'1': 'января', '2': 'февраля', '3': 'марта', '4': 'апреля', '5': 'мая', '6': "июня", '7': 'июля',
         '8': 'августа', '9': 'сентября', '10': "октября", "11": "ноября", "12": "декабря"}
now = datetime.datetime.now()
vk_session = vk_api.VkApi(token=config.TOKEN)
longpoll = VkBotLongPoll(vk_session, config.ID)
kol = 0


def main():
    global kol
    for event in longpoll.listen():
        if (event.type == VkBotEventType.GROUP_JOIN or event.type == VkBotEventType.MESSAGE_NEW) and kol == 0:
            kol = 1
            begining(event)
        if event.type == VkBotEventType.GROUP_LEAVE:
            kol = 0
        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['text'] == 'Узнать дату и время':
            time_date(event)
        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['text'] == 'Правила':
            rules(event)
        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['text'] == 'Курсы валют':
            currency(event)
        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['text'] == 'Доллар':
            dollar(event)
        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['text'] == 'Гривна':
            hryvnia(event)
        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['text'] == 'Евро':
            euro(event)
        if event.type == VkBotEventType.MESSAGE_NEW and event.obj.message['text'] == 'Назад':
            vk = vk_session.get_api()
            keyboard = json.dumps(keyboards.KEYBOARD).encode('utf-8')
            keyboard = str(keyboard.decode('utf-8'))
            vk.messages.send(user_id=event.obj.message['from_id'], random_id=random.randint(0, 2 ** 64), message='ОК',
                             keyboard=keyboard)


def dollar(event):
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=random.choice(['Минуточку...', 'Сейчас узнаю']),
                     random_id=random.randint(0, 2 ** 64))
    value = Dollar().get_currency_price()
    vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                     random_id=random.randint(0, 2 ** 64))
    return


def hryvnia(event):
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=random.choice(['Минуточку...', 'Сейчас узнаю']),
                     random_id=random.randint(0, 2 ** 64))
    value = Hryvnia().get_currency_price()
    vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                     random_id=random.randint(0, 2 ** 64))
    return


def euro(event):
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=random.choice(['Минуточку...', 'Сейчас узнаю']),
                     random_id=random.randint(0, 2 ** 64))
    value = Euro().get_currency_price()
    vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                     random_id=random.randint(0, 2 ** 64))
    return


def currency(event):
    vk = vk_session.get_api()
    keyboard = json.dumps(keyboards.KEYBOARD_2).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    vk.messages.send(user_id=event.obj.message['from_id'], message='Выбери валюту',
                     random_id=random.randint(0, 2 ** 64), keyboard=keyboard)
    return


def time_date(event):
    message = "Сегодня " + str(now.day) + ' ' + month[str(now.month)] + ' ' + str(now.year) + ' ' + 'года. ' + \
              "Время: " + str(now.hour) + ':' + str(now.minute)
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=message, random_id=random.randint(0, 2 ** 64))
    return


def rules(event):
    vk = vk_session.get_api()
    keyboard = json.dumps(keyboards.KEYBOARD).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    vk.messages.send(user_id=event.obj.message['from_id'],
                     message=config.RULES,
                     random_id=random.randint(0, 2 ** 64))
    return


def begining(event):
    keyboard = json.dumps(keyboards.KEYBOARD).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    vk = vk_session.get_api()
    if event.type == VkBotEventType.GROUP_JOIN:
        name = vk.users.get(user_id=event.obj.user_id)[0]['first_name']
        vk.messages.send(user_id=event.obj.user_id,
                         message="Добро пожаловать, {}!\nЯ - Волчара, бот, который не выступает в цирке.".format(name),
                         random_id=random.randint(0, 2 ** 64), keyboard=keyboard)
    if event.type == VkBotEventType.MESSAGE_NEW:
        name = vk.users.get(user_id=event.obj.message['from_id'])[0]['first_name']
        vk.messages.send(user_id=event.obj.message['from_id'],
                         message="Добро пожаловать, {}!\nЯ - Волчара, бот, который не выступает в цирке.".format(name),
                         random_id=random.randint(0, 2 ** 64), keyboard=keyboard)
    return


if __name__ == '__main__':
    main()