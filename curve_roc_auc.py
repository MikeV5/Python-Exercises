import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import auc

negativi = np.array([34, 74, 100, 127, 153, 114, 19, 6, 4, 0])
positivi = np.array([2, 6, 10, 12, 23, 55, 75, 41, 30, 15])

#Calcolo TPR e FPR
TPR = []
FPR = []

for i in range(11):
    TP = sum(positivi[i:]) #Somma di tutti i valori positivi dall'indice i fino alla fine dell'array
    FP = sum(negativi[i:])
    TN = sum(negativi[:i]) #Somma di tutti i valori negativi dall'inizio dell'array fino all'indice i
    FN = sum(positivi[:i])

    if (FP + TN) == 0:
        FPR.append(0)
    else:
        FPR.append(FP / (FP + TN))
    if (TP + FN) == 0:
        TPR.append(0)
    else:
        TPR.append(TP / (TP + FN))

print("TPR: ",TPR)
print("FPR: ",FPR)

#Calcolo l'AUC

#roc_auc = auc(FPR, TPR)   #Ritorna 0.85
AUC = sum((FPR[i] - FPR[i+1]) * TPR[i] for i in range(len(FPR)-1))
plt.text(0.6, 0.2, f"AUC={AUC:.2f}", fontsize=12)
print("AUC: ",AUC)

#Curva ROC come scatter plot
plt.scatter(FPR, TPR)
plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
plt.xlabel('Tasso di falsi positivi (FPR)')
plt.ylabel('Tasso di veri positivi (TPR)')
plt.title('Curva ROC')
plt.show()