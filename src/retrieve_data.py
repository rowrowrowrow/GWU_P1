def retrieve_data(tickers, start_date, end_date):
    """Retrieve historical data for a list of tickers within a specified time period.
    
    Args: 
        tickers (list) = List of tickers to retrieve data for.
        start_date(Timestamp) = The start date of the historical data.
        end_date(Timestamp) = The end date of the historical data.
    
    Returns:
        A DataFrame containing the historical data for the specified tickers.
        
    """
    
    # Load the environment variables from the .env file
    #by calling the load_dotenv function
    load_dotenv()

    # Set the variables for the Alpaca API and secret keys
    alpaca_api_key= os.getenv("ALPACA_API_KEY")
    alpaca_secret_key= os.getenv("ALPACA_SECRET_KEY")

    # Create the Alpaca tradeapi.REST object
    alpaca = tradeapi.REST(alpaca_api_key, alpaca_secret_key, api_version="v2")
    
    # Set timeframe to 1Day
    timeframe = "1Day"
    
    # Use the Alpaca get_bars function to get historical data of the assets
    portfolio_prices_df = alpaca.get_bars(
        tickers,
        timeframe,
        start = start_date,
        end = end_date
     ).df
    
    return portfolio_prices_df
    