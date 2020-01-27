# Find usernames/ids for people in free chat and not in paid chat
# TODO: Compare paid chat to google sheets signup form and send messages for renewal

import pandas as pd



df_free = pd.read_csv('../data/users/ATTA_FREE.csv')
df_paid = pd.read_csv('../data/users/ATTA_PAID.csv')

username_free = set(df_free['username'].dropna())
username_paid = set(df_paid['username'].dropna())

# Remove bots from message list
username_free = [_ for _ in username_free if 'bot' not in _]
username_paid = [_ for _ in username_paid if 'bot' not in _]

free_only = username_free - username_paid
