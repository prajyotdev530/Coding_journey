import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

dataset=pd.read_csv("/Users/prajyotmore/Downloads/study_material/Machine-Learning-A-Z-Codes-Datasets/Part 2 - Regression/Section 6 - Polynomial Regression/Python/Position_Salaries.csv")
print(dataset.head())
print(dataset)
X=dataset.iloc[:,1:-1].values
Y=dataset.iloc[:,-1].values
model=LinearRegression()
model.fit(X,Y)
print(model.predict([[6.5]]))
import joblib
joblib.dump(model, 'model.pkl')
print("Model saved as model.pkl")


