from src.get_tickers_list import get_tickers_list
from src.perform_analysis import perform_analysis
from ipywidgets import interact_manual, FloatSlider, SelectMultiple, DatePicker
from datetime import date, timedelta
import pandas as pd

def run():
    """The main function for running the script."""
    my_risk_aversion = FloatSlider(min=0, max=10, step=0.01, value=1, description='Risk Aversion:')

    ticker_options = get_tickers_list()
    
    my_batch_of_tickers = SelectMultiple(
        options=ticker_options,
        description='Assets:',
    )
    
    # Define default start and end dates
    default_end_date = date.today()
    default_start_date = default_end_date - timedelta(days=(5 * 365))
    end_date_max = date.today() - timedelta(days=2)
    start_date_max = end_date_max - timedelta(days=1)
    
    start_date = DatePicker(
        description='Start Date',
        value=default_start_date,
        max=start_date_max,
    )
    
    end_date = DatePicker(
        description='End Date',
        min=start_date.value,
        value=default_end_date,
        max=end_date_max,
    )
    
    # See the following for an explanation:
    #     https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Events.html
    def update_end_date(change):
        end_date.min = change.new + timedelta(days=1)
        
    start_date.observe(update_end_date, names='value')

    out = interact_manual(perform_analysis, risk_aversion=my_risk_aversion, tickers=my_batch_of_tickers, start_date=start_date, end_date=end_date)
    
    return out
   
    