# Main script for ichimoku cloud
import os
import sys
import ccxt
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

binance = ccxt.binance()

columns = ['date', 'open', 'high', 'low', 'close', 'volume']
data = binance.fetch_ohlcv('BTC/USDT', '1h')

df = pd.DataFrame(data=data, columns=columns)
df['date'] = df['date'].apply(lambda x: datetime.fromtimestamp(x/1000))
df.set_index('date', inplace=True)
