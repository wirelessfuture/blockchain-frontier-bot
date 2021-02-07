from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

def get_eth_price() -> dict:
    return cg.get_price(ids='ethereum', vs_currencies='usd,gbp,czk,aud')
