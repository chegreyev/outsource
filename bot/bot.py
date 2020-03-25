from keyboards import *
from user import User
from settings import token

bot = telebot.TeleBot(token)
user = User()


@bot.message_handler(commands=['employees'])
def bd_employees(msg):
    users = User().get_all()
    for usr in users:
        bot.send_message(msg.chat.id,
                         User().user_to_string(usr),
                         reply_markup=delete_employee_markup)


@bot.callback_query_handler(lambda clb: clb.data == 'delete')
def delete_employee(clb):
    employee_id = clb.message.text[18:27]  # the telegram_id of the user
    User().deleteEmployee(employee_id)

    bot.delete_message(
        clb.message.chat.id,
        clb.message.message_id
    )

    bot.send_message(
        clb.message.chat.id,
        'Сотрудник был успешно удален'
    )
