import requests
import importlib
from urllib.parse import quote_plus


def send_message(file, message):
    filename = file.split('/')[-1]
    botname = filename[:filename.find('.')]
    api = importlib.import_module('telegram.api.' + botname)
    msg = 'https://api.telegram.org/bot' + api.key()
    msg += '/sendMessage?chat_id=' + api.chat_id()
    msg += '&text=' + quote_plus(message)
    requests.get(msg)
