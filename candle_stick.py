
from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
import pandas as pd

# Set the start and end dates
start_date = '2023-01-01'

# Ticker symbol for Apple
ticker = 'AAPL'

# Fetch data using yfinance
data = yf.download(ticker, start=start_date, end = datetime.today().strftime('%Y-%m-%d'))

# Restructure Data
data.reset_index(inplace=True)
data['Date'] = data['Date'].map(mdates.date2num)
data = data[['Date', 'Open', 'High', 'Low', 'Close']].values

# Visualization using mpl_finance.candlestick_ohlc
fig, ax = plt.subplots(figsize=(12, 6))
ax.grid(True)
ax.set_axisbelow(True)
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='both', colors='white')
ax.xaxis_date()
plt.xticks(rotation=90)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title(f'Candlestick Chart for {ticker}', color = 'white')

candlestick_ohlc(ax, data, width = 0.5, colorup='#00ff00', colordown='r')

plt.tight_layout()
plt.show()