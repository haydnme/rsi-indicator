import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import datetime as dt
import sys

def parse_arguments():
    """Parse and validate command-line arguments for ticker, start date, end date, and interval."""
    args = sys.argv
    try:
        ticker, start_date, end_date, interval = args[1:]
    except ValueError:
        print("Please provide the ticker, start date, end date, and interval.")
        sys.exit(1)
    
    # Validate start_date format
    try:
        start_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        print("Error: Start date must be in the format YYYY-MM-DD.")
        sys.exit(1)
    
    # Check if end_date is "now" (case-insensitive) or validate it as a date
    if end_date.lower() == "now":
        end_date = dt.datetime.now()
    else:
        try:
            end_date = dt.datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            print("Error: End date must be in the format YYYY-MM-DD or 'now'.")
            sys.exit(1)
    
    # Ensure start_date is before end_date
    if start_date >= end_date:
        print("Error: Start date must be before the end date.")
        sys.exit(1)
    
    # Restrict interval to "1d" or "1wk"
    if interval not in ["1d", "1wk"]:
        print("Error: Interval must be '1d' or '1wk'.")
        sys.exit(1)
    
    return ticker, start_date, end_date, interval

def fetch_data(ticker, start_date, end_date, interval):
    """Fetch stock data for the specified date range and interval."""
    try:
        data = yf.download(ticker, start_date, end_date, interval=interval)
        
        # Flatten MultiIndex columns if present (e.g., for UK tickers like 'BARC.L')
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
        
        # For UK stocks, use 'Close' as 'Adj Close' if necessary
        if ticker.endswith('.L') or 'Adj Close' not in data.columns:
            data['Adj Close'] = data['Close'] if 'Close' in data.columns else None
            if data['Adj Close'].isnull().all():
                print("No valid 'Adj Close' or 'Close' data available.")
                sys.exit(1)
                
    except Exception as e:
        print(f"Could not fetch data for {ticker}: {e}")
        sys.exit(1)
    
    if data.empty:
        print("No data was returned.")
        sys.exit(1)
        
    return data

def calculate_rsi(data, period=14):
    """Calculate the Relative Strength Index (RSI) based on adjusted close prices."""
    delta = data['Adj Close'].diff(1).dropna()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100.0 - (100.0 / (1.0 + rs))

    combined = pd.concat([data['Adj Close'], rsi.rename('RSI')], axis=1).dropna()
    return combined

def plot_data(combined, ticker):
    """Plot the Adjusted Close price and RSI data with the ticker in the title."""
    plt.figure(figsize=(12, 8))
    
    # Adjusted Close Price Plot
    ax1 = plt.subplot(211)
    ax1.plot(combined.index, combined['Adj Close'], color='lightgray')
    ax1.set_title(f'{ticker.upper()} Adjusted Close Price', color='white')  # Ticker in title
    ax1.grid(True, color='#555555')
    ax1.set_facecolor('black')
    ax1.figure.set_facecolor('#121212')
    ax1.tick_params(axis='x', colors='white')
    ax1.tick_params(axis='y', colors='white')
    
    # RSI Plot
    ax2 = plt.subplot(212, sharex=ax1)
    ax2.plot(combined.index, combined['RSI'], color='lightgray')
    for level, color in zip([0, 10, 20, 30, 70, 80, 90, 100], 
                            ['#ff0000', '#ffaa00', '#00ff00', '#cccccc', 
                             '#cccccc', '#00ff00', '#ffaa00', '#ff0000']):
        ax2.axhline(level, linestyle='--', alpha=0.5, color=color)
    
    ax2.set_title("RSI Value", color='white')
    ax2.grid(False)
    ax2.set_facecolor('black')
    ax2.tick_params(axis='x', colors='white')
    ax2.tick_params(axis='y', colors='white')
    
    plt.show()

def main():
    ticker, start_date, end_date, interval = parse_arguments()
    data = fetch_data(ticker, start_date, end_date, interval)
    combined_data = calculate_rsi(data)
    plot_data(combined_data, ticker)

if __name__ == "__main__":
    main()