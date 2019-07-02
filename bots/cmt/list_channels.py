from bots.cmt.api import token, channel_url
import telebot


def main():

    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['list_channels'])
    def run_bot(message):
        bot.reply_to(message, channel_url)

    bot.polling()



if __name__ == '__main__':
    main()
