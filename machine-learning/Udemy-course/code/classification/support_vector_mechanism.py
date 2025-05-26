import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('/Users/prajyotmore/Downloads/study_material/Machine-Learning-A-Z-Codes-Datasets/Part 3 - Classification/Section 16 - Support Vector Machine (SVM)/Python/Social_Network_Ads.csv')
x=dataset.iloc[:,:-1].values
print(x)
y=dataset.iloc[:,-1].values
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)
from sklearn.svm import SVC
model=SVC(kernel='linear',random_state=0)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
from sklearn.metrics import confusion_matrix
cf=confusion_matrix(y_test,y_pred)
print(cf)
plt.scatter(range(len(y_test)),y_test,color='red')
plt.scatter(range(len(y_pred)),y_pred,color='blue',marker='x')
print(np.concatenate((y_test.reshape(-1,1),y_pred.reshape(-1,1)),axis=1))
plt.show()



