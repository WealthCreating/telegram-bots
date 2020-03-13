from telegram.ext import CommandHandler
from pprint import pprint


class Commands:

    def __init__(self, *args, **kwargs):

        # Add commands
        self.add_command('start')


    def add_command(self, fn_str):
        fn = getattr(self, fn_str)
        self.manager.add_handler(CommandHandler(fn_str, fn))


    def start(self, update, context):

        msg = self.config['MESSAGES']['start']
        user_data = update.message.from_user.__dict__

        update.message.reply_text(msg.format(**user_data))
