'''
    The user inputs his information data , all the info saves in User class
    after the confirmation of information data , botFolder sends to django database
'''

from keyboards import register_employee_markup, change_register_employee , employee_start_message__markup
from bot import bot, user
from checks.check import *
from Files.filesFunctions import *

@bot.callback_query_handler(lambda callback: callback.data == 'new_employee_start_message__register')
def registerNewEmployee(callback):
    bot.send_message(
        callback.message.chat.id,
        'Мы приступаем к регистрации/введении нового сотрудника в базу данных\nВведите пожалуйста ФИО\nНапример : Быков Андрей Михайлович)'
    )
    bot.register_next_step_handler(
        callback.message,
        registerName
    )


def registerName(m):
    if checkRegisteredName(m.text) is True:
        user.telegram_id = m.from_user.id
        name = m.text.split(" ")
        user.last_name = name[0]
        user.first_name = name[1]
        user.father_name = name[2]
        bot.send_message(
            m.chat.id,
            f'Отлично {name[1]}, теперь введите дату Вашего рождения\nНапример: 2000-05-19'
        )
        bot.register_next_step_handler(
            m,
            registerIIN
        )
    else:
        bot.send_message(
            m.chat.id,
            'Вы неверно ввели ФИО\nВведите пожалуйста еще раз\nНапример: Быков Андрей Михайлович'
        )
        bot.register_next_step_handler(
            m,
            registerName
        )

def registerBirthDay(m):
    if checkRegisteredUDVdate(m.text) is True:
        user.birth_day = m.text
        bot.send_message(
            m.chat.id,
            'Отлично , теперь введите номер ИИН'
        )
        bot.register_next_step_handler(
            m,
            registerIIN
        )
    else:
        bot.send_message(
            m.chat.id ,
            'Вы неверно ввели дату Вашего рождения\nВведите пожалуйста еще раз\nНапример: 2000-05-19'
        )

        bot.register_next_step_handler(
            m,
            registerBirthDay
        )

def registerIIN(m):
    if checkRegisteredIIN(m.text) is True:
        user.iin = m.text
        bot.send_message(m.chat.id,
                         'Хорошо теперь нужно будет ввести данные удовстверения, заранее подготовьте пожалуйста удовстверение\nВведите пожалуйста номер удовстверения')
        bot.register_next_step_handler(m, registerUDVnumber)
    else:
        bot.send_message(
            m.chat.id,
            "Вы неверно ввели ИИН\nВведите пожалуйста еще раз\nНапример: 000519500056"
        )
        bot.register_next_step_handler(
            m,
            registerIIN
        )

def registerUDVnumber(m):
    user.udv_number = m.text
    bot.send_message(m.chat.id,
                     'Отлично , теперь введите пожалуйста дату получения удостоверения.\nНапример: 2000-05-19')
    bot.register_next_step_handler(m, registerUDVdate)


def registerUDVdate(m):
    if checkRegisteredUDVdate(m.text) is True:
        user.udv_date = m.text
        bot.send_message(m.chat.id,
                         'Теперь введите место получения удостворения.\nНапример : МВД РК')
        bot.register_next_step_handler(m, registerUDVplace)
    else :
        bot.send_message(
            m.chat.id,
            'Вы неверно ввели Дату получения удостоверения\nВведите пожалуйста еще раз\nНапример: 2000-05-19'
        )
        bot.register_next_step_handler(
            m,
            registerUDVdate
        )


def registerUDVplace(m):
    user.udv_place = m.text
    bot.send_message(m.chat.id,
                     'Теперь введите ваше фактическое место проживания\nНапример : г.Алматы , ул. Розыбакиева')
    bot.register_next_step_handler(m, registerAddress)


def registerAddress(m):
    user.address = m.text
    bot.send_message(m.chat.id,
                     'Отлично, теперь нужен номер банковской карты. Например: 5169 4971')
    bot.register_next_step_handler(m, registerBankCard)


def registerBankCard(m):
    if checkRegisteredBankCard(m.text) is True:
        card_number = m.text.split(" ")
        correct_card_number = ''
        for i in card_number:
            correct_card_number += i
        user.bank_card = correct_card_number
        bot.send_message(m.chat.id,
                         'Теперь введите данные IBAN')
        bot.register_next_step_handler(m, registerIBAN)
    else:
        bot.send_message(
            m.chat.id,
            'Вы неверно ввели номер банковской карты\nВведите пожалуйста еще раз\nНапример: 1234 5678 9101 2345'
        )
        bot.register_next_step_handler(
            m,
            registerBankCard
        )

def registerIBAN(m):
    if checkRegisteredIBAN(m.text) is True:
        user.iban = m.text
        bot.send_message(m.chat.id,
                         'Введите данные контактные , начнем с телефона. Пример : 87022465104')
        bot.register_next_step_handler(m,
                                       registerContactPhone)
    else:
        bot.send_message(
            m.chat.id,
            'Вы неверно введи номер IBAN\nВведите пожалуйста еще раз\nНапример: KZ83722C000012774429'
        )

        bot.register_next_step_handler(
            m,
            registerIBAN
        )

def registerContactPhone(m):
    user.contact_phone = m.text
    bot.send_message(m.chat.id,
                     'Осталось дело за малыи, введите адрес электроной почты. Например: mail@gmail.com')
    bot.register_next_step_handler(m, registerEmail)


def registerEmail(m):
    user.email_address = m.text
    bot.send_message(m.chat.id,
                     user.user_to_string_tg(user),
                     reply_markup=register_employee_markup
                     )


# After the User sends all the information about himself
#   The user gets 2 InlineKeyboardButton:
#       1) Подтвердить ( text ) - correct_employee_data ( callback )
#       2) Изменить данные ( text ) - incorrect_employee_data ( callback )

@bot.callback_query_handler(lambda callback: callback.data == 'correct_employee_data')
def confirm_new_employee(callback):
    user.registerEmployee()
    bot.send_message(
        callback.message.chat.id,
        'Поздравляю, вы успешно зарегестрировались!',
        reply_markup=employee_start_message__markup
    )

    # Sending his Confidential dogovor
    bot.send_document(
        callback.message.chat.id,
        data=confidemtial_dogovor(user.returnUserData(callback.message.chat.id))
    )
    # Sending his Corporate security
    bot.send_document(
        callback.message.chat.id,
        data=corporate_security(user.returnUserData(callback.message.chat.id))
    )
    # Sending his trudovoi dogovor
    bot.send_document(
        callback.message.chat.id,
        data=trudovoi_dogovor(user.returnUserData(callback.message.chat.id))
    )

    hr_emp = user.get_hr()

    # Sends HR employee the "new_employee" alert
    bot.send_message(
        hr_emp,
        f'В боте зарегестрировался новый сотрудник\n{user.user_to_string_tg(user)}'
    )
    # Removes InlineButtons from Employee message info
    bot.edit_message_reply_markup(
        callback.message.chat.id,
        callback.message.message_id
    )




@bot.callback_query_handler(lambda callback: callback.data == 'incorrect_employee_data')
def change_new_employee_data(callback):
    '''
        If the user wants to change his information
        he gets the message of his info with InlineButtons with labels of what to change
    :param callback:
    '''
    bot.edit_message_reply_markup(
        message_id=callback.message.message_id,
        chat_id=callback.message.chat.id,
        reply_markup=change_register_employee
    )
