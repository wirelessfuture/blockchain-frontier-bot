import logging
import os

from telegram import Update
from telegram.ext import (
    Updater, 
    CommandHandler, 
    MessageHandler, 
    Filters, 
    CallbackContext
)

# Setup Python Dot Env
from dotenv import load_dotenv
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Import the price checker
from coingecko import get_eth_price, get_trending_search, get_percentage_data


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'Use the command /price to check the price of Eth!\n'\
        'Use the command /trending to get the latest trending searches on Coingecko!\n'\
        'Use the command /percentage to get Eth price percentage data!\n'\
    )

def price_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /price is issued."""
    new_price = get_eth_price()
    if "error" not in new_price:
        usd = new_price["ethereum"]["usd"]
        gbp = new_price["ethereum"]["gbp"]
        czk = new_price["ethereum"]["czk"]
        aud = new_price["ethereum"]["aud"]
        update.message.reply_text(f'Eth USD: ${usd}\nEth GBP: £{gbp}\nEth CZK: {czk}Kč\nEth AUD: ${aud}')
    else:
        update.message.reply_text(new_price["error"])

def trending_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /trending is issued."""
    new_trending = get_trending_search()
    if "error" not in new_trending:
        tokens = [token["item"]["name"] + "\n" for token in new_trending["coins"]]
        tokens.insert(0, "Top 7 Searches on Coingecko:\n")
        update.message.reply_text(f''.join(tokens))
    else:
        update.message.reply_text(new_trending["error"])

def percentage_command(update: Update, context: CallbackContext) -> None:
    """Sends a message when the command /percentage is issued."""
    new_percentage = get_percentage_data()
    if "error" not in new_percentage:
        market_data = new_percentage["market_data"]
        price_change_24h = market_data["price_change_percentage_24h"]
        price_change_7d = market_data["price_change_percentage_7d"]
        price_change_14d = market_data["price_change_percentage_14d"]
        price_change_30d = market_data["price_change_percentage_30d"]
        price_change_60d = market_data["price_change_percentage_60d"]
        price_change_200d = market_data["price_change_percentage_200d"]
        price_change_1y = market_data["price_change_percentage_1y"]
        update.message.reply_text(
            f'Eth Price Change:\n'\
            f'24h:  {price_change_24h}%\n'\
            f'7d:  {price_change_7d}%\n'\
            f'14d:  {price_change_14d}%\n'\
            f'30d:  {price_change_30d}%\n'\
            f'60d:  {price_change_60d}%\n'\
            f'200d:  {price_change_200d}%\n'\
            f'1y:  {price_change_1y}%\n'\
        )
    else:
        update.message.reply_text(new_percentage["error"])

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.getenv("BOT_TOKEN"))

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("price", price_command))
    dispatcher.add_handler(CommandHandler("trending", trending_command))
    dispatcher.add_handler(CommandHandler("percentage", percentage_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()