import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
data=pd.read_csv('/Users/prajyotmore/Downloads/study_material/Machine-Learning-A-Z-Codes-Datasets/Part 3 - Classification/Section 14 - Logistic Regression/Python/Social_Network_Ads.csv')
print(data)
x=data.iloc[:,0:-1].values
y=data.iloc[:,-1].values
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)

sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)
model=LogisticRegression()
model.fit(x_train,y_train)
y_predict=model.predict(sc.inverse_transform(x_test))
print(np.concatenate((y_predict.reshape(len(y_predict),1),y_test.reshape(len(y_test),1)),1))

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_predict)
print(cm)
from sklearn.metrics import classification_report
print(classification_report(y_test,y_predict))
from sklearn.metrics import r2_score
r2=r2_score(y_test,y_predict)
print(r2)