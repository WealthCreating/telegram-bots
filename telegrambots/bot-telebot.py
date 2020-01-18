from api import token

import telebot

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.reply_to(message, 'Telebot is running the show')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message.text)
    bot.reply_to(message, message.text)

bot.polling()
