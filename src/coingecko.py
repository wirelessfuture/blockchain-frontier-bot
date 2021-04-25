from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def check_server(func: any) -> any:
    """Decorator for checking the coingecko API status before each request"""

    def wrapper_is_server_ok(*args, **kwargs):
        try:
            if cg.ping()["gecko_says"] == "(V3) To the Moon!":
                return func(*args, **kwargs)
            else:
                return {"error": "Server is currently experiencing issues"}
        except Exception as e:
            return {"error": "Something went wrong. 👀"}

    return wrapper_is_server_ok


@check_server
def get_trending_search() -> dict:
    """Get trending search coins (Top-7) on CoinGecko in the last 24 hours."""
    return cg.get_search_trending()


@check_server
def get_market_data(id: str) -> dict:
    """Get the latest market data."""
    return cg.get_coin_by_id(
        id=id,
        localization_string=False,
        tickers=False,
        market_data=True,
        community_data=False,
        developer_data=False,
        sparkline=False,
    )


@check_server
def get_coins() -> dict:
    """Retrieves all the coins listed on coingecko."""
    return cg.get_coins_list()


@check_server
def get_gigachad_prices() -> dict:
    """Get the latest Gigachad list prices."""
    gigachad_list = ["xio", "mettalex", "origintrail", "rocket-pool", "flash-stake"]
    price_dict = {}
    for token in gigachad_list:
        price_dict[token] = cg.get_price(ids=token, vs_currencies="usd")[token]
    return price_dict
