import telebot

hr_replykeyboard = telebot.types.ReplyKeyboardMarkup()
hr_replykeyboard_btn1 = telebot.types.KeyboardButton('Получить деньги')
hr_replykeyboard_btn2 = telebot.types.KeyboardButton('Задать вопрос')
hr_replykeyboard_btn3 = telebot.types.KeyboardButton('База участников')
hr_replykeyboard.add(hr_replykeyboard_btn1 , hr_replykeyboard_btn2 , hr_replykeyboard_btn3)


hr_replykeyboard_vopros = telebot.types.ReplyKeyboardMarkup()
hr_replykeyboard_vopros_btn1 = telebot.types.KeyboardButton('Предложить 2 варианта ответа')
hr_replykeyboard_vopros_btn2 = telebot.types.KeyboardButton('Задать точный вопрос')
hr_replykeyboard_vopros.add(hr_replykeyboard_vopros_btn1 , hr_replykeyboard_vopros_btn2)

