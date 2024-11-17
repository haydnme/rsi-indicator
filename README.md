Techical Indicator

This Python application fetches stock market data from Yahoo Finance, calculates the Relative Strength Index (RSI), and visualizes both the adjusted close price and RSI using Matplotlib. It is designed for users who want to analyze stock trends over a specified period and interval.

---

## Features

- **Stock Data Retrieval**: Fetches data for any stock ticker using Yahoo Finance.
- **RSI Calculation**: Computes the Relative Strength Index (RSI) using a 14-period rolling average by default.
- **Interactive Visualization**: Plots the adjusted close price and RSI on separate panels with color-coded RSI thresholds for better readability.
- **Command-line Interface**: Allows users to specify the stock ticker, date range, and interval directly via the command line.

---

## Requirements

- Python 3.8 or later
- Dependencies:
  - `pandas`
  - `numpy`
  - `yfinance`
  - `matplotlib`

Install the required libraries using pip:

```bash
pip install pandas numpy yfinance matplotlib
```

---

## Usage

### Command-line Arguments
The application expects the following four arguments:

1. **Ticker**: The stock ticker symbol (e.g., `AAPL` for Apple, `BARC.L` for Barclays).
2. **Start Date**: The start date for the data range in `YYYY-MM-DD` format.
3. **End Date**: The end date for the data range in `YYYY-MM-DD` format or `now` (case-insensitive) to use the current date.
4. **Interval**: The data interval (`1d` for daily data, `1wk` for weekly data).

### Running the Application

Run the script from the terminal as follows:

```bash
python main.py [TICKER] [START_DATE] [END_DATE] [INTERVAL]
```

Example:

```bash
python main.py AAPL 2023-01-01 2023-12-31 1d
```

### Output

1. **Data Fetch**: Downloads stock data within the specified date range and interval.
2. **RSI Calculation**: Computes RSI for the adjusted close prices.
3. **Plotting**: Displays a dual-panel plot:
   - **Top Panel**: Adjusted close price.
   - **Bottom Panel**: RSI with thresholds (30 and 70 marked for overbought and oversold conditions).

---

## Example Visualization

- The top panel displays the adjusted close price.
- The bottom panel visualizes the RSI with horizontal lines marking RSI levels (e.g., 30 for oversold, 70 for overbought).

---

## Error Handling

The script includes robust error handling for:
- Incorrect or missing command-line arguments.
- Invalid date formats.
- End dates earlier than start dates.
- Unsupported intervals (`1d` or `1wk` only supported).
- Missing or incomplete stock data.

---

## Notes

- For UK tickers (e.g., `BARC.L`), the script uses the 'Close' price if 'Adj Close' is not available.
- The color-coded RSI plot uses visually distinct thresholds to highlight overbought and oversold regions.

---