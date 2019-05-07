# Main script for ichimoku cloud
import os
import sys
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('data/historical_candles.csv')

p1 = 9
p2 = 26
p3 = 52
p4 = 26

# Tenkan (conversion line)
# (highest high + highest low)/2 for the past 9 periods

# Kijun (base line)
# (highest high + lowest low)/2 for the past 26 periods

# Chikou (lagging span)
# Current closing price time-shifted backwards 26 periods

# Senkou span A (leading span A)
# (tenkan + kijun)/2 time-shifted fowwards 26 periods

# Senkou span B (leading span B)
# (highest high + lowest low)/2 for past 52 periods, shifted forwards 26 periods


# Span A > Span B == green cloud
# Span A < Span B == red cloud
