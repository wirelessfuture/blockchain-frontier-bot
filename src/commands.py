import os

# Setup Python Dot Env
from dotenv import load_dotenv
load_dotenv()

# Import telegram modules
from telegram import Update
from telegram.ext import CallbackContext

# Import parsers
from parsers import (
    market_data_parser,
    eth_gas_price_parser
)

# Import the coingecko functions
from coingecko import (
    get_trending_search, 
    get_market_data,
    get_gigachad_prices
)

# Import the defipulse functions
from defipulse import (
    get_eth_gas_prices,
    get_defi_pulse_data
)

# Import Coin Search
from search import search


# Only allow whitelisted groups to use command
def on_message(func: any) -> any:
    """When a message comes in, make sure chat_id is in whitelist."""
    whitelisted_group = [int(os.getenv("TELEGRAM_GROUP_CHAT_ID")), int(os.getenv("TELEGRAM_BOT_CHAT_ID"))] # Hard-coded for now
    def is_whitelisted(*args, **kwargs):
        if args[0].message.chat_id in whitelisted_group:
            return func(args[0], args[1])
        else:
            print(args[0].message.chat_id, " not in whitelist!")
    return is_whitelisted

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
@on_message
def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        '/price <search-term> - Get the latest market data for the search result\n'\
        '/gigachad - Gigachad R&D\n'\
        '/trending - Latest trending searches\n'\
    )

@on_message
def price_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /price is issued."""
    try:
        search_term = search(str(context.args[0]))
        new_market_data = get_market_data(search_term)["market_data"]
        if "error" not in new_market_data:
            # Parse the market data
            market_data = market_data_parser(new_market_data, search_term.upper())
            # Send reply messages
            update.message.reply_text(text=f''.join(market_data))
        else:
            update.message.reply_text(new_market_data["error"])
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /price <search-term>')
    except (KeyError):
        update.message.reply_text('I am sorry, I could not find that. 🤷‍♂️')

@on_message
def eth_gas_command(update: Update, context: CallbackContext) -> None:
    """Sends a message when the command /ethgas is issued."""
    new_gas_data = get_eth_gas_prices()
    gas_data = eth_gas_price_parser(new_gas_data)
    update.message.reply_text(text=f''.join(gas_data))

@on_message
def gigachad_command(update: Update, context: CallbackContext) -> None:
    """Sends a message when the command /gigachad is issued."""
    new_gigachad = get_gigachad_prices()
    if "error" not in new_gigachad:
        tokens = [token + ': $' + str(price['usd']) + '\n' for token, price in new_gigachad.items()]
        tokens.insert(0, "Gigachad Research Prices:\n")
        update.message.reply_text(f''.join(tokens))
    else:
        update.message.reply_text(new_gigachad["error"])

@on_message
def trending_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /trending is issued."""
    new_trending = get_trending_search()
    if "error" not in new_trending:
        tokens = [token["item"]["name"] + "\n" for token in new_trending["coins"]]
        tokens.insert(0, "Top 7 Searches on Coingecko:\n")
        update.message.reply_text(f''.join(tokens))
    else:
        update.message.reply_text(new_trending["error"])