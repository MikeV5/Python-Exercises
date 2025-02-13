import numpy as np
import matplotlib.pyplot as plt

def prob_somma_2dadi():
    probs = np.zeros(11)
    for i in range(1, 7):
        for j in range(1, 7):
            probs[i + j - 2] += 1
    probs /= 36
    return probs

somme = np.arange(2, 13)
probs = prob_somma_2dadi()
plt.bar(somme, probs)
plt.title('PDF')
plt.xlabel('Somma dei dadi')
plt.ylabel('Probabilità')
plt.xticks(somme)
plt.show()