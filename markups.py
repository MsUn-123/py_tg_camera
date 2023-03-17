from telebot import types

def showMenu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
    btn1 = types.KeyboardButton('Take frame')
    btn2 = types.KeyboardButton('Ping')
    btn3 = types.KeyboardButton('Test menu')
    markup.add(btn1, btn2, btn3)
    return markup

def testMenu():
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard = True)
    btn1 = types.KeyboardButton('Take me back!')
    markup.add(btn1)
    return markup