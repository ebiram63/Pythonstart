import numpy as np
import pandas as pd
import yfinance as yf


NIFTY = yf.download('^NSEI',start='2018-6-1', end='2022-6-1')


NIFTY['Log_Ret'] = np.log(NIFTY['Close'] / NIFTY['Close'].shift(1))


NIFTY['Volatility'] = NIFTY['Log_Ret'].rolling(window=252).std() * np.sqrt(252)
print(NIFTY.tail(15))


NIFTY[['Close', 'Volatility']].plot(subplots=True, color='blue',figsize=(8, 6))