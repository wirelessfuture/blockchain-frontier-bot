from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


def check_server(func: any) -> any:
    """Decorator for checking the coingecko API status before each request"""
    def wrapper_is_server_ok():
        if cg.ping()["gecko_says"] == "(V3) To the Moon!":
            return func()
        else:
            return {"error": "Server is currently experiencing issues"}
    return wrapper_is_server_ok

@check_server
def get_trending_search() -> dict:
    """Get trending search coins (Top-7) on CoinGecko in the last 24 hours."""
    return cg.get_search_trending()

@check_server
def get_eth_price() -> dict:
    """Get the latest price of Ethereum in various currencies."""
    return cg.get_price(ids='ethereum', vs_currencies='usd,gbp,czk,aud')

@check_server
def get_eth_percentage_change() -> dict:
    """Get the latest Ethereum price percentage change in various time ranges."""
    return cg.get_coin_by_id(
        id="ethereum", 
        localization_string=False, 
        tickers=False, 
        market_data=True, 
        community_data=False, 
        developer_data=False, 
        sparkline=False
    )

@check_server
def get_btc_price() -> dict:
    """Get the latest price of Bitcoin in various currencies."""
    return cg.get_price(ids='bitcoin', vs_currencies='usd,gbp,czk,aud')

@check_server
def get_btc_percentage_change() -> dict:
    """Get the latest Bitcoin price percentage change in various time ranges."""
    return cg.get_coin_by_id(
        id="bitcoin", 
        localization_string=False, 
        tickers=False, 
        market_data=True, 
        community_data=False, 
        developer_data=False, 
        sparkline=False
    )