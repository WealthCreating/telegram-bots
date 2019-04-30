from time import sleep
import pandas as pd
from datetime import datetime
import pytz

from telegram import telegram


url = 'https://www.omniexplorer.info/address/1NTMakcgVwQpMdGxRQnFKyb3G1FAJysSfz'

def run(chrome):
    prev_amt = pd.read_csv('telegram/data/tether.csv').iloc[0, 0]
    chrome.get(url)
    table  = chrome.load('ul[@class="result-list"]/div/div[1]')

    for row in table:
        row = row.text
        amt = row[row.find('\n') + 1:row.find('\nTether')]
        date = row[row.find('/')-1:row.find('M\n')+1]
        date = datetime.strptime(date, '%m/%d/%Y %H:%M:%S %p')
        date = pytz.timezone('UTC').localize(date, is_dst=None)
        date = datetime.strftime(date, '%m/%d/%Y %H:%M:%S %p')
        if amt == prev_amt:
            break

    message = 'ALERT: ' + str(amt) + ' USDT sent on ' + date + ' (UTC)'
    telegram.send_message(__file__, message)
    most_recent_amt = table[0].text
    most_recent_amt = most_recent_amt[most_recent_amt.find('\n') + 1:most_recent_amt.find('\nTether')]
    pd.DataFrame(data=[most_recent_amt], columns=['Tether Printed']).to_csv('data.csv',index=False)
