import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
dataset=pd.read_csv('/Users/prajyotmore/Downloads/study_material/Machine-Learning-A-Z-Codes-Datasets/Part 8 - Deep Learning/Section 39 - Artificial Neural Networks (ANN)/Python/Churn_Modelling.csv')

dataset=dataset.drop(['RowNumber','CustomerId','Surname'],axis=1)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
dataset['Gender']=le.fit_transform(dataset['Gender'])


X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values
print(X[1,:])
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ce=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[1])],remainder='passthrough')
X=ce.fit_transform(X)
print(X[1,:])
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(x_train)
X_test=sc.transform(x_test)
ann=tf.keras.models.Sequential()
ann.add(tf.keras.layers.Dense(units=6,activation='relu'))
ann.add(tf.keras.layers.Dense(units=6,activation='relu'))
ann.add(tf.keras.layers.Dense(units=1,activation='sigmoid'))  #if more than binary then the activation is softmax
ann.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy']) #if not binary then the loss is categorical_crossentroy
ann.fit(X_train,y_train,batch_size=128,epochs=100)
ann.predict(X_test)
print(X_test)

print(ann.predict(sc.transform([[1,0,0,600,1,40,3,60000,2,1,1,50000]])))


