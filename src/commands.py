# Import telegram modules
from telegram import Update
from telegram.ext import CallbackContext

# Import the price checker
from coingecko import (
    get_trending_search, 
    get_eth_price, 
    get_eth_percentage_change,
    get_btc_price,
    get_btc_percentage_change,
    get_gigachad_prices
)

# Import our entities
from entities import (
    PriceDict,
    PercentageDict
)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        '/trending to get the latest trending searches\n'\
        '/ethprice to check the price of ETH\n'\
        '/ethpercentage to get ETH price percentage data\n'\
        '/btcprice to check the price of BTC\n'\
        '/btcpercentage to get BTC price percentage data\n'\
        '/gigachad to get prices of the Gigachad list\n'\
    )

def trending_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /trending is issued."""
    new_trending = get_trending_search()
    if "error" not in new_trending:
        tokens = [token["item"]["name"] + "\n" for token in new_trending["coins"]]
        tokens.insert(0, "Top 7 Searches on Coingecko:\n")
        update.message.reply_text(f''.join(tokens))
    else:
        update.message.reply_text(new_trending["error"])

def eth_price_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /ethprice is issued."""
    new_price = get_eth_price()
    if "error" not in new_price:
        prices = [f'ETH {currency}: {price} \n' for currency, price in new_price["ethereum"].items()]
        update.message.reply_text(''.join(prices))
    else:
        update.message.reply_text(new_price["error"])

def eth_percentage_command(update: Update, context: CallbackContext) -> None:
    """Sends a message when the command /percentage is issued."""
    new_percentage = get_eth_percentage_change()
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
            f'ETH Price Change:\n'\
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

def btc_price_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /btcprice is issued."""
    new_price = get_btc_price()
    if "error" not in new_price:
        prices = [f'BTC {currency}: {price} \n' for currency, price in new_price["bitcoin"].items()]
        update.message.reply_text(''.join(prices))
    else:
        update.message.reply_text(new_price["error"])

def btc_percentage_command(update: Update, context: CallbackContext) -> None:
    """Sends a message when the command /btcpercentage is issued."""
    new_percentage = get_btc_percentage_change()
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
            f'BTC Price Change:\n'\
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

def gigachad_command(update: Update, context: CallbackContext) -> None:
    """Sends a message when the command /gigachad is issued."""
    new_gigachad = get_gigachad_prices()
    if "error" not in new_gigachad:
        tokens = [token + ': $' + str(price['usd']) + '\n' for token, price in new_gigachad.items()]
        tokens.insert(0, "Gigachad Research Prices:\n")
        update.message.reply_text(f''.join(tokens))
    else:
        update.message.reply_text(new_percentage["error"])