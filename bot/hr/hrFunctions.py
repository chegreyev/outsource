from bot import bot , user
from user import Vopros
from keyboards import admin_take_money__markup , hr_main_vopros_markup , admin_single_vopros__markup , admin_double_vopros__markup

vopros = Vopros()


@bot.callback_query_handler(lambda callback: callback.data == 'hr_start_message__take_money')
def hrTakeMoney(callback):
    bot.send_message(
        callback.message.chat.id,
        'Для какой цели вы бы хотели взять деньги ?'
    )
    bot.register_next_step_handler(
        callback.message,
        hrTakeMoney__aim
    )

def hrTakeMoney__aim(message):
    vopros.aim = message.text
    bot.send_message(
        message.chat.id ,
        'Какую сумму денег вы бы хотели взять ?'
    )
    bot.register_next_step_handler(
        message,
        hrTakeMoney__money
    )

def hrTakeMoney__money(message):
    vopros.money = message.text

    bot.send_message(
        message.chat.id,
        'Ваш запрос отправлен в обработку.\nОжидайте ответа'
    )

    bot.send_message(
        user.get_admin(),
        vopros._request(message.chat.id),
        reply_markup=admin_take_money__markup
    )

@bot.callback_query_handler(lambda callback: callback.data == 'hr_start_message__vopros')
def hrVoprosSingle(callback):
    bot.send_message(
        callback.message.chat.id,
        'Выберите какой тип вопроса',
        reply_markup=hr_main_vopros_markup
    )

@bot.callback_query_handler(lambda callback: callback.data == 'hr_main_vopros_markup__single')
def hrVoprosSingle_main(callback):
    bot.send_message(
        callback.message.chat.id,
        'Отлично , можете задать свой вопрос :'
    )

    bot.register_next_step_handler(
        callback.message,
        hrVoprosSingle
    )

def hrVoprosSingle(message):
    vopros.single_vopros = message.text

    bot.send_message(
        message.chat.id,
        'Ваш вопрос принят. Ожидайте ответа'
    )

    bot.send_message(
        user.get_admin(),
        vopros.singleVoprosRequest(message.chat.id),
        reply_markup=admin_single_vopros__markup
    )

@bot.callback_query_handler(lambda callback: callback.data == 'hr_main_vopros_markup__double')
def hrVoprosDouble_main(callback):
    bot.send_message(
        callback.message.chat.id,
        'Отлично , можете задать свой вопрос :'
    )

    bot.register_next_step_handler(
        callback.message,
        hrVoprosDouble
    )

def hrVoprosDouble(message):
    vopros.double_vopros = message.text

    bot.send_message(
        message.chat.id,
        'Теперь напишите Первый вариант ответа'
    )

    bot.register_next_step_handler(
        message,
        hrVoprosDouble_First
    )

def hrVoprosDouble_First(message):
    vopros.double_vopros_first = message.text

    bot.send_message(
        message.chat.id,
        'Теперь напишите Второй вариант ответа'
    )

    bot.register_next_step_handler(
        message,
        hrVoprosDouble_Double
    )

def hrVoprosDouble_Double(message):
    vopros.double_vopros_double = message.text

    bot.send_message(
        message.chat.id,
        'Ваш вопрос принят. Ожидайте ответа'
    )

    bot.send_message(
        chat_id=user.get_admin(),
        text=vopros.doubleVoprosRequest(message.chat.id),
        reply_markup=admin_double_vopros__markup
    )