def market_data_parser(market_data: dict, coin: str) -> list:
    """Takes a dict with market data and parses the result as a list."""
    # Current Prices
    currency_keys = ["aud", "usd", "czk", "gbp"]
    current_prices = [f'{key.upper()}: {value}\n' for key, value in market_data["current_price"].items() if key in currency_keys]
    current_prices.insert(0, f'Current {coin} Price\n')
    current_prices.append('\n')

    # 24 Hour Price Change
    price_change_percentage_24h = [f'{key.upper()}: {value}%\n' for key, value in market_data["price_change_percentage_24h_in_currency"].items() if key in currency_keys]
    price_change_percentage_24h.insert(0, '24h Price Change %\n')
    price_change_percentage_24h.append('\n')

    # 24 Hour Percentage Change
    price_change_24h = [f'{key.upper()}: {value}\n' for key, value in market_data["price_change_24h_in_currency"].items() if key in currency_keys]
    price_change_24h.insert(0, '24h Price Change\n')
    price_change_24h.append('\n')

    # Return Concatenated Lists
    return current_prices + price_change_percentage_24h + price_change_24h

def eth_gas_price_parser(gas_data: dict) -> list:
    """Takes a dict with gas price data and parses the result as a list."""
    price_keys = ["average", "fast", "fastest"]
    gas_prices = [f'{key}: {int(value/10)} GWEI\n' for key, value in gas_data.items() if key in price_keys]
    gas_prices.insert(0, 'ETH Gas Prices\n')
    gas_prices.append('\n')

    return gas_prices