import keys

import logging
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler

TOKEN = keys.token

# Setting up logging module, so you will know when 
# and why things don't work as expected
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Commands
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    context.bot.send_message(chat_id=update.effective_chat.id, text="yes!")

def help_command(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                            text="Commands:"
                                 "\n/start -- Starts the bot"
                                 "\n/mybday [dd.mm.yyyy] -- Saves the user birthday"
                                 "\n/next -- Shows the next birthday"
                                 "\n/dates -- Shows the birthdays list"                                
                                 "\n/help -- Shows the commands")


def main():
    """Start the bot."""
    # The Updater continuously fetches new updates from telegram and passes them on to the Dispatcher
    # Create Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # On different commands - answer in Telegram
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    help_handler = CommandHandler('help', help_command)
    dispatcher.add_handler(help_handler)

    # Continuously make a request to the telegram servers and get new updates from there 
    # if they exists.
    updater.start_polling()

    # Runs the bot until a termination signal is send
    updater.idle()
    

if __name__ == '__main__':
    main()