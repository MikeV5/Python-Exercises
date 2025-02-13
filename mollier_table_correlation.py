import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr,spearmanr

datiT=[5,10,15,20,30,40,60,80,100,150,200,250,300,374]
datiVi=[0.0179,0.0179,0.0179,0.0179,0.018,0.018,0.0183
        ,0.0185,0.0187,0.0196,0.207,0.0224,0.0252,0.057]


correlazioneP=pearsonr(datiT,datiVi)
correlazioneS=spearmanr(datiT,datiVi)


print("Pearson:",correlazioneP.statistic)
print("Spearman:",correlazioneS.statistic)


plt.scatter(datiT,datiVi)

plt.plot(np.unique(datiT),np.poly1d(np.polyfit(datiT,datiVi,1))(np.unique(datiT)))
plt.title('Vi')
plt.xlabel("T")
plt.ylabel("Vi")
plt.show()