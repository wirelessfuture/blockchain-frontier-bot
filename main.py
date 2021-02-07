import logging
import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Setup Python Dot Env
from dotenv import load_dotenv
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Import the price checker
from price import get_eth_price


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Use the command /price to check the price of Eth!')


def price_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /price is issued."""
    new_price = get_eth_price()
    usd = new_price["ethereum"]["usd"]
    gbp = new_price["ethereum"]["gbp"]
    czk = new_price["ethereum"]["czk"]
    aud = new_price["ethereum"]["aud"]
    update.message.reply_text(f'Eth USD: ${usd}\nEth GBP: £{gbp}\nEth CZK: {czk}Kč\nEth AUD: ${aud}')


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.getenv("BOT_TOKEN"))

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("price", price_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()