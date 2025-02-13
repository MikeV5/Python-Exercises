import numpy as np
from matplotlib import pyplot as plt
import statistics
from numpy import mean
from scipy.stats import norm
#Dati per il produttore A
datiA=[85,85,80,70,70,60,55,50,40,40,30,30,20,20,10]

#Dati per il produttore B
datiB=[50,50,50,50,50,50,50,50,50,50,50,50,50,50,49]

#Media e deviazione standard per ogni produttore
mediaA=mean(datiA)
mediaB=mean(datiB)
devStdA=statistics.pstdev(datiA)
devStdB=statistics.pstdev(datiB)
print('Produttore A - Media: {:.2f}, Deviazione standard:{:.2f}'.format(mediaA,devStdA))
print('Produttore B - Media: {:.2f}, Deviazione standard:{:.2f}'.format(mediaB,devStdB))

#funzione per calcolare distribuzione normale
def dnorm(x,mean=0,sd=1):
  from scipy.stats import norm
  result=norm.pdf(x,loc=mean,scale=sd)
  return result

#calcolo distribuzione normale per il produttore A (distNormA = norm.pdf(datiA, mediaA, devStdA))
distNormA = list()
tmp = 0
for count in range (15):
  tmp = dnorm(datiA[count],mediaA,devStdA)
  distNormA.append(tmp)
  count += 1

#calcolo distribuzione normale per il produttore B (distNormB = norm.pdf(datiB, mediaB, devStdB))
distNormB = list()
tmp = 0
for count in range (15):
  tmp = dnorm(datiB[count],mediaB,devStdB)
  distNormB.append(tmp)
  count += 1

#Rappresentazione della distribuzione gaussiana per il produttore A
plt.plot(datiA, distNormA, label="Produttore A")
plt.legend()
plt.xlabel("Vita batteria (in mesi)")
plt.ylabel("Densità di Probabilità")
plt.show()

#Rappresentazione della distribuzione gaussiana per il produttore B
plt.plot(datiB, distNormB, label="Produttore B")
plt.legend()
plt.xlim(0, 100)
plt.xlabel("Vita batteria (in mesi)")
plt.ylabel("Densità di Probabilità")
plt.show()