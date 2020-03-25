from telebot import TeleBot

from user import User
from settings import token

from bot import bot
import hr.registerEmployee
import hr.changeRegisterEmployee


@bot.message_handler(commands=['start'])
def start(message):
    if User().check_user(message.from_user.id) == 'none':
        bot.send_message(message.chat.id,
                         text='Здравствуйте, я Aiva Bot.\nВаш помощник в компании\n-Предоставление услуг\n-Консультирование\n-Управление')
    elif User().check_user(message.from_user.id) == 'admin':
        bot.send_message(message.chat.id, text='Вы успешно зарегестрировались')


bot.polling(none_stop=True)