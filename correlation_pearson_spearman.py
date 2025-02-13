from matplotlib import pyplot as plt
from scipy import stats

x = [-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3]
y = []

#Calcolo valore assoluto
for i in  x :
  y.append(abs(i))

#Coefficiente di correlazione di Pearson
pearson_rho,pvalue = stats.pearsonr(x,y)

#Conversione in float
rho_converted = '%f' % pearson_rho

#Coefficiente di correlazione di Spearman
spearman_rho, pvalue = stats.spearmanr(x,y)

plt.xlabel("x")
plt.ylabel("y =|x|")
plt.scatter(x,y)

print(" pearson coefficient:",rho_converted,"\n",
       "spearmnan rank coefficient:",spearman_rho)