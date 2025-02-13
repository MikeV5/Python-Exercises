import itertools
import random
from collections import Counter #libreria per contare le permutazioni
import matplotlib.pyplot as plt
import numpy as np

permutazioni= list(itertools.permutations([1, 2, 3, 4])) #genera le permutazioni
listaPermutazioni = list()

for i in range(1000000):
    permutazioneRandom = random.choice(permutazioni) #seleziona una permutazione a caso
    listaPermutazioni.append(permutazioneRandom)

frequenze = Counter(listaPermutazioni) #conta le frequenze delle permutazioni

for permutazione in frequenze:  #scorre tutte le chiavi del dizionario frequenze
    freq = frequenze[permutazione]
    print(f"Permutazione {permutazione}:{freq}")

x=list(range(len(permutazioni)))
y=list(frequenze.values())
plt.bar(x,y)
plt.xticks(x, permutazioni, rotation=90)
plt.xlabel('Permutazioni')
plt.ylabel('Frequenze')
plt.show()