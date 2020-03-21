from user import User
from keyboards import *
import telebot

token = '908340142:AAHzmgZqmxWw9Qkoh7OCTzCqjjrWczLtxC4'

bot = telebot.TeleBot(token)

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


bot.polling(none_stop=True)