import pandas as pd
import pickle
import gzip
import matplotlib.pyplot as plt



with gzip.open('data/stocks_adjusted_close.pklz', 'rb') as f:
    stocks_ac = pickle.load(f)
with gzip.open('data/stocks_full.pklz', 'rb') as f:
    stocks_full = pickle.load(f)



# Visualización ===============================================================
plt.figure(figsize=(10,6))
plt.title('Cotización de las principales acciones, 1990-2023')

# Iteracion para graficar todas las variables
for company in name[0:9]:
    plt.plot(stocks_ac.index, stocks_ac[company], label = company)

plt.ylabel('US$')
plt.grid(True)
plt.legend()

plt.show()



