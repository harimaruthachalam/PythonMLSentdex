import pandas as pd
import quandl
quandl.ApiConfig.api_key = '76eCnz6z9XTH8nfLWeQU'
import pickle

# Request to the Quandl Server for data
#df = quandl.get('WIKI/GOOGL')

# Writing the data
#pickle.dump(df, open("DataFromQuandl_Stock.pickle", "wb+"))

# Reading the Data dump
df = pickle.load(open("DataFromQuandl_Stock.pickle", "rb"))

print(df.head())

print(df['Adj. High'])
print(df['Adj. Close'])
print(df['Adj. High'] - df['Adj. Close'])
foo = df[['Adj. High', 'Adj. Close']]

print(foo)
print(type(foo))
