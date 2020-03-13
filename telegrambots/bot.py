# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Transition-guide-to-Version-12.0

from wrappers import restricted
from commands import Commands
from log import *

import sys
import yaml
import pathlib

import pandas as pd

from pprint import pprint
from telegram.ext import Updater



class Bot(Commands):

    def __init__(self, config_file='../config.yaml', *args, **kwargs):

        # Configure bot settings
        self.configure(config_file)

        # Create bot instance
        self.updater = Updater(self.config['TOKEN'], use_context=True)
        self.manager = self.updater.dispatcher

        # TODO: add basic commands
        super().__init__(self)

        # TODO: add message handlers
        self.add_message_handler()


    def configure(self, config_file, *args, **kwargs):

        # load config file
        my_file = pathlib.Path(config_file)

        # Check if config file exists
        if my_file.is_file():
            with open(config_file) as fp:
                self.config = yaml.load(fp, Loader=yaml.FullLoader)
        else:
            raise FileNotFoundError('config.yaml file does not exist.  Please make from config.sample.yaml file')

        # Log all errors and add error handler
        self.logger = logging.getLogger(__name__)
        # self.manager.add_handler(CallbackQueryHandler())


    # TODO: add message handlers to bot
    def add_message_handler(self, *args, **kwargs):
        pass


    def add_error_handler(self, *args, **kwargs):
        logger.warning(f'Update "{update}" caused error "{context.error}"')
