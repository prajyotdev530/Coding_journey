import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
dataset=pd.read_csv('/Users/prajyotmore/Downloads/study_material/Machine-Learning-A-Z-Codes-Datasets/Part 2 - Regression/Section 8 - Decision Tree Regression/Python/Position_Salaries.csv')
x=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values

model=RandomForestRegressor()
model.fit(x,y)
print(model.predict([[6.5]]))
x_grid=np.arange(min(x[:,0]),max(x[:,0]),0.1)
x_grid=x_grid.reshape((len(x_grid),1))
plt.scatter(x,y)
plt.plot(x_grid,model.predict(x_grid),color='red')
plt.scatter([[6.5]],model.predict([[6.5]]),color='blue')
plt.show()