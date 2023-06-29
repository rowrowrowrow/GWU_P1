import pandas as pd
import sqlalchemy

def store_data_sql(data):
    """Stores data into separate tables in an SQL database based on unique symbols.
    
    Args:
        data (DataFrame): The DataFrame containing the data to be stored in the SQL database.
    
    """
    
    # Create the connection string for your SQLite database
    database_connection_string = 'sqlite:///'

    # Pass the connection string to the SQLAlchemy create_engine function
    engine = sqlalchemy.create_engine(database_connection_string)
    
    # Iterate over the unique symbols and save each symbol's data into a separate table
    for symbol in data['symbol'].unique():
        symbol_data = data[data['symbol'] == symbol]
        symbol_data.to_sql(name=symbol, con=engine, if_exists='replace')