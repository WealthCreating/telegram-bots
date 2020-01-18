import sys
import yaml
import pathlib

import pandas as pd

from pprint import pprint
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


class Bot:

    self.config_file = '../config.yaml'

    def __init__(self):

        # Configure bot settings
        self._config()

        # Create bot instance
        self.manager = Updater(self.config['token'], user_context=True)

        # add basic commands
        self.add_command()


    def _config(self, *args, **kwargs):

        # load config file
        my_file = Path(self.config_file)

        # Check if config file exists
        if my_file.is_file():
            with open(config_file) as fp:
                self.config = yaml.load(fp)
        else:
            pprint('config.yaml file does not exist.  Please make from config.sample.yaml file')
            sys.exit()


    # Wrapper to restrict bot functions to admins
    def restricted(fn):
        def wrapper(bot, update, *args, **kwargs):
            user_id = update.effective_user.id
            if user_id not in self.config['ADMINS']:
                # TODO: send message that user is not permitted
                print(f'Unauthorized access denied for {user_id}')
                return
            return fn(bot, update, *args, **kwargs)
        return wrapper


    # Command to start bot for listening
    def start(self):
        self.manager.start_polling()


    # Add commands to bot
    def add_command(self, command=None):
        pass
