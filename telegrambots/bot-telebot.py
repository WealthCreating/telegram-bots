from api import token

import telebot

import telegram.ext

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'Help is on the way!')

@bot.message_handler(commands=['start'])
def start(message):
    print(message.text)
    bot.reply_to(message, "You're a wizard, Carter!")

# Experimental
# @bot.message_handler(lambda query: '@' in query.text)
@bot.message_handler(func=lambda message: '@' in message.text)
def handle_email(message):
    print(f'This is your email: {message.text}')
    print(message)
    bot.reply_to(message, f'This is your email: {message.text}')

# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     if '@' in message.text:
#         # Show `SUCCESS`
#         print('GREAT SUCCESS')
#         bot.reply_to(message, 'GREAT SUCCESS')
#     else:
#         pass


bot.polling()


message

# TODO:  Add buttons to telebot
