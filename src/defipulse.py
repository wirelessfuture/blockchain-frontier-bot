# Import Python Modules
import requests
import os

# Setup Python Dot Env
from dotenv import load_dotenv
load_dotenv()


def get_eth_gas_prices() -> dict:
    """Gets the current Ethereum gas prices."""
    defipulse_api_key = os.getenv("DEFIPULSE_API_KEY")
    ethgasstation_endpoint = 'https://data-api.defipulse.com/api/v1/egs/api/ethgasAPI.json'
    params = {"api-key": defipulse_api_key}
    return requests.get(url=ethgasstation_endpoint, params=params).json()

def get_defi_pulse_data() -> dict:
    """Gets the current DefiPulse market data."""
    defipulse_api_key = os.getenv("DEFIPULSE_API_KEY")
    defipulse_endpoint = 'https://data-api.defipulse.com/api/v1/defipulse/api/MarketData'
    params = {"api-key": defipulse_api_key}
    return requests.get(url=defipulse_endpoint, params=params).json()