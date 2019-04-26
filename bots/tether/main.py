import os
import telebot
import requests
import pandas as pd
from urllib.parse import quote_plus
from selenium import webdriver
from time import sleep
from api import key
from datetime import datetime
import pytz



url = 'https://www.omniexplorer.info/address/1NTMakcgVwQpMdGxRQnFKyb3G1FAJysSfz'
message = 'https://api.telegram.org/bot' + key + '/sendMessage?chat_id=@cryptoinsiderslobby&text='
# message2 = 'https://api.telegram.org/bot' + key + '/sendMessage?chat_id=DAtQmE5wjmzmFFoSFvdbrw&text='
#
# requests.get(message + quote_plus("jk "))
# https://api.telegram.org/bot665412175:AAF6L_z7YPkb9RwTMjpvNubQelzOMXG6VF0/sendMessage?chat_id=s1315999340_17611182089278269709&text=What%27s+up+bitches

options = webdriver.ChromeOptions()
options.add_argument('headless')

while True:
    web = webdriver.Chrome(os.getcwd() + '/chromedriver', options=options)
    web.get(url)
    sleep(90)

    prev_amt = pd.read_csv('data.csv').iloc[0, 0]
    table  = web.find_elements_by_xpath('//ul[@class="result-list"]/div/div[1]')
    for row in table:
        row = row.text
        amt = row[row.find('\n') + 1:row.find('\nTether')]
        date = row[row.find('/')-1:row.find('M\n')+1]
        date = datetime.strptime(date, '%m/%d/%Y %H:%M:%S %p')
        date = pytz.timezone('UTC').localize(date, is_dst=None)
        date = datetime.strftime(date, '%m/%d/%Y %H:%M:%S %p')
        if amt == prev_amt:
            break

        alert = 'ALERT: ' + str(amt) + ' USDT sent on ' + date + ' (UTC)'
        requests.get(message + quote_plus(alert))

    most_recent_amt = table[0].text
    most_recent_amt = most_recent_amt[most_recent_amt.find('\n') + 1:most_recent_amt.find('\nTether')]
    pd.DataFrame(data=[most_recent_amt], columns=['Tether Printed']).to_csv('data.csv',index=False)
    web.close()
