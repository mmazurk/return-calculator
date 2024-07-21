import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import acf

sp500 = yf.Ticker('^GSPC')
data = sp500.history(period='10y', interval='1mo')

data['Return'] = data['Close'].pct_change()
returns = data['Return'].dropna()

fig, ax = plt.subplots()
ax.hist(returns, bins=13, linewidth=0.5, edgecolor="white")
plt.show()

returns.describe()
float(returns.skew())

# Here is how I can calculate autocorrelation
autocorr = acf(returns, nlags=4)
autocorr

# This shows that the returns tend to be inerse for two months but after three they aren't related at all.
