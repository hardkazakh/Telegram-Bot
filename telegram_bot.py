import telebot
from telebot import types

bot = telebot.TeleBot('1013724910:AAFaXtOdtmfuPfI0gABIeLZB38Gg3GMCmMc')

@bot.message_handler(commands=["start"])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True,False)
    keyboard.row("yes", "no")
    send = bot.send_message(message.chat.id, 'Hi, I am TELEGRAM BOT. Do you want a new phone?', reply_markup=keyboard)
    bot.register_next_step_handler(send, send_company)

def send_company(message):
    if message.text.lower() == 'yes':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('apple', 'samsung', 'huawei')
        send = bot.send_message(message.chat.id, 'Enter company: ', reply_markup=keyboard)
        bot.register_next_step_handler(send, send_phone)
    elif message.text.lower() == 'no':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('/start')
        bot.send_message(message.chat.id, 'We are an online phone shop.If you want to buy a phone. Enter </start>', reply_markup=keyboard)

def send_phone(message):
    if message.text.lower() == 'apple':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('iphone 11 pro', 'iphone xs max', 'iphone 8')
        send = bot.send_message(message.chat.id, 'Enter the type of phone:', reply_markup=keyboard)
        bot.register_next_step_handler(send, send_opinion)
    elif message.text.lower() == 'samsung':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('galaxy fold', 'galaxy z flip', 'galaxy s20 ultra')
        send = bot.send_message(message.chat.id, 'Enter the type of phone:', reply_markup=keyboard)
        bot.register_next_step_handler(send, send_opinion) 
    elif message.text.lower() == 'huawei':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('Mate 30 Pro', 'P30 Pro', 'Mate 20 Pro')
        send = bot.send_message(message.chat.id, 'Enter the type of phone:', reply_markup=keyboard)
        bot.register_next_step_handler(send, send_opinion)
        
def send_opinion(message):
    if message.text.lower() == 'iphone 11 pro':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('i want buy', 'i do not know')
        send = bot.send_message(message.chat.id, 'OS: iOS 13 \nDiagonal: 5.8 \nRAM: 6 GB \nMemory: 512 GB \nPrice: 779 999T \nEnter your opinion: \nhttps://tlgur.com/d/4zZeKO34', reply_markup=keyboard)
        bot.register_next_step_handler(send, send_money)
    elif message.text.lower() == 'iphone xs max':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('i want buy', 'i do not know')
        send = bot.send_message(message.chat.id, 'OS: iOS 12 \nDiagonal: 6.5 \nRAM: 6 GB \nMemory: 512 GB \nPrice: 698 000T \nEnter your opinion: \nhttps://tlgur.com/d/8KoXvke8', reply_markup=keyboard)
        bot.register_next_step_handler(send, send_money)
    elif message.text.lower() == 'iphone 8':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('i want buy', 'i do not know')
        send = bot.send_message(message.chat.id, 'OS: iOS 11 \nDiagonal: 4.7 \nRAM: 2 GB \nMemory: 256 GB \nPrice: 490 000T \nEnter your opinion: \nhttps://tlgur.com/d/g3v0DzZG', reply_markup=keyboard)
        bot.register_next_step_handler(send, send_money) 
    elif message.text.lower() == 'galaxy fold':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('i want buy', 'i do not know')
        send=bot.send_message(message.chat.id, 'OS: Android 9.0 \nDiagonal: 4.6 \nRAM: 12GB \nMemory: 512GB \nPrice: 900 000T \nEnter your opinion: \nhttps://tlgur.com/d/GJavZxx8', reply_markup=keyboard)
        bot.register_next_step_handler(send, send_money) 
    elif message.text.lower() == 'galaxy z flip':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('i want buy', 'i do not know')
        send = bot.send_message(message.chat.id,'OS: Android 10 \nDiagonal: 6.7 \nRAM: 8 GB \nMemory: 256GB \nPrice: 598 690T \nEnter your opinion: \nhttps://tlgur.com/d/4RameVeg', reply_markup=keyboard)
        bot.register_next_step_handler(send, send_money) 
    elif message.text.lower() == 'galaxy s20 ultra':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('i want buy', 'i do not know')
        send = bot.send_message(message.chat.id,'OS: Android 10 \nDiagonal: 6.9 \nRAM: 12GB \nMemory: 128GB \nPrice: 495 290T \nEnter your opinion: \nhttps://tlgur.com/d/4RameVeg', reply_markup=keyboard)
        bot.register_next_step_handler(send, send_money) 
    elif message.text.lower() == 'mate 30 pro':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('i want buy', 'i do not know')
        send = bot.send_message(message.chat.id,'OS: Android 10 \nDiagonal: 6.5, \nRAM: 8 GB \nMemory: 256GB \nPrice: 499 890T \nEnter your opinion: \nhttps://tlgur.com/d/8QeqB7K8', reply_markup=keyboard)
        bot.register_next_step_handler(send, send_money)
    elif message.text.lower() == 'p30 pro':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('i want buy', 'i do not know')
        send= bot.send_message(message.chat.id,'OS: Android 9.0 \nDiagonal: 6.5 \nRAM: 8 GB \nMemory: 256GB \nPrice: 345 500T \nEnter your opinion: \nhttps://tlgur.com/d/GLr0X5B4', reply_markup=keyboard)
        bot.register_next_step_handler(send, send_money)
    elif message.text.lower() == 'mate 20 pro':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('i want buy', 'i do not know')
        send= bot.send_message(message.chat.id,'OS: Android 9.0 \nDiagonal: 6.5 \nRAM: 4 GB \nMemory: 128GB \nPrice: 259 290T \nEnter your opinion: \nhttps://tlgur.com/d/81ev7zl8 ', reply_markup=keyboard)
        bot.register_next_step_handler(send, send_money)

def send_money(message):
    if message.text.lower() == 'i want buy':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('i sent money. i am waiting for my order', '/start')
        send=bot.send_message(message.chat.id, 'OK. You send this money to KASPI GOLD: 87081234567. We will deliver your order within 3 days', reply_markup=keyboard)
        bot.register_next_step_handler(send, send_thanks)
        
    elif message.text.lower() == 'i do not know':
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('/start')
        bot.send_message(message.chat.id, 'OK. If you change your mind, you can order by clicking the /start button', reply_markup=keyboard)

def send_thanks(message):
    if message.text.lower() == 'i sent money. i am waiting for my order':     
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('/start')      
        bot.send_message(message.chat.id, 'Thank you for your purchase', reply_markup=keyboard)

bot.polling()       
