import telebot
import requests
from urllib.parse import quote_plus

def send_message(key, chat_id, message):
    message = create_message(key, chat_id, message)
    requests.get(message)

def create_message(key, chat_id, message):
    message = 'https://api.telegram.org/bot' + key
    message += '/sendMessage?chat_id=' + chat_id
    message += '&text=' + message
