from user import User
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
        bot.send_message(msg.from_user.id , User().user_to_string(usr))

bot.polling(none_stop=True)