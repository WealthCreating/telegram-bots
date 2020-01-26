# This file successfully pulls all users from a group and saves it locally
from telethon import TelegramClient
import pandas as pd
import yaml


with open('../config.yaml') as fp:
    config = yaml.load(fp, Loader=yaml.FullLoader)


api_id = '1196118'
api_hash = 'f9524543760f8a3733bf4dce1c91cdb4'
name = 'carlfarterson'
channel = '@AllThingsTA'

client = TelegramClient('session_name', api_id, api_hash)

client.start()

# get all the users
users = [[u.id, u.first_name, u.last_name, u.username] \
         for u in client.iter_participants(channel, aggressive=True)]


df = pd.DataFrame(users, columns=['id', 'first_name', 'last_name', 'username'])
df.to_csv('../data/users/ATTA_FREE.csv', index=False)

client.disconnect()
