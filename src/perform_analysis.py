from src.retrieve_data import retrieve_data
from src.store_data_sql import store_data_sql
from src.data_formating import format_data
import pandas as pd
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt import plotting
from datetime import date
from matplotlib import pyplot

def perform_analysis(risk_aversion, tickers, start_date, end_date):
    #---------------- this will be set by the user ------------
    # Define tickers for both the bond and stock portion of the portfolio
    tickers_as_list = list(tickers)
    
    if not len(tickers_as_list):
        return "Please select a batch of assets to perform an analysis."
    
    # Define start and end dates
    if start_date >= end_date:
        return "The starting date for historical date must be older than the end date."
        
    if end_date >= date.today():
        return "The end date for historical date must be older than today's date."
        
    start_date_string = start_date.strftime("%Y-%m-%d")
    end_date_string = end_date.strftime("%Y-%m-%d")
    #------------------------------------------------------
    
    # Retrieve the historical data
    data_df = retrieve_data(tickers=tickers_as_list, start_date=start_date_string, end_date=end_date_string)

    # Store data in SQL database
    # store_data_sql(data_df)

    # Format data Dataframe
    formated_data_df = format_data(data_df)
    
    # return formated_data_df
    # Calculate expected returns and sample covariance
    mu = expected_returns.mean_historical_return(formated_data_df)
    S = risk_models.sample_cov(formated_data_df)

    # Optimize for maximal Sharpe ratio
    ef = EfficientFrontier(mu, S)
    ef_risk = ef.deepcopy()
    ef_sharpe = ef.deepcopy()
    
    fig, ax1 = pyplot.subplots()
    fig, ax2 = pyplot.subplots()
    fig, ax3 = pyplot.subplots()
    plotting.plot_efficient_frontier(ef, ax=ax1, show_assets=True, show_tickers=True)
    
    # Provide plot based on risk risk_aversion
    raw_max_quadratic_utility_weights = ef_risk.max_quadratic_utility(risk_aversion=risk_aversion)
    clean_max_quadratic_utility_weights = ef_risk.clean_weights()
    plotting.plot_weights(weights=clean_max_quadratic_utility_weights, ax=ax2)
    ax2.set_title("Max Quadratic Utility Allocation")
    # ef_risk.save_weights_to_file("max_quadratic_utility_weights.csv")
    ret_tangent, std_tangent, _ = ef_risk.portfolio_performance()
    ax1.scatter(std_tangent, ret_tangent, marker="*", s=100, c="r", label="Max Quadratic Utility")
    
    
    # Provide plot based on Sharpe
    raw_max_sharpe_weights = ef_sharpe.max_sharpe()
    clean_max_sharpe_weights = ef_sharpe.clean_weights()
    # ef_sharpe.save_weights_to_file("max_sharpe_weights.csv")
    plotting.plot_weights(weights=clean_max_sharpe_weights, ax=ax3)
    ax3.set_title("Max Sharpe Allocation")
    ret_tangent, std_tangent, _ = ef_sharpe.portfolio_performance()
    ax1.scatter(std_tangent, ret_tangent, marker="x", s=100, c="r", label="Max Sharpe")
    
    ax1.set_title("Efficient Frontier with Max Sharpe and Max Quadratic Utility")
    ax1.legend()