from bot import bot
from keyboards import *
from user import User
from settings import token
from keyboards import *

from bot import bot

import hr.registerEmployee
import hr.changeRegisterEmployee
import hr.deleteEmployee

import hr.hrFunctions
import adminFunctions


@bot.message_handler(commands=['start'])
def start(message):
    check = User().check_user(message.from_user.id)

    if check == 'hr':
        bot.send_message(
            message.from_user.id,
            'Поздравляю, вы успешно авторизовались! Теперь вы будете получать уведомление от новых сотрудников',
            reply_markup=hr_start_message__markup
        )
    elif check == 'admin':
        bot.send_message(
            message.from_user.id,
            'Поздравляю, вы успешно авторизовались! Теперь вы будете получать уведомление от новых сотрудников',
        )
    elif check == 'employee':
        bot.send_message(
            message.from_user.id,
            'Поздравляю, вы успешно авторизовались!',
            reply_markup=employee_start_message__markup
        )
    else:
        bot.send_message(
            message.from_user.id,
            'Здравствуйте, я Aiva Bot.\nВаш помощник в компании\n-Предоставление услуг\n-Консультирование\n-Управление'
        )
        bot.send_message(
            message.from_user.id,
            'Вы не зарегестрированы в системе\nПожалуйста зарегестрируйтесь.',
            reply_markup=new_employee_start_message__markup
        )


bot.polling(none_stop=True , timeout=30)
