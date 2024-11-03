# rsi-indicator
An RSI indicator coded in Python.

This application generates RSI values for a given stock ticker and outputs a chart showing the close price and rsi value between date range.

Usage:
python main.py <ticker> <start_date> <end_date> <interval>

For example: to view the rsi indicator for META from 2024-01-01 until the current date on a daily chart you would use the following arguments: 
python main.py meta 2024-01-01 now 1d

To view the rsi indicator for META from 2023-01-01 up until 2024-06-01 on a weekly interval you would use the following arguments:
python main.py meta 2023-01-01 2024-06-01 1wk

Valid interval periods are:
1d = Daily
1wk = Weekly