from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


dataset=pd.read_csv('/Users/prajyotmore/Documents/Coding-Journey/machine-learning/Udemy-course/study-material/Machine-Learning-A-Z-Codes-Datasets/Part 2 - Regression/Section 4 - Simple Linear Regression/Python/Salary_Data.csv')
print(dataset)
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values
print((X))
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
model=LinearRegression()
model.fit(X_train,Y_train)
Y_pred=model.predict(X_test)
print(model.predict([[15]]))
plt.scatter(X_train,Y_train,color='red')
#plt.scatter(X_test,Y_pred,color='blue',marker='x')
plt.plot(X_train,model.predict(X_train),color='green')
plt.show()
