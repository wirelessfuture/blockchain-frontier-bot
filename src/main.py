# Import Python Modules
import logging
import os

# Import telegram modules
from telegram.ext import (
    Updater, 
    CommandHandler
)

# Setup Python Dot Env
from dotenv import load_dotenv
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Import the command handlers
from commands import (
    help_command,
    price_command,
    eth_gas_command,
    trending_command,
    gigachad_command,
)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.getenv("TELEGRAM_BOT_TOKEN"))

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("price", price_command))
    dispatcher.add_handler(CommandHandler("ethgas", eth_gas_command))
    dispatcher.add_handler(CommandHandler("trending", trending_command))
    dispatcher.add_handler(CommandHandler("gigachad", gigachad_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()