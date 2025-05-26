import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVC


dataset=pd.read_csv('/Users/prajyotmore/Downloads/study_material/Machine-Learning-A-Z-Codes-Datasets/Part 3 - Classification/Section 17 - Kernel SVM/Python/Social_Network_Ads.csv')
x=dataset.iloc[:,0:-1].values
y=dataset.iloc[:,-1].values
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

model=SVC(kernel='rbf',random_state=0)
y_train=y_train.reshape(len(y_train),)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(y_pred)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),axis=1))
import socket
local_host=socket.gethostbyname('localhost')
print(local_host)


