from api import token
import telebot
import pandas as pd
import time


users = pd.read_csv('../data/users.csv')


# Create bot
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'Help is on the way!')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Spinning up bot...")
    # Wait a few seconds to pretend the bot is starting


def validate(message):
    users = pd.read_csv('../data/users.csv')
    if
    # TODO: validate username in users

@bot.message_handler(func=lambda m: '@' in m.text)
def handle_email(message):
    print(type(message))
    validate(message)
    bot.reply_to(message, f'This is your email: {message.text}')




# TODO: add buttons

bot.polling()
