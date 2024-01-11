import pandas as pd
import numpy as np

def momentum_strategy(data, lookback_period=50, momentum_threshold=0.02):
    # Calculate returns
    data['Returns'] = data['Close'].pct_change()

    # Calculate the rolling mean of returns over the lookback period
    data['RollingMean'] = data['Returns'].rolling(window=lookback_period).mean()

    # Create a signal based on momentum
    data['Signal'] = np.where(data['Returns'] > data['RollingMean'] * (1 + momentum_threshold), 1, 0)
    data['Signal'] = np.where(data['Returns'] < data['RollingMean'] * (1 - momentum_threshold), -1, data['Signal'])

    # Generate buy and sell signals
    data['Buy_Signal'] = np.where(data['Signal'] == 1, data['Close'], np.nan)
    data['Sell_Signal'] = np.where(data['Signal'] == -1, data['Close'], np.nan)

    return data[['Close', 'Buy_Signal', 'Sell_Signal']]

# Example usage
# Assuming 'data' is a pandas DataFrame with 'Date' and 'Close' columns
# You can obtain financial data using libraries like yfinance or pandas_datareader
# For simplicity, this example assumes daily closing prices.
# Adjust the parameters according to the specific requirements of the fund.

# Example:
# data = yfinance.download('AAPL', start='2022-01-01', end='2022-12-31')
# result = momentum_strategy(data)

# The 'result' DataFrame will contain closing prices, buy signals, and sell signals.
