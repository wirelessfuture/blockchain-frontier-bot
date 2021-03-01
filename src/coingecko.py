from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


def check_server(func: any) -> any:
    """Decorator for checking the coingecko API status before each request"""
    def wrapper_is_server_ok():
        try:
            if cg.ping()["gecko_says"] == "(V3) To the Moon!":
                return func()
            else:
                return {"error": "Server is currently experiencing issues"}
        except Exception:
            return {"error": "Server is currently experiencing issues"}
    return wrapper_is_server_ok

@check_server
def get_trending_search() -> dict:
    """Get trending search coins (Top-7) on CoinGecko in the last 24 hours."""
    return cg.get_search_trending()

@check_server
def get_eth_market_data() -> dict:
    """Get the latest Ethereum market data."""
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
def get_btc_market_data() -> dict:
    """Get the latest Bitcoin market data."""
    return cg.get_coin_by_id(
        id="bitcoin", 
        localization_string=False, 
        tickers=False, 
        market_data=True, 
        community_data=False, 
        developer_data=False, 
        sparkline=False
    )

@check_server
def get_ada_market_data() -> dict:
    """Get the latest Bitcoin market data."""
    return cg.get_coin_by_id(
        id="cardano", 
        localization_string=False, 
        tickers=False, 
        market_data=True, 
        community_data=False, 
        developer_data=False, 
        sparkline=False
    )

@check_server
def get_gigachad_prices() -> dict:
    """Get the latest Gigachad list prices."""
    gigachad_list = [
        "xio",
        "mettalex",
        "origintrail",
        "rocket-pool"
    ]
    price_dict = {}
    for token in gigachad_list:
        price_dict[token] = cg.get_price(ids=token, vs_currencies='usd')[token]
    return price_dict