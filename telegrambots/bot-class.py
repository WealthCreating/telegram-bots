from api import token
import telebot
import pandas as pd

# TODO: Replicate the scrollable window


class Bot:

    def __init__(self, token):

        # Create bot instance
        self.bot = telebot.Telebot(token)

        # add basic commands
        self.command()
