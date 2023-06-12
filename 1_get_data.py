import pandas as pd
import pickle
import time
import yfinance as yf
import gzip
from datetime import datetime


fecha_inicio = datetime(1990, 1, 1)



# Importación =================================================================
df = pd.read_excel('data/tickers.xlsx')

tickers = {}
for index, row in df.iterrows():
    tickers[row['Ticker']] = row['Nombre']

keys = list(tickers.keys())
name = list(tickers.values())


# Obtención de data ===========================================================
## Cierre ajustado
while True:
    try:
        stocks_ac = yf.download(keys, start=fecha_inicio)['Adj Close']; break
    except:
        print('Error'); time.sleep(5)

stocks_ac = stocks_ac.rename(tickers, axis=1)
stocks_ac.sort_index(axis=1, inplace=True)
stocks_ac.sort_index(axis=0, inplace=True)
stocks_ac


## Full dataset
while True:
    try:
        stocks_full = yf.download(keys, start=fecha_inicio); break
    except:
        print('Error'); time.sleep(5)


stocks_full = stocks_full.rename(tickers, axis=1)
stocks_full.columns = pd.MultiIndex.from_tuples(stocks_full.columns)
stocks_full = stocks_full.swaplevel(axis=1)
stocks_full.sort_index(axis=1, inplace=True)
stocks_full.sort_index(axis=0, inplace=True)
stocks_full


# Guardado ====================================================================
with gzip.open('data/stocks_adjusted_close.pklz', 'wb') as f:
    pickle.dump(stocks_ac, f)
with gzip.open('data/stocks_full.pklz', 'wb') as f:
    pickle.dump(stocks_full, f)


# stocks_ac.to_csv('data/stocks_ac.csv', sep=';')
# stocks_full.to_csv('data/stocks_full.csv', sep=';')