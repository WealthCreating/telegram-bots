# Running the bot
from bot import Bot

from datetime import datetime, timedelta
from time import sleep


if __name__ == '__main__':

    bot = Bot()

    # Start bot for listening
    bot.updater.start_polling()
