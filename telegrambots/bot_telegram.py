from api import token
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)



# Version 1
def start(update, context):
    sub_lifetime = InlineKeyboardButton("Lifetime", callback_data='4')
    sub_one_year = InlineKeyboardButton("1 year", callback_data='3')
    sub_six_months = InlineKeyboardButton("6 months", callback_data='2')
    sub_three_months = InlineKeyboardButton("3 months", callback_data='1')
    keyboard = [
        [sub_lifetime, sub_one_year],
        [sub_six_months, sub_three_months]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('How long of a subscription period do you want?', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    query.edit_message_text(text=f'Selected option: {query.data}')


def help(update, context):
    update.message.reply_text('Use `/start` to test this bot')


def error(update, context):
    logger.warning(f'Update "{update}" caused error "{context.error}"')


def main():

    updater = Updater(token, use_context=True)

    # Add commands
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))

    # Add error handler
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # Start bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives `SIGINT`,
    # `SIGTERM` or `SIGABRT`
    updater.idle()



# Run file
if __name__ == '__main__':
    main()





# ------------------------------------------------------------------------------
# Version 2

# bot = telegram.Bot(token=bot_token)
# chat_id = bot.get_updates()[-1].message.chat_id
# bot.send_message(chat_id=chat_id, text='Right back at ya')
