from wrappers import restricted

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
        self.configure()

        # Create bot instance
        self.updater = Updater(self.config['token'], user_context=True)
        self.manager = self.updater.dispatcher

        # TODO: add basic commands
        self.add_command()

        # TODO: add message handlers
        self.add_message_handler()

        # TODO: log all errors
        self.add_error_handler()



    def configure(self, *args, **kwargs):

        # load config file
        my_file = Path(self.config_file)

        # Check if config file exists
        if my_file.is_file():
            with open(config_file) as fp:
                self.config = yaml.load(fp, Loader=yaml.FullLoader)
        else:
            pprint('config.yaml file does not exist.  Please make from config.sample.yaml file')
            sys.exit()


    # Command to start bot for listening
    def start(self):
        self.manager.start_polling()


    # Add commands to bot
    def add_command(self, command_str=None, command_fn=None):
        self.manager.add_handler(CommandHandler(command_str, command_fn))


    # TODO: add message handlers to bot
    def add_message_handler(self, *args, **kwargs):
        pass

    def add_error_handler(self, *args, **kwargs):
        pass
