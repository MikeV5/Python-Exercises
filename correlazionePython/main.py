import numpy as np
from scipy.stats import pearsonr
from matplotlib import pyplot as plt

# Dati dei giorni con il rispettivo indice di traffico
datiTraffico = np.array([[1, 100], [2, 90], [3, 80], [4, 80], [5, 90], [6, 60], [7, 40],
                         [8, 105], [9, 95], [10, 80], [11, 85], [12, 95], [13, 60], [14, 35],
                         [15, 100], [16, 90], [17, 75], [18, 80], [19, 90], [20, 65], [21, 40],
                         [22, 105], [23, 90], [24, 80], [25, 85], [26, 90], [27, 55], [28, 35]])

primiSetteGiorni = datiTraffico[:7, 1]

correlazioni = list()
for i in range(1, 22):  # indice 22 non viene considerato
    correlazioni.append(pearsonr(primiSetteGiorni, datiTraffico[i:i + 7, 1])[0])

last_4giorni = datiTraffico[:4, 1]
last_5giorni = datiTraffico[:5, 1]
last_6giorni = datiTraffico[:6, 1]

correlazioni.append(pearsonr(last_6giorni, datiTraffico[22:28, 1])[0])
correlazioni.append(pearsonr(last_5giorni, datiTraffico[23:28, 1])[0])
correlazioni.append(pearsonr(last_4giorni, datiTraffico[24:28, 1])[0])
# print(correlazioni)

# Grafico del traffico a Milano
plt.plot(datiTraffico[:, 0], datiTraffico[:, 1], color='red')
plt.title("Traffico a Milano")
plt.xlabel("Giorni")
plt.ylabel("Indice di traffico")
plt.show()

# Grafico dei coeff. di correlazione (con shift)
#plt.axhline(y=0, color='black', linestyle='--')
plt.xlim(-0.5, 25)
plt.plot(correlazioni, color='blue')
plt.plot(correlazioni, 'o', markersize=10, color='blue')

plt.title("Autocorrelazione")
plt.xlabel("Shift in giorni")
plt.ylabel('Coeff. Autocorrelazione')
plt.show()
