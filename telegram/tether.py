from datetime import datetime
import pandas as pd
import pytz
from telegram import telegram, chrome


url = 'https://www.omniexplorer.info/address/1NTMakcgVwQpMdGxRQnFKyb3G1FAJysSfz'

def find_amt_date(element):
    row = element.text.split('\n')
    amt = row[1]
    date = row[4]
    date = datetime.strptime(date, '%m/%d/%Y %H:%M:%S %p')
    utc_date = pytz.timezone('UTC').localize(date, is_dst=None)
    utc_date_str = datetime.strftime(date, '%m/%d/%Y %H:%M:%S %p') + ' (UTC)'
    return amt, utc_date_str

def run(chrome):
    prev_amt = pd.read_csv('telegram/data/tether.csv').iloc[0, 0]
    chrome.get(url)
    table  = chrome.load('ul[@class="result-list"]/div/div[1]')

    for element in table:
        amt, date = find_amt_date(element)
        if amt == prev_amt:
            break

    message = 'ALERT: ' + str(amt) + ' USDT sent on ' + date
    telegram.send_message(__file__, message)
    most_recent_amt, _ = find_amt_date(table[0])
    pd.DataFrame(data=[most_recent_amt], columns=['Tether Printed']).to_csv('data.csv',index=False)
