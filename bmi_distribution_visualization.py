import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

def calcoloBMI(peso, altezza):
    return peso / (altezza ** 2)

def assegnaColore(bmi):
    if bmi < 18.5:
        return ('yellow', 'underweight')
    elif bmi < 25.0:
        return ('red', 'normal')
    elif bmi < 30.0:
        return ('green', 'overweight')
    else:
        return ('blue', 'obese')

#lettura file csv
url = 'https://raw.githubusercontent.com/Bogdan11031999/BigData/main/BMI_Pallavolisti%20-%20Foglio1.csv'
dataset = pd.read_csv(url,sep = ',')

#inserimento dei valori del csv in strutture dati
pesi=dataset['Peso']
altezze=dataset['Altezza']

italianiData = {
    "weights": pesi,
    "heights": altezze
}

italianiBMI = []
for i in range(len(italianiData["weights"])):
    bmi = calcoloBMI(italianiData["weights"][i], italianiData["heights"][i])
    italianiBMI.append(bmi)

italiani_colori = []
italians_labels = []

for bmi in italianiBMI:
    colore, label = assegnaColore(bmi)
    italiani_colori.append(colore)
    italians_labels.append(label)

plt.scatter(italianiData["weights"], italianiData["heights"], c=italiani_colori, s=3)
plt.xlabel("Peso (Kg)")
plt.ylabel("Altezza (m)")
plt.title("Distribuzione del BMI dei pallavolisti italiani")
plt.ylim(0.6, 2.5)
plt.xlim(0, 250)

legendaNomi = []
colori = ['yellow', 'red', 'green', 'blue']
labels = ['underweight', 'normal', 'overweight', 'obese']

for i in range(len(colori)):
    legendaNomi.append(plt.Line2D([], [], marker='o', color='w', label=labels[i], markerfacecolor=colori[i], markersize=5))

plt.legend(handles=legendaNomi)
plt.show()