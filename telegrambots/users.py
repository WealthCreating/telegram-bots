# This file successfully pulls all users from a group and saves it locally
from telethon import TelegramClient
import pandas as pd
import yaml


with open('../config.yaml') as fp:
    config = yaml.load(fp, Loader=yaml.FullLoader)

config['CHANNELS'].items()


client = TelegramClient('session_name', config['API_ID'], config['API_HASH'])

client.start()

# get users for each channel
for channel_name, channel_id in config['CHANNELS'].items():

    users = [[u.id, u.first_name, u.last_name, u.username] \
             for u in client.iter_participants(channel_id, aggressive=True)]

    df = pd.DataFrame(users, columns=['id', 'first_name', 'last_name', 'username'])
    df.to_csv(f'../data/users/{channel_name}.csv', index=False)


client.disconnect()
