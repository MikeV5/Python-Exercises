import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from scipy.sparse import hstack
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('https://raw.githubusercontent.com/Bogdan11031999/BigData/main/ToDo_14_EmailSpam.csv')
X_train, X_test, y_train, y_test = train_test_split(data[['keyword', 'lunghezza', 'intestazion']], data['valida'], test_size=0.4, random_state=2)
gnb = GaussianNB()
cv = CountVectorizer()
X_train_cv = cv.fit_transform(X_train['keyword']).toarray()
X_test_cv = cv.transform(X_test['keyword']).toarray()
gnb.fit(X_train_cv, y_train)
y_pred = gnb.predict(X_test_cv)
print("Accurattezza modello:", metrics.accuracy_score(y_test, y_pred))