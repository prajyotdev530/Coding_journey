import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
dataset=pd.read_csv('/Users/prajyotmore/Documents/Coding-Journey/machine-learning/Udemy-course/study-material/Machine-Learning-A-Z-Codes-Datasets/Part 1 - Data Preprocessing/Section 2 -------------------- Part 1 - Data Preprocessing --------------------/Python/Data.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1]
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])
print(X)
country_mapping = {'France': 0, 'Germany': 1, 'Spain': 2}

# Replace the country names using the mapping
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder

ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
le=LabelEncoder()
X=np.array(ct.fit_transform(X))
Y=le.fit_transform(Y)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
print(X_test)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train[:,3:]=sc.fit_transform(X_train[:,3:])
X_test[:,3:]=sc.transform(X_test[:,3:])
print(X_train)
print(X_test)
model=linear_model.LinearRegression()
model.fit(X_train,Y_train)
Y_pred=model.predict(X_test)
print(model.predict(X_test))
plt.scatter(range(len(Y_test)),Y_test,color='red')
plt.scatter(range(len(Y_pred)),Y_pred,color='blue',marker='x')
plt.legend(['Actual','Predicted'])
plt.title('car buy prediction')
plt.show()


