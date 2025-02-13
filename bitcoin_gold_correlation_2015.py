import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

dataset = pd.read_csv('https://raw.githubusercontent.com/Bogdan11031999/BigData/main/btcgold.csv')
gold = dataset['gold']
btc = dataset['btc']
resPearson=stats.pearsonr(gold,btc)
plt.figure(figsize=(8, 6))
plt.scatter(btc,gold)
plt.xlabel("Oro in once")
plt.ylabel("Bitcoin")
plt.title("Correlazione del prezzo del bitcoin e dell'oncia doro nell'anno 2015.\nIndice di correlazione di Pearson:"+str(resPearson.statistic))

#TODO
#r^2 con alpha = 0.05
#valutazioni

plt.show()