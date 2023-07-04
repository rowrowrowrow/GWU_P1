import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

def get_tickers_list():
    """Retrieves a list of active assets' symbols along with their index positions.

    Returns:
        A list of tuples in the format ('symbol', index), where 'symbol' is the symbol of an active asset
        and 'index' is the index position of the asset plus one.

    """

    load_dotenv()

    # Set the variables for the Alpaca API and secret keys
    alpaca_api_key= os.getenv("ALPACA_API_KEY")
    alpaca_secret_key= os.getenv("ALPACA_SECRET_KEY")

    # Create the Alpaca tradeapi.REST object
    alpaca = tradeapi.REST(alpaca_api_key, alpaca_secret_key, api_version="v2")
    
    active_assets = api.list_assets(status='active')

    # Create a list of tuples with symbol and index
    tickers_list = [(asset.name , asset.symbol) for index, asset in enumerate(active_assets)]

    return tickers_list


