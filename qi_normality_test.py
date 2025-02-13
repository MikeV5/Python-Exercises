import pandas as pd
import numpy as np
from scipy.stats import kstest, norm
import matplotlib.pyplot as plt
dati = pd.read_csv("https://raw.githubusercontent.com/Bogdan11031999/BigData/main/QI_randomMF.csv") #carico il file csv da github
qi_maschi = dati["QI_Maschi"]#creo l'array con il QI dei maschi
qi_femmine = dati["QI_Femmine"]#creo l'array con il QI delle femmine
media_maschi = np.mean(qi_maschi)#calcolo il QI medio dei maschi
deviazione_standard_maschi = np.std(qi_maschi)#calcolo la deviazione standard dei maschi
media_femmine = np.mean(qi_femmine)#calcolo il QI medio delle femmine
deviazione_standard_femmine = np.std(qi_femmine)#calcolo la deviazione standard delle femmine
cdf_teorica_maschi = norm.cdf(qi_maschi, media_maschi, deviazione_standard_maschi)
cdf_teorica_femmine = norm.cdf(qi_femmine, media_femmine, deviazione_standard_femmine)
statistiche_maschi, p_value_maschi = kstest(qi_maschi, cdf_teorica_maschi, args=(media_maschi, deviazione_standard_maschi))
statistiche_femmine, p_value_femmine = kstest(qi_femmine, cdf_teorica_femmine, args=(media_femmine, deviazione_standard_femmine))
statistiche_maschi, p_value_maschi = kstest(qi_maschi, cdf_teorica_maschi)
statistiche_femmine, p_value_femmine = kstest(qi_femmine, cdf_teorica_femmine)

if p_value_maschi > 0.05:
    print("I dati dei maschi seguono una distribuzione normale con media {} e deviazione standard {}".format(media_maschi, deviazione_standard_maschi))
else:
    print("I dati dei maschi non seguono una distribuzione normale con media {} e deviazione standard {}".format(media_maschi, deviazione_standard_maschi))

if p_value_femmine > 0.05:
    print("I dati delle femmine seguono una distribuzione normale con media {} e deviazione standard {}".format(media_femmine, deviazione_standard_femmine))
else:
    print("I dati delle femmine non seguono una distribuzione normale con media {} e deviazione standard {}".format(media_femmine, deviazione_standard_femmine))

print()


# crea un array di valori x per le CDF teoriche
x = np.linspace(min(min(qi_maschi), min(qi_femmine)), max(max(qi_maschi), max(qi_femmine)), 1000)

# crea un istogramma dei dati dei maschi e delle femmine
plt.hist([qi_maschi, qi_femmine], bins=20, density=True, alpha=0.5, color=['blue', 'pink'])

# disegna le CDF teoriche per i maschi e per le femmine
plt.plot(x, norm.cdf(x, media_maschi, deviazione_standard_maschi), color='blue')
plt.plot(x, norm.cdf(x, media_femmine, deviazione_standard_femmine), color='pink')

# aggiungi etichette e titolo al grafico
plt.xlabel('QI')
plt.ylabel('Densità di probabilità')
plt.title('Distribuzione dei dati dei maschi e delle femmine e CDF teoriche')

# aggiungi una legenda al grafico
plt.legend(['CDF teorica maschi', 'CDF teorica femmine', 'Dati maschi', 'Dati femmine'])

# mostra il grafico
plt.show()