import telebot

hr_replykeyboard = telebot.types.ReplyKeyboardMarkup()
hr_replykeyboard_btn1 = telebot.types.KeyboardButton('Получить деньги')
hr_replykeyboard_btn2 = telebot.types.KeyboardButton('Задать вопрос')
hr_replykeyboard_btn3 = telebot.types.KeyboardButton('База участников')
hr_replykeyboard.add(hr_replykeyboard_btn1, hr_replykeyboard_btn2, hr_replykeyboard_btn3)

hr_replykeyboard_vopros = telebot.types.ReplyKeyboardMarkup()
hr_replykeyboard_vopros_btn1 = telebot.types.KeyboardButton('Предложить 2 варианта ответа')
hr_replykeyboard_vopros_btn2 = telebot.types.KeyboardButton('Задать точный вопрос')
hr_replykeyboard_vopros.add(hr_replykeyboard_vopros_btn1, hr_replykeyboard_vopros_btn2)

delete_employee_markup = telebot.types.InlineKeyboardMarkup()
delete_btn1 = telebot.types.InlineKeyboardButton(text="Удалить сотрудника", callback_data='delete')
delete_employee_markup.add(delete_btn1)

register_employee_markup = telebot.types.InlineKeyboardMarkup()
register_employee_correct = telebot.types.InlineKeyboardButton(text='Подтвердить',callback_data='correct_employee_data')
register_employee_incorrect = telebot.types.InlineKeyboardButton(text='Изменить данные',callback_data='incorrect_employee_data')
register_employee_markup.row(register_employee_correct, register_employee_incorrect)


change_register_employee = telebot.types.InlineKeyboardMarkup()

first_name = telebot.types.InlineKeyboardButton(text='Имя', callback_data='change_first_name')
last_name = telebot.types.InlineKeyboardButton(text='Фамилия', callback_data='change_last_name')
father_name = telebot.types.InlineKeyboardButton(text='Отчество', callback_data='change_father_name')
iin = telebot.types.InlineKeyboardButton(text='ИИН', callback_data='change_iin')
udv_number = telebot.types.InlineKeyboardButton(text='Номер удв.', callback_data='change_udv_number')
udv_date = telebot.types.InlineKeyboardButton(text='Дата удв.', callback_data='change_udv_date')
udv_place = telebot.types.InlineKeyboardButton(text='Место удв.', callback_data='change_udv_place')
address = telebot.types.InlineKeyboardButton(text='Адрес прож.', callback_data='change_address')
bank_card = telebot.types.InlineKeyboardButton(text='Банк карта', callback_data='change_bank_card')
iban = telebot.types.InlineKeyboardButton(text='IBAN', callback_data='change_iban')
contact_phone = telebot.types.InlineKeyboardButton(text='Номер телефона', callback_data='change_contact_phone')
email_address = telebot.types.InlineKeyboardButton(text='email', callback_data='change_email_address')
confirm_changed_data = telebot.types.InlineKeyboardButton('Подтвердить' , callback_data='correct_employee_data')
#TODO : Нужно добавть функционал для кнопки назад
# nazad = telebot.types.InlineKeyboardButton(text='НАЗАД' , callback_data='back_change_employee') # Нужно добавить функционал

change_register_employee.row(first_name , last_name , father_name)
change_register_employee.row(iin , address , email_address)
change_register_employee.row(udv_number)
change_register_employee.row(udv_date)
change_register_employee.row(udv_place)
change_register_employee.row(bank_card)
change_register_employee.row(iban)
change_register_employee.row(contact_phone)
change_register_employee.row(confirm_changed_data)
# change_register_employee.row(nazad)