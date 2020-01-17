# Testing out random shit

# 2020.01.16
# Run something similar to echobot2.py from python-telegram-bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from api import token


bot = telegram.Bot(token=token)

print(bot.get_me())
# Create the Updater and pass the bots' toen
updater = Updater(token, use_context=True)

# Get the dispatcher to register handlers
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
