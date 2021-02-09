from dataclasses import dataclass


@dataclass
class PriceDict:
    coin_id: str
    usd: float
    gbp: float
    czk: float
    aud: float


@dataclass
class PercentageDict:
    coin_id: str
    price_change_percentage_24h: float
    price_change_percentage_7d: float
    price_change_percentage_14d: float
    price_change_percentage_30d: float
    price_change_percentage_60d: float
    price_change_percentage_200d: float
    price_change_percentage_1y: float