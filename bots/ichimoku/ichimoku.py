# Main script for ichimoku cloud
from bots.ichimoku.functions import make_lines, make_spans
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('data/historical_candles.csv')

tenkan_period = 20
kijun_period = 60
senkou_b_period = 120
displacement = 30

make_lines(df, tenkan=tenkan_period, kijun=kijun_period)
make_spans(df, displacement=displacement, senkou_b_period=senkou_b_period)

print(df)



# Span A > Span B == green cloud
# Span A < Span B == red cloud
