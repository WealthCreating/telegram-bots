import logging
from bots.cmt.api import TOKEN
from telegram import Bot
from telegram.ext import Updater, CommandHandler, InlineQueryHandler

bot = Bot(token=TOKEN)



# ------------------------------------------------------------------------------



# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def inlinequery(update, context):
    query = update.inline_query.query
    results = []
    update.inline_query.answer(results)



def main():
    # Create Updater with token
    updater = Updater(TOKEN, use_context=True)

    # Get dispatcher to register handlers
    dp = updater.dispatcher

    # Start bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
