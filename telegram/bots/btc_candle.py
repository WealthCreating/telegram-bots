# Exchanges:  bitfinex, bitstamp, bitmex
# Time frame: 1 min before utc 00:00:00, then @ 00:00:00
import ccxt
from telegram import telegram
from datetime import datetime

exchanges = ['bitstamp', 'bitfinex', 'bitmex']


def run(date):
    utc_date_str = datetime.strftime(date, '%m/%d/%Y %H:%M:%S %p (UTC)')
    message = utc_date_str + '\n'
    for exchange in exchanges:
        api = getattr(ccxt, exchange)()
        last_price = round(api.fetch_ticker(symbol='BTC/USD')['last'], 2)
        message += exchange.capitalize() + ': $' + str(last_price) + '\n'

    telegram.send_message(file=__file__, message=message)
