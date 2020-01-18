from api import token
import telebot
import pandas as pd



class Bot(telebot.Telebot):

    def __init__(self, token):

        # Create bot instance
        super().__init__(token)

        # add basic commands
        self.command()



if __name__ == '__main__':

    bot = Bot(token)
