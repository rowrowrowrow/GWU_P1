from src.retrieve_data import retrieve_data
from src.store_data_sql import store_data_sql
from src.data_formating import format_data
import pandas as pd

def run():
    """The main function for running the script."""
    
    #---------------- this will be set by the user ------------
    # Define tickers for both the bond and stock portion of the portfolio
    tickers = ["SPY", "AGG"]

    # Define start and end dates
    start_date = pd.to_datetime("2023-05-9").strftime("%Y-%m-%d")
    end_date = pd.to_datetime("2023-06-9").strftime("%Y-%m-%d")
    #------------------------------------------------------
    
    # Retrieve the historical data
    data_df = retrieve_data(tickers, start_date, end_date)
    
    # Store data in SQL database
    store_data_sql(data_df)

     # Format data Dataframe
    formated_data_df = format_data(data_df)
   
    