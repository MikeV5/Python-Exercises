import pandas as pd
from matplotlib import pyplot as plt

url = 'https://raw.githubusercontent.com/burgosale/Dataset/main/whosbigger.csv'
df = pd.read_csv(url)
df.head()

#pesi
IT_WEIGHT = 0.5
EN_WEIGHT = 0.5

#funzione bunda score
def bunda_score(df,it_weight, en_weight):
    #calcolo punteggio bunda per ogni riga del dataset
    df['bunda_score'] = it_weight*df['IT_pagerank']+en_weight*df['EN_pagerank']
    # Ordino il dataframe in ordine decrescente in base al punteggio bunda
    df = df.sort_values(by=['bunda_score'], ascending=False)
    # Assegnare il punteggio bunda a ciascuna riga del dataframe
    for i, row in df.iterrows():
        df.at[i, 'bunda_rank'] = i+1
    # Restituire il dataframe con il punteggio bunda e il rank associato
    return df[['name', 'bunda_score', 'bunda_rank']]


result = bunda_score(df, IT_WEIGHT,EN_WEIGHT)
result= result.sort_values(by=['bunda_rank'],ascending = False)

#creazione grafico a barre
plt.figure(figsize=(17,8))
plt.bar(result['name'],result['bunda_rank'],color = 'red')
plt.xlabel('Persona')
plt.ylabel('bunda rank')
plt.show()