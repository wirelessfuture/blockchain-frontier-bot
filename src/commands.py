# Import telegram modules
from telegram import Update
from telegram.ext import CallbackContext

# Import the coingecko functions
from coingecko import (
    get_trending_search, 
    get_eth_price, 
    get_eth_percentage_change,
    get_btc_price,
    get_btc_percentage_change,
    get_gigachad_prices,
    get_ada_price
)

# Import the defipulse functions
from defipulse import (
    get_eth_gas_prices,
    get_defi_pulse_data
)

# Import our entities
from entities import (
    PriceDict,
    PercentageDict
)


# Only allow whitelisted groups to use command
def on_message(func: any) -> any:
    """When a message comes in, make sure chat_id is in whitelist."""
    whitelisted_group = -1001268910811 # Hard-coded for now
    def is_whitelisted(*args, **kwargs):
        if args[0].message.chat_id == whitelisted_group:
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
        '/ethgas - Gets the current gas prices\n'\
        '/defipulse - Gets the current TVL in DeFi\n'\
        '/trending - Latest trending searches\n'\
        '/ethprice - Price of ETH\n'\
        '/ethpercentage - ETH price change %\n'\
        '/btcprice - Price of BTC\n'\
        '/btcpercentage - BTC price change %\n'\
        '/gigachad - Gigachad R&D\n'\
        '/adaprice - Price of ADA\n'\
    )

@on_message
def eth_gas_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /ethgas is issued."""
    price_keys = [
        "average",
        "fast",
        "fastest"
    ]
    new_gas_prices = get_eth_gas_prices()
    prices = [f'{key}: {value} GWEI\n' for key, value in new_gas_prices.items() if key in price_keys]
    prices.insert(0, 'ETH Gas Prices\n')
    update.message.reply_text(''.join(prices))

@on_message
def defipulse_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /defipulse is issued."""
    defipulse_data = get_defi_pulse_data()
    tvl = defipulse_data["All"]["total"]
    update.message.reply_text("Total Value Locked in Ethereum DeFi:\n${:,} USD".format(tvl))

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

@on_message
def eth_price_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /ethprice is issued."""
    new_price = get_eth_price()
    if "error" not in new_price:
        prices = [f'ETH {currency}: {price} \n' for currency, price in new_price["ethereum"].items()]
        update.message.reply_text(''.join(prices))
    else:
        update.message.reply_text(new_price["error"])

@on_message
def eth_percentage_command(update: Update, context: CallbackContext) -> None:
    """Sends a message when the command /percentage is issued."""
    percentage_keys = [
        "price_change_percentage_24h",
        "price_change_percentage_7d",
        "price_change_percentage_14d",
        "price_change_percentage_30d",
        "price_change_percentage_60d",
        "price_change_percentage_200d",
        "price_change_percentage_1y",
    ]
    new_percentage = get_eth_percentage_change()
    if "error" not in new_percentage:
        percentages = [f'{key.split("_")[-1]}: {value}%\n' for key, value in new_percentage["market_data"].items() if key in percentage_keys]
        percentages.insert(0, 'ETH Price Change %\n')
        update.message.reply_text(''.join(percentages))
    else:
        update.message.reply_text(new_percentage["error"])

@on_message
def btc_price_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /btcprice is issued."""
    new_price = get_btc_price()
    if "error" not in new_price:
        prices = [f'BTC {currency}: {price} \n' for currency, price in new_price["bitcoin"].items()]
        update.message.reply_text(''.join(prices))
    else:
        update.message.reply_text(new_price["error"])

@on_message
def btc_percentage_command(update: Update, context: CallbackContext) -> None:
    """Sends a message when the command /btcpercentage is issued."""
    percentage_keys = [
        "price_change_percentage_24h",
        "price_change_percentage_7d",
        "price_change_percentage_14d",
        "price_change_percentage_30d",
        "price_change_percentage_60d",
        "price_change_percentage_200d",
        "price_change_percentage_1y",
    ]
    new_percentage = get_btc_percentage_change()
    if "error" not in new_percentage:
        percentages = [f'{key.split("_")[-1]}: {value}%\n' for key, value in new_percentage["market_data"].items() if key in percentage_keys]
        percentages.insert(0, 'BTC Price Change %\n')
        update.message.reply_text(''.join(percentages))
    else:
        update.message.reply_text(new_percentage["error"])

@on_message
def gigachad_command(update: Update, context: CallbackContext) -> None:
    """Sends a message when the command /gigachad is issued."""
    new_gigachad = get_gigachad_prices()
    if "error" not in new_gigachad:
        tokens = [token + ': $' + str(price['usd']) + '\n' for token, price in new_gigachad.items()]
        tokens.insert(0, "Gigachad Research Prices:\n")
        update.message.reply_text(f''.join(tokens))
    else:
        update.message.reply_text(new_percentage["error"])

@on_message
def ada_price_command(update: Update, context: CallbackContext) -> None:
    """Sends a message when the command /adaprice is issued."""
    new_price = get_ada_price()
    if "error" not in new_price:
        prices = [f'ADA {currency}: {price} \n' for currency, price in new_price["cardano"].items()]
        update.message.reply_text(''.join(prices))
    else:
        update.message.reply_text(new_price["error"])