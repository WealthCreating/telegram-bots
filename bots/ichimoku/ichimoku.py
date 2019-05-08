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

df2 = df[:400]

# Span A > Span B == green cloud
# Span A < Span B == red cloud
tenkan = df2['tenkan']
kijun = df2['kijun']
a = df2['senkou_a']
b = df2['senkou_b']
x = df2['date']

fig = plt.plot(x, a, x, b)
plt.fill_between(x, a, b, where=a >= b, facecolor='green', interpolate=True)
plt.fill_between(x, a, b, where=a <= b, facecolor='red', interpolate=True)

plt.plot(x, tenkan, color='yellow')
plt.plot(x, kijun, color='blue')
plt.show()
