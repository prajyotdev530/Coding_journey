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
model=PolynomialFeatures(degree=10)
X_poly=model.fit_transform(X)
print(X_poly)
lin_regr=LinearRegression()
lin_regr.fit(X_poly,Y)
predict=lin_regr.predict(X_poly)
plt.scatter(X,Y,color='red')
plt.plot(X,predict,color='blue')
plt.xlabel('position')
plt.ylabel('salary')
plt.title('Salary vs Position')
print(lin_regr.predict(model.fit_transform([[6.5]])))
plt.scatter(6.5,lin_regr.predict(model.fit_transform([[6.5]])),color='violet')
plt.show()


