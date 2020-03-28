from bot import bot , user
from user import User , Vopros
from pprint import pprint

adminVopros = Vopros()

def takeFromMessageUserId(text):
    id = text.split('\n')[2].split(' ')[3]
    return int(id)

def takeFromMessageMoney(text):
    money = text.split('\n')[4].split(' ')[2]
    return money

def takeFromSingleMessageVopros(text):
    vopros = text.split('\n')[3]
    return vopros

def takeFromDoubleMessageVopros(text):
    vopros_list = text.split('\n')[3:]
    vopros = ''
    for i in vopros_list:
        vopros+=i + '\n'
    return vopros

@bot.callback_query_handler(lambda callback: callback.data == 'admin_take_money__markup__accept')
def adminAcceptMoney(callback):
    bot.send_message(
        callback.message.chat.id ,
        'Отлично , деньги будут выданы в течении дня.'
    )

    bot.send_message(
        takeFromMessageUserId(callback.message.text),
        f'Admin ответил на ваш запрос\nЗапрос : {takeFromMessageMoney(callback.message.text)} тг\nОтвет : Одобрен\nВ течении дня вам выдадут деньги'
    )

@bot.callback_query_handler(lambda callback: callback.data == 'admin_take_money__markup__decline')
def adminDeclineMoney(callback):
    bot.send_message(
        callback.message.chat.id ,
        'Хорошо , сотрудник будет осведомлен.'
    )

    bot.send_message(
        takeFromMessageUserId(callback.message.text),
        f'Admin ответил на ваш запрос\nЗапрос : {takeFromMessageMoney(callback.message.text)} тг\nОтвет : Отклонен\nПодумайте на счет причины отклонения и попробуйте снова'
    )

@bot.callback_query_handler(lambda callback: callback.data == 'admin_single_vopros__markup__answer')
def adminSingleVopros(callback):
        adminVopros.adminVopros = callback.message.text

        bot.send_message(
            callback.message.chat.id,
            'Ваш ответ :'
        )

        bot.register_next_step_handler(
            callback.message,
            adminAnswerSingleVopros
        )

def adminAnswerSingleVopros(message):

    bot.send_message(
        message.chat.id,
        f'Спасибо , сотрудник {User().get_user_full_name(takeFromMessageUserId(adminVopros.adminVopros))} будет вам благодарен.'
    )

    bot.send_message(
        takeFromMessageUserId(adminVopros.adminVopros),
        f'Admin ответил на ваш вопрос.\n{takeFromSingleMessageVopros(adminVopros.adminVopros)}\nОтвет : {message.text}'
    )

@bot.callback_query_handler(lambda callback: callback.data == 'admin_single_vopros__markup__incorrect')
def adminSingleVoprosIncorrect(callback):
    bot.send_message(
        callback.message.chat.id,
        'Сотрудник будет проинформирован'
    )

    bot.send_message(
        takeFromMessageUserId(callback.message.text),
        f'Admin ответил на ваш вопрос.\n{takeFromSingleMessageVopros(callback.message.text)}\nОтвет : Некорректный вопрос.\nПодумайте насчет причины отклонения и попробуйте снова.'
    )

@bot.callback_query_handler(lambda callback: callback.data == 'admin_double_vopros__markup__first')
def adminDoubleVoprosFirst(callback):
    bot.send_message(
        callback.message.chat.id,
        'Спасибо , Сотрудник будет проинформирован'
    )

    bot.send_message(
        takeFromMessageUserId(callback.message.text),
        f'Admin ответил на ваш вопрос.\n{takeFromDoubleMessageVopros(callback.message.text)}\nОтвет : 1'
    )

@bot.callback_query_handler(lambda callback: callback.data == 'admin_double_vopros__markup__double')
def adminDoubleVoprosDouble(callback):
    bot.send_message(
        callback.message.chat.id,
        'Спасибо , Сотрудник будет проинформирован'
    )

    bot.send_message(
        takeFromMessageUserId(callback.message.text),
        f'Admin ответил на ваш вопрос.\n{takeFromDoubleMessageVopros(callback.message.text)}\nОтвет : 2'
    )