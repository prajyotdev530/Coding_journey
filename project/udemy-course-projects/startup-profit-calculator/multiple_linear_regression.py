import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

dataset=pd.read_csv('/Users/prajyotmore/Documents/Coding-Journey/machine-learning/Udemy-course/study-material/Machine-Learning-A-Z-Codes-Datasets/Part 2 - Regression/Section 5 - Multiple Linear Regression/Python/50_Startups.csv')
print(dataset)
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
imputer.fit(X[:,0:2])
X[:,0:2]=imputer.transform(X[:,0:2])
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[3])],remainder='passthrough')
X=np.array(ct.fit_transform(X))
print(X)
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train[:,3:]=sc.fit_transform(X_train[:,3:])
X_test[:,3:]=sc.transform(X_test[:,3:])
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,Y_train)
Y_predict=model.predict(X_test)
print(X_train.shape)
print(Y_train.shape)
plt.scatter(range(len(Y_test)),Y_test,color='red')
plt.scatter(range(len(Y_predict)),Y_predict,color='blue',marker='x')
plt.show()
print(np.concatenate((Y_test.reshape(len(Y_test),1),Y_predict.reshape(len(Y_predict),1)),axis=1))

plt.show()
