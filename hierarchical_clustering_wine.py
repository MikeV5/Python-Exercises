import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

#Caricamento del dataset dei vini
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
column_names = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols',
                'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue',
                'OD280/OD315 of diluted wines', 'Proline']

wine_data = pd.read_csv(url, names=column_names)

#Stampa delle prime 5 righe del dataFrame
print(wine_data.head())

#Selezione delle tredici colonne tranne la prima colonna della classe
X = wine_data.iloc[:, 1:].values

#Calcoliamo la matrice di linkage per l'albero di clustering agglomerativo
Z = linkage(X, 'ward')

#Dendrogramma
plt.title('Dendrogramma per il clustering dei vini')
dendrogram(Z, leaf_rotation=90., leaf_font_size=8.,)
plt.show()