'''
    There is the functions to change the registered user data

    After the user enters his information data , the user gets 2 buttons
    Confirm and Change , Change works by the typing new information of concrete date
    and sends to confirm , but he gets the message with his data to confirm/change

    User data:
        -first_name
        -last_name
        -father_name
        -iin
        -udv_number
        -udv_date
        -udv_place
        -address
        -bank_card
        -iban
        -contact_phone
        -email_address
'''
from keyboards import change_register_employee
from bot import bot, user


@bot.callback_query_handler(lambda callback: callback.data == 'change_first_name')
def change_new_employee_first_name(callback):
    bot.send_message(
        callback.message.chat.id,
        'Введите пожалуйста ваше Имя:'
    )
    bot.register_next_step_handler(
        callback.message,
        registerChangedFirstName
    )


def sendUser(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=user.user_to_string_tg(user),
        reply_markup=change_register_employee
    )


def registerChangedFirstName(message):
    user.first_name = message.text
    bot.send_message(
        message.chat.id,
        f'Вы успешно поменяли Имя на {user.first_name}'
    )
    sendUser(message)


@bot.callback_query_handler(lambda callback: callback.data == 'change_last_name')
def change_new_employee_last_name(callback):
    bot.send_message(
        callback.message.chat.id,
        'Введите пожалуйста вашу Фамилию:'
    )
    bot.register_next_step_handler(
        callback.message,
        registerChangedLastName
    )


def registerChangedLastName(message):
    user.last_name = message.text
    bot.send_message(
        message.chat.id,
        f'Вы успешно поменяли Фамилию на {user.last_name}'
    )
    sendUser(message)


@bot.callback_query_handler(lambda callback: callback.data == 'change_father_name')
def change_new_employee_father_name(callback):
    bot.send_message(
        callback.message.chat.id,
        'Введите пожалуйста ваше Отчество:'
    )

    bot.register_next_step_handler(
        callback.message,
        registerChangedFatherName
    )


def registerChangedFatherName(message):
    user.father_name = message.text
    bot.send_message(
        message.chat.id,
        f'Вы успешно поменяли Отчество на {user.father_name}'
    )

    sendUser(message)


@bot.callback_query_handler(lambda callback: callback.data == 'change_iin')
def change_new_employee_iin(callback):
    bot.send_message(
        callback.message.chat.id,
        'Введите пожалуйста ваш ИИН:'
    )

    bot.register_next_step_handler(
        callback.message,
        registerChangedIIN
    )


def registerChangedIIN(message):
    user.iin = message.text
    bot.send_message(
        message.chat.id,
        f'Вы успешно поменяли ваш ИИН на {user.iin}'
    )

    sendUser(message)


@bot.callback_query_handler(lambda callback: callback.data == 'change_udv_number')
def change_new_employee_udv_number(callback):
    bot.send_message(
        callback.message.chat.id,
        'Введите пожалуйста ваш номер удостоверения:'
    )

    bot.register_next_step_handler(
        callback.message,
        registerChangedudvNumber
    )


def registerChangedudvNumber(message):
    user.udv_number = message.text
    bot.send_message(
        message.chat.id,
        f'Вы успешно поменяли ваш номер удостоверения на {user.udv_number}'
    )

    sendUser(message)


@bot.callback_query_handler(lambda callback: callback.data == 'change_udv_date')
def change_new_employee_udv_date(callback):
    bot.send_message(
        callback.message.chat.id,
        'Введите пожалуйста дату номера удостоверения:'
    )

    bot.register_next_step_handler(
        callback.message,
        registerChangedudvDate
    )


def registerChangedudvDate(message):
    user.udv_date = message.text
    bot.send_message(
        message.chat.id,
        f'Вы успешно поменяли вашу дату номера удостоверения на {user.udv_date}'
    )
    sendUser(message)


@bot.callback_query_handler(lambda callback: callback.data == 'change_udv_place')
def change_new_employee_udv_place(callback):
    bot.send_message(
        callback.message.chat.id,
        'Введите пожалуйста место получения удостоверения:'
    )

    bot.register_next_step_handler(
        callback.message,
        registerChangedudvPlace
    )


def registerChangedudvPlace(message):
    user.udv_place = message.text
    bot.send_message(
        message.chat.id,
        f'Вы успешно поменяли место получения удостоверения на {user.udv_place}'
    )
    sendUser(message)


@bot.callback_query_handler(lambda callback: callback.data == 'change_address')
def change_new_employee_address(callback):
    bot.send_message(
        callback.message.chat.id,
        'Введите пожалуйста место проживания:'
    )

    bot.register_next_step_handler(
        callback.message,
        registerChangedAddress
    )


def registerChangedAddress(message):
    user.address = message.text
    bot.send_message(
        message.chat.id,
        f'Вы успешно поменяли место проживания на {user.address}'
    )
    sendUser(message)


@bot.callback_query_handler(lambda callback: callback.data == 'change_bank_card')
def change_new_employee_bank_card(callback):
    bot.send_message(
        callback.message.chat.id,
        'Введите пожалуйста номер банковской карты:'
    )

    bot.register_next_step_handler(
        callback.message,
        registerChangedBankCard
    )


def registerChangedBankCard(message):
    user.bank_card = message.text
    bot.send_message(
        message.chat.id,
        f'Вы успешно поменяли номер банковской карты на {user.bank_card}'
    )
    sendUser(message)


@bot.callback_query_handler(lambda callback: callback.data == 'change_iban')
def change_new_employee_iban(callback):
    bot.send_message(
        callback.message.chat.id,
        'Введите пожалуйста номер IBAN:'
    )

    bot.register_next_step_handler(
        callback.message,
        registerChangedIban
    )


def registerChangedIban(message):
    user.iban = message.text
    bot.send_message(
        message.chat.id,
        f'Вы успешно поменяли номер IBAN на {user.iban}'
    )
    sendUser(message)


@bot.callback_query_handler(lambda callback: callback.data == 'change_contact_phone')
def change_new_employee_contact_phone(callback):
    bot.send_message(
        callback.message.chat.id,
        'Введите пожалуйста ваш контактный номер:'
    )

    bot.register_next_step_handler(
        callback.message,
        registerChangedContactPhone
    )


def registerChangedContactPhone(message):
    user.contact_phone = message.text
    bot.send_message(
        message.chat.id,
        f'Вы успешно поменяли контактный номер на {user.contact_phone}'
    )

    sendUser(message)


@bot.callback_query_handler(lambda callback: callback.data == 'change_email_address')
def change_new_employee_email_address(callback):
    bot.send_message(
        callback.message.chat.id,
        'Введите пожалуйста ваш email :'
    )

    bot.register_next_step_handler(
        callback.message,
        registerChangedEmailAddress
    )


def registerChangedEmailAddress(message):
    user.email_address = message.text
    bot.send_message(
        message.chat.id,
        f'Вы успешно поменяли email на {user.email_address}'
    )

    sendUser(message)
