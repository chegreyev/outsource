from user import User
from keyboards import *
import telebot

token = '908340142:AAHzmgZqmxWw9Qkoh7OCTzCqjjrWczLtxC4'

bot = telebot.TeleBot(token)
user = User()

@bot.message_handler(commands=['start'])
def start(message):
    if User().check_user(message.from_user.id) == 'none':
        bot.send_message(message.from_user.id ,text = 'Здравствуйте, я Aiva Bot.\nВаш помощник в компании\n-Предоставление услуг\n-Консультирование\n-Управление')
    elif User().check_user(message.from_user.id) == 'admin':
        bot.send_message(message.from_user.id ,text =  'Вы успешно зарегестрировались')

@bot.message_handler(commands=['employees'])
def bd_employees(msg):
    users = User().get_all()
    for usr in users:
        bot.send_message(msg.from_user.id , User().user_to_string(usr) , reply_markup=delete_employee_markup)

@bot.callback_query_handler(lambda clb : clb.data == 'delete')
def delete_employee(clb):
    employee_id = clb.message.text[18:27]
    User().deleteEmployee(employee_id)


    bot.delete_message(clb.message.chat.id ,
                       clb.message.message_id)

    bot.send_message(clb.message.chat.id ,
                     'Сотрудник был успешно удален')

@bot.message_handler(commands=['new_employee'])
def registerNewEmployee(m):
    bot.send_message(m.chat.id ,
                     'Мы приступаем к регистрации/введении нового сотрудника в базу данных\nВведите пожалуйста как вас зовут (ФИО)')
    bot.register_next_step_handler(m , registerName)

def registerName(m):
    user.telegram_id = m.from_user.id
    name = m.text.split(" ")
    user.last_name = name[0]
    user.first_name = name[1]
    user.father_name = name[2]
    bot.send_message(m.chat.id ,
                     f'Отлично {name[1]}, теперь введите номер ИИН')
    bot.register_next_step_handler(m ,
                                   registerIIN)

def registerIIN(m):
    user.iin = m.text
    bot.send_message(m.chat.id ,
                     'Хорошо теперь нужно будет ввести данные удовстверения, заранее подготовьте пожалуйста удовстверение\nВведите пожалуйста номер удовстверения')
    bot.register_next_step_handler(m .
                                   registerUDVnumber)

def registerUDVnumber(m):
    user.udv_number = m.text
    bot.send_message(m.chat.id,
                     'Отлично , теперь введите пожалуйста дату получения удостоверения. Например: 2000-05-19')
    bot.register_next_step_handler(m , registerUDVdate)

def registerUDVdate(m):
    user.udv_date = m.text
    bot.send_message(m.chat.id ,
                     'Теперь введите место получения удостворения. Например : МВД РК')
    bot.register_next_step_handler(m ,
                                   registerUDVplace)

def registerUDVplace(m):
    user.udv_place = m.text
    bot.send_message(m.chat.id ,
                     'Теперь введите ваше фактическое место проживания')
    bot.register_next_step_handler(m ,
                                   registerAddress)

def registerAddress(m):
    user.address = m.text
    bot.send_message( m.chat.id ,
                      'Отлично, теперь нужен номер банковской карты. Например: 5169 4971')
    bot.register_next_step_handler(m ,
                                   registerBankCard)

def registerBankCard(m):
    card_number = m.text.split(" ")
    correct_card_number = ''
    for i in card_number:
        correct_card_number += i
    user.bank_card = correct_card_number
    bot.send_message(m.chat.id ,
                     'Теперь введите данные IBAN')
    bot.register_next_step_handler(m ,
                                   registerIBAN)

def registerIBAN(m):
    user.iban = m.text
    bot.send_message(m.chat.id ,
                     'Введите данные контактные , начнем с телефона. Пример : 87022465104')
    bot.register_next_step_handler(m ,
                                   registerContactPhone)

def registerContactPhone(m):
    user.contact_phone = m.text
    bot.send_message(m.chat.id ,
                     'Осталось дело за малыи, введите адрес электроной почты. Например: mail@gmail.com')
    bot.register_next_step_handler(m,
                                   registerEmail)

def registerEmail(m):
    user.email_address = m.text
    bot.send_message(m.chat.id ,
                     user.user_to_string(),
                     reply_markup=register_employee_markup)



bot.polling(none_stop=True)
