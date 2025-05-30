import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
dataset=pd.read_csv('/Users/prajyotmore/Downloads/study_material/Machine-Learning-A-Z-Codes-Datasets/Part 2 - Regression/Section 7 - Support Vector Regression (SVR)/Python/Position_Salaries.csv')
X=dataset.iloc[:,1:-1].values
Y=dataset.iloc[:,-1].values.reshape(-1,1)
sc=StandardScaler()
X=sc.fit_transform(X)
sc2=StandardScaler()
Y=sc2.fit_transform(Y)
Y=Y.reshape(len(Y),)
from sklearn.svm import SVR
svr_model=SVR(kernel='rbf')
svr_model.fit(X,Y)
print(sc2.inverse_transform(svr_model.predict(sc.transform([[6.5]])).reshape(-1,1)))
plt.scatter(sc.inverse_transform(X),sc2.inverse_transform(Y.reshape(-1,1)),color='red')
plt.scatter([[6.5]],sc2.inverse_transform(svr_model.predict(sc.transform([[6.5]])).reshape(-1,1)),color='blue',)
plt.plot(sc.inverse_transform(X),sc2.inverse_transform(svr_model.predict(X).reshape(-1,1)),color='green')
plt.show() 
