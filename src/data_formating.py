import pandas as pd

def format_data(data):
    """Formats the given data DataFrame to a specific format by pivoting the table and organizing the columns. 
    
        Args:
            data (DataFrame): The DataFrame containing the data to be formatted. 
            
        Returns:
            DataFrame: The formatted DataFrame with the desired format, where each ticker symbol 
            corresponds to a column, and the rows represent dates with the corresponding close prices.
            
    """
    
    # Reset index if 'timestamp' is the index column
    if 'timestamp' not in data.columns:
        data = data.reset_index()

    # Convert timestamp to datetime
    data['date'] = pd.to_datetime(data['timestamp'])
    
    # Extract date only
    data['date'] = data['date'].dt.date
    
    # Pivot table to have ticker symbols as columns
    formatted_data = data.pivot(index='date', columns='symbol', values='close')
    
    # Reset index and rename columns
    formatted_data = formatted_data.reset_index().rename_axis(None, axis=1)
    
    return formatted_data