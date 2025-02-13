import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Caricamento dati dal file CSV
data = pd.read_csv('https://raw.githubusercontent.com/Bogdan11031999/BigData/main/ToDo_14_EmailSpam.csv')

#Set di addestramento e test
X_train, X_test, y_train, y_test = train_test_split(data[['keyword', 'lunghezza', 'intestazion']], data['valida'], test_size=0.4, random_state=2)

# Codifica della colonna 'keyword'
X_trainCodifica = pd.get_dummies(X_train, columns=['keyword'])
X_testCodifica = pd.get_dummies(X_test, columns=['keyword'])

#Allineamento di X_trainCodifica e X_testCodifica
X_trainCodifica, X_testCodifica = X_trainCodifica.align(X_testCodifica, join='outer', axis=1, fill_value=0)

model = DecisionTreeClassifier() #si crea il modello con albero decisionale
model.fit(X_trainCodifica, y_train) #Addestramento del modello

y_pred = model.predict(X_testCodifica) #previsioni sul set di test

accuratezza = accuracy_score(y_test, y_pred) #Accuratezza del modello
print("Accurattezza modello:", accuratezza)
