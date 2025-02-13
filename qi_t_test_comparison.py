import matplotlib.pyplot as plt
import numpy as np
import math
import statistics
from statistics import pstdev
from scipy import stats

#array contenenti quoziente intellettivo di uomini e donne
datiUomini = [130,113,111,117,122,118,120,120,114,112,116]
datiDonne = [119,126,130,130,121,121,117,139,120,120,114]
print("QI Uomini: " , datiUomini)
print("QI Donne: " , datiDonne)

#calcolo quantità di dati per uomini e donne
nDatiUomini = len(datiUomini)
nDatiDonne = len(datiDonne)
print("Quantità dati uomini: " , nDatiUomini)
print("Quantità dati donne: " , nDatiDonne)

#calcolo media quoziente intellettivo
mediaQIUomini = np.mean(datiUomini)
mediaQIDonne = np.mean(datiDonne)
print("media quoziente intellettivo uomini: " , mediaQIUomini)
print("media quoziente intellettivo donne: " , mediaQIDonne)

#calcolo deviazione standard
devStdUomini = statistics.pstdev(datiUomini)
devStdDonne = statistics.pstdev(datiDonne)
print("Deviazione st uomini: ", devStdUomini)
print("Deviazione st donne: ", devStdDonne)

#calcolo mediana
medianaUomini = statistics.median_low(datiUomini)
medianaDonne = statistics.median_low(datiDonne)
print("mediana uomini: " , medianaUomini)
print("mediana donne: " , medianaDonne)

#calcolo t value
devStdUomini_2 = pow(devStdUomini, 2)
devStdDonne_2 = pow(devStdDonne, 2)


t_numeratore = abs(mediaQIUomini - mediaQIDonne)
t_denominatore = math.sqrt(devStdUomini_2/nDatiUomini + devStdDonne_2/nDatiDonne)
t_value = t_numeratore/t_denominatore

print("t value: ", t)

#gradi di libertà
DF = nDatiDonne -1 + nDatiUomini-1
#100-alfa confidence level
alfa = 0.05

#livello di significatività P
P = stats.t.pdf(t_value,DF)
print(stat)

if P < alfa:
  print("test significativo")
else:
  print("test non significativo")
