# Testing out random shit

# 2020.01.16
# Run something similar to echobot2.py from python-telegram-bot
import telegram
from variables import token


bot = telegram.Bot(token=token)

print(bot.get_me())
