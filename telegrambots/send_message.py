# Send private message to a user
# NOTE: Bots are not able to initiate direct messages. Only human accounts can.

from telethon import TelegramClient
import pandas as pd
import yaml


with open('../config.yaml') as fp:
    config = yaml.load(fp, Loader=yaml.FullLoader)


# Send messages from @carlfarterson
client = TelegramClient('session_name', config['API_ID'], config['API_HASH'])

async def main():

    await client.send_message('CriptoAZ', 'test')
    await client.send_message(373647236, 'test')

with client:
    client.loop.run_until_complete(main())


# Another version of the same shit above
# bot = TelegramClient('session_name', config['API_ID'], config['API_HASH']).start(bot_token=config['TOKEN'])
#
# async def main():
#     await bot.send_message('CriptoAZ', 'usename test')
#     await bot.send_message(373647236, 'user_id test')
#
#
# bot.loop.run_until_complete(main())
