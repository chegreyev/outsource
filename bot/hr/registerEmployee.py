'''
    The user inputs his information data , all the info saves in User class
    after the confirmation of information data , bot sends to django database
'''

from keyboards import register_employee_markup, change_register_employee
from bot import bot, user


@bot.callback_query_handler(lambda callback: callback.data == 'new_employee_start_message__register')
def registerNewEmployee(callback):
    bot.send_message(callback.message.chat.id,
                     'Мы приступаем к регистрации/введении нового сотрудника в базу данных\nВведите пожалуйста как вас зовут (ФИО)')
    bot.register_next_step_handler(callback.message, registerName)


def registerName(m):
    user.telegram_id = m.from_user.id
    name = m.text.split(" ")
    user.last_name = name[0]
    user.first_name = name[1]
    user.father_name = name[2]
    bot.send_message(m.chat.id,
                     f'Отлично {name[1]}, теперь введите номер ИИН')
    bot.register_next_step_handler(m, registerIIN)


def registerIIN(m):
    user.iin = m.text
    bot.send_message(m.chat.id,
                     'Хорошо теперь нужно будет ввести данные удовстверения, заранее подготовьте пожалуйста удовстверение\nВведите пожалуйста номер удовстверения')
    bot.register_next_step_handler(m, registerUDVnumber)


def registerUDVnumber(m):
    user.udv_number = m.text
    bot.send_message(m.chat.id,
                     'Отлично , теперь введите пожалуйста дату получения удостоверения. Например: 2000-05-19')
    bot.register_next_step_handler(m, registerUDVdate)


def registerUDVdate(m):
    user.udv_date = m.text
    bot.send_message(m.chat.id,
                     'Теперь введите место получения удостворения. Например : МВД РК')
    bot.register_next_step_handler(m, registerUDVplace)


def registerUDVplace(m):
    user.udv_place = m.text
    bot.send_message(m.chat.id,
                     'Теперь введите ваше фактическое место проживания')
    bot.register_next_step_handler(m, registerAddress)


def registerAddress(m):
    user.address = m.text
    bot.send_message(m.chat.id,
                     'Отлично, теперь нужен номер банковской карты. Например: 5169 4971')
    bot.register_next_step_handler(m, registerBankCard)


def registerBankCard(m):
    card_number = m.text.split(" ")
    correct_card_number = ''
    for i in card_number:
        correct_card_number += i
    user.bank_card = correct_card_number
    bot.send_message(m.chat.id,
                     'Теперь введите данные IBAN')
    bot.register_next_step_handler(m, registerIBAN)


def registerIBAN(m):
    user.iban = m.text
    bot.send_message(m.chat.id,
                     'Введите данные контактные , начнем с телефона. Пример : 87022465104')
    bot.register_next_step_handler(m,
                                   registerContactPhone)


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
    hr_emp = user.get_hr()
    # Sends HR employee the "new_employee" alert
    bot.send_message(
        hr_emp,
        f'В боте зарегестрировался новый сотрудник\n{user.user_to_string_tg(user)}'
    )
    # Sends the current user info that he is added to database
    bot.send_message(
        callback.message.chat.id,
        text=f'Сотрудник {user.first_name} был успешно добавлен.'
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
