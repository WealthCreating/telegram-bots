from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import pandas as pd
import numpy as np

import os
from api import token


class Bot:

    def __init__(self, token, *args, **kwargs):
        self.token = token
        # Create the updater and pass in token
        self.updater = Updater(token, use_context=True)
        # Get dispatcher to register handlers
        self.dp = self.updater.dispatcher
        # On different command - answer in Telegram
        self.dp.add_handler(CommandHandler('start', self.start))

        # Log all errors
        self.dp.add_error_handler(self.error_handler)

        # Start the bot
        self.updater.start_polling()

        self.updater.idle()


    def error_handler(self, update, context):
        pass


    def start(self, update, context):
        self.update.message.reply_text('Test response')


    # Send message to user
    def message(self, username, text):
        pass


b = Bot(token)
