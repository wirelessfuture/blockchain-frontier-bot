from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


def check_server(func: any) -> bool:
    """Decorator for checking the coingecko API status before each request"""
    def wrapper():
        if cg.ping()["gecko_says"] == "(V3) To the Moon!":
            func()
        else:
            return {"error": "Server is currently experiencing issues"}
    return func

@check_server
def get_eth_price() -> dict:
    """Get the latest price of Ethereum in various currencies."""
    return cg.get_price(ids='ethereum', vs_currencies='usd,gbp,czk,aud')

@check_server
def get_trending_search() -> dict:
    """Get trending search coins (Top-7) on CoinGecko in the last 24 hours."""
    return cg.get_search_trending()