import keys

import logging
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler

TOKEN = keys.token

# Setting up logging module, so you will know when 
# and why things don't work as expected
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)


# Commands
def start_command(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def main():

    # The Updater continuously fetches new updates from telegram and passes them on to the Dispatcher
    # Create Updater and pass it your bot's token.
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start_command)
    dispatcher.add_handler(start_handler)

    # continuously make a request to the telegram servers and get new updates from there 
    # if they exists.
    updater.start_polling()

    # Runs the bot until a termination signal is send
    updater.idle()
    

if __name__ == '__main__':
    main()