from sklearn import model_selection
import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
import sklearn

data = pd.read_csv('https://raw.githubusercontent.com/Bogdan11031999/BigData/main/QI_randomMF_Eta_Fumo.csv')
X = data[['QI', 'Eta']]
y = data['Fuma']

# Suddivisione dei dati in set di addestramento e set di test
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=2)

# Creazione dell'istanza del modello di regressione logistica
model = LogisticRegression()

# Addestramento del modello
model.fit(X_train, y_train)

# Effettuare previsioni sul set di test
y_pred = model.predict(X_test)

# Calcolo dell'accuratezza del modello
accuracy = sklearn.metrics.accuracy_score(y_test, y_pred)
# Addestramento del modello
model.fit(X, y)
# Estrazione dei coefficienti e del termine noto del modello
coef = model.coef_[0]
intercept = model.intercept_

# Plot dei punti dati
plt.scatter(X['QI'], X['Eta'], c=y, cmap='rainbow')

# Calcolo dei valori sull'asse x per la decision boundary
x_boundary = np.linspace(X['QI'].min(), X['QI'].max(), 100)

# Calcolo dei valori sull'asse y per la decision boundary
y_boundary = -(coef[0] * x_boundary + intercept[0]) / coef[1]

# Plot della decision boundary
plt.plot(x_boundary, y_boundary, color='black')

# Impostazione delle etichette degli assi
plt.xlabel('QI')
plt.ylabel('Eta')

# Impostazione dei limiti degli assi
plt.xlim(X['QI'].min() - 1, X['QI'].max() + 1)
plt.ylim(10, 90)
plt.title('Età + QI vs Fumo - Accuratezza: {:.2f}'.format(accuracy))
# Mostra il grafico
plt.show()