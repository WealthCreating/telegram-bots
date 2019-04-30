import requests
import importlib
from urllib.parse import quote_plus

def send_message(file, message):
    file = file[:file.find('.')]
    api = importlib.import_module('api.' + file)
    msg = 'https://api.telegram.org/bot' + api.key()
    msg += '/sendMessage?chat_id=' + api.chat_id()
    msg += '&text=' + quote_plus(message)
    requests.get(msg)
