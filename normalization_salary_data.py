import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from sklearn.metrics import r2_score

#Caricamento il file csv da github
df = pd.read_csv('https://raw.githubusercontent.com/MikeV5/BigData/main/Salary_Data.csv')

X = df[['YearsExperience']]
y = df['Salary']

model = LinearRegression()

#Addestra il modello
model.fit(X, y)

#Esegue le predizioni utilizzando i dati di addestramento
y_pred = model.predict(X)

w0 = model.intercept_  #L'intercetta della retta di regressione
w1 = model.coef_[0]  #Coefficiente di x della retta di regressione
print(f'w0 = {w0:.3f}')
print(f'w1 = {w1:.3f}')

#Calcolo coefficiente R^2
r2 = r2_score(y, y_pred)
print(f'R^2= {r2:.3f}')

#Genera 3 esempi casuali di anni di esperienza nel range di X
x_min = X['YearsExperience'].min()
x_max = X['YearsExperience'].max()

year_random = np.random.uniform(x_min,x_max, size=3)
random_df = pd.DataFrame({'YearsExperience': year_random})
new_y= model.predict(random_df)

for i in range(len(year_random)):
  print("Anni di esperienza: {:.1f} - Predizione salariale: {:.2f}".format(year_random[i], new_y[i]))

#Limiti dell'asse x con uno spazio aggiuntivo di 0.1
x_margin = 0.1 * (x_max - x_min)
plt.xlim(x_min - x_margin, x_max + x_margin)

#Limiti dell'asse y con uno spazio aggiuntivo di 0.1
y_min = y.min()
y_max = y.max()
y_margin = 0.1 * (y_max - y_min)
plt.ylim(y_min - y_margin, y_max + y_margin)

#Grafico
plt.scatter(X, y, color='b', s=10, label='Dati di addestramento')
plt.plot(X, w1*X + w0, color='r', label='Retta di regressione')
plt.xlabel('Years experience')
plt.ylabel('Salary')
plt.title('Years experience vs Salary')
plt.text(1, 110000, f"y = {w1:.4f}x + {w0:.4f}", fontsize=10)
plt.text(1, 100000, f"R^2 = {r2:.3f}", fontsize=10)
plt.legend()
plt.show()