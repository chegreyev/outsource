from keyboards import delete_employee_markup
from user import User

from bot import bot

@bot.callback_query_handler(lambda callback: callback.data == 'hr_start_message__database')
def bd_employees(callback):
    users = User().get_all()
    for usr in users:

        if usr['is_admin'] == True or usr['is_hr'] == True:
            continue

        bot.send_message(
            callback.message.chat.id,
            User().user_to_string(usr),
            reply_markup=delete_employee_markup
        )


@bot.callback_query_handler(lambda clb: clb.data == 'delete')
def delete_employee(clb):
    employee_id = clb.message.text[18:27]
    User().deleteEmployee(employee_id)

    bot.delete_message(
        clb.message.chat.id,
        clb.message.message_id
    )

    bot.send_message(
        clb.message.chat.id,
        'Сотрудник был успешно удален'
    )
