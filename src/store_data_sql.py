import pandas as pd
import sqlalchemy
from src.table_exists import table_exists

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
        
        # Check if the table already exists in the SQL database
        table_exists_flag = table_exists(engine, symbol)

        if table_exists_flag:
            # Retrieve existing data from the SQL table
            existing_data = pd.read_sql_table(symbol, con=engine)

            # Identify new rows based on dates that do not already exist in the table
            new_rows = symbol_data[~symbol_data['timestamp'].isin(existing_data['timestamp'])]

            # Append only the new rows to the existing data
            updated_data = existing_data.append(new_rows)

            # Replace the existing data in the SQL table with the updated data
            updated_data.to_sql(name=symbol, con=engine, if_exists='replace', index=False)
        else:
            # If the table does not exist, save the data directly
            symbol_data.to_sql(name=symbol, con=engine, if_exists='replace', index=False)
    