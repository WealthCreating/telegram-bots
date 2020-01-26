# This file successfully pulls all users from a group and saves it locally
from telethon import TelegramClient
import pandas as pd
import yaml


with open('../config.yaml') as fp:
    config = yaml.load(fp, Loader=yaml.FullLoader)


client = TelegramClient('session_name', config['API_ID'], config['API_HASH'])


# Send message
async def main():
    await client.send_message('aswlee', 'test')


with client:
    client.loop.run_until_complete(main())
