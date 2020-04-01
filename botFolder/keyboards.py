import telebot

# Delete employee InlineKeyboard
delete_employee_markup = telebot.types.InlineKeyboardMarkup()
delete_btn1 = telebot.types.InlineKeyboardButton(text="Удалить сотрудника", callback_data='delete')
delete_employee_markup.add(delete_btn1)

# Register employee InlineKeyboard
register_employee_markup = telebot.types.InlineKeyboardMarkup()
register_employee_correct = telebot.types.InlineKeyboardButton(text='Подтвердить',callback_data='correct_employee_data')
register_employee_incorrect = telebot.types.InlineKeyboardButton(text='Изменить данные',callback_data='incorrect_employee_data')
register_employee_markup.row(register_employee_correct, register_employee_incorrect)

# Change registered employee data
change_register_employee = telebot.types.InlineKeyboardMarkup()

first_name = telebot.types.InlineKeyboardButton(text='Имя', callback_data='change_first_name')
last_name = telebot.types.InlineKeyboardButton(text='Фамилия', callback_data='change_last_name')
father_name = telebot.types.InlineKeyboardButton(text='Отчество', callback_data='change_father_name')
birth_day = telebot.types.InlineKeyboardButton(text='Дата рождения' , callback_data="change_birth_day")
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
change_register_employee.row(birth_day)
change_register_employee.row(udv_number)
change_register_employee.row(udv_date)
change_register_employee.row(udv_place)
change_register_employee.row(bank_card)
change_register_employee.row(iban)
change_register_employee.row(contact_phone)
change_register_employee.row(confirm_changed_data)
# change_register_employee.row(nazad)


# Initial keyboards for start message
# HR branch
hr_start_message__markup = telebot.types.InlineKeyboardMarkup()
hr_start_message__take_money = telebot.types.InlineKeyboardButton(text='Получить деньги' , callback_data='hr_start_message__take_money')
hr_start_message__vopros = telebot.types.InlineKeyboardButton(text='Задать вопрос' , callback_data='hr_start_message__vopros')
hr_start_message__database = telebot.types.InlineKeyboardButton(text='База участников' , callback_data='hr_start_message__database')
hr_start_message__markup.add(hr_start_message__take_money , hr_start_message__vopros , hr_start_message__database)


# Simple employee branch
employee_start_message__markup = telebot.types.InlineKeyboardMarkup()
employee_start_message__take_money = telebot.types.InlineKeyboardButton(text='Получить деньги' , callback_data='employee_start_message__take_money')
employee_start_message__vopros = telebot.types.InlineKeyboardButton(text='Задать вопрос' , callback_data='employee_start_message__vopros')
employee_start_message__markup.add(employee_start_message__take_money , employee_start_message__vopros)


# New employee branch
new_employee_start_message__markup = telebot.types.InlineKeyboardMarkup()
new_employee_start_message__register = telebot.types.InlineKeyboardButton(text='Новый сотрудник' , callback_data='new_employee_start_message__register')
new_employee_start_message__markup.add(new_employee_start_message__register)

# HR Vopros
hr_main_vopros_markup = telebot.types.InlineKeyboardMarkup()
hr_main_vopros_markup__single = telebot.types.InlineKeyboardButton(text='Задать точный вопрос' , callback_data='hr_main_vopros_markup__single')
hr_main_vopros_markup__double = telebot.types.InlineKeyboardButton(text='Предложить 2 варианта ответа' , callback_data='hr_main_vopros_markup__double')
hr_main_vopros_markup.row(hr_main_vopros_markup__single , hr_main_vopros_markup__double)

# employee Vopros
employee_main_vopros_markup = telebot.types.InlineKeyboardMarkup()
employee_main_vopros_markup__single = telebot.types.InlineKeyboardButton(text='Задать точный вопрос' , callback_data='employee_main_vopros_markup__single')
employee_main_vopros_markup__double = telebot.types.InlineKeyboardButton(text='Предложить 2 варианта ответа' , callback_data='employee_main_vopros_markup__double')
employee_main_vopros_markup.row(employee_main_vopros_markup__single , employee_main_vopros_markup__double)

# Admin take_money
admin_take_money__markup = telebot.types.InlineKeyboardMarkup()
admin_take_money__markup__accept = telebot.types.InlineKeyboardButton(text='Удтвердить' , callback_data='admin_take_money__markup__accept')
admin_take_money__markup__decline = telebot.types.InlineKeyboardButton(text='Отклонить' , callback_data='admin_take_money__markup__decline')
admin_take_money__markup.row(admin_take_money__markup__accept,admin_take_money__markup__decline)

# Admin single_vopros
admin_single_vopros__markup = telebot.types.InlineKeyboardMarkup()
admin_single_vopros__markup__answer = telebot.types.InlineKeyboardButton(text='Ответить' , callback_data='admin_single_vopros__markup__answer')
admin_single_vopros__markup__incorrect = telebot.types.InlineKeyboardButton(text='Некорректный вопрос' , callback_data='admin_single_vopros__markup__incorrect')
admin_single_vopros__markup.row(admin_single_vopros__markup__answer , admin_single_vopros__markup__incorrect)

# Admin double vopros
admin_double_vopros__markup = telebot.types.InlineKeyboardMarkup()
admin_double_vopros__markup__first = telebot.types.InlineKeyboardButton(text='1' , callback_data='admin_double_vopros__markup__first')
admin_double_vopros__markup__double = telebot.types.InlineKeyboardButton(text='2' , callback_data='admin_double_vopros__markup__double')
admin_double_vopros__markup.row(admin_double_vopros__markup__first , admin_double_vopros__markup__double)