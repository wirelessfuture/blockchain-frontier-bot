from coingecko import get_coins

def search(term: str) -> str:
    """Search for a coin using either ID or Symbol to make search more robust."""
    coins = get_coins()
    for coin in coins:
        for key, value in coin.items():
            if key == "id" and value.lower() == term.lower():
                return term
            if key == "symbol" and value.lower() == term.lower():
                return coin["id"]