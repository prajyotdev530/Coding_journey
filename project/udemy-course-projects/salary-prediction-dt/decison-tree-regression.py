import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
dataset=pd.read_csv('/Users/prajyotmore/Downloads/study_material/Machine-Learning-A-Z-Codes-Datasets/Part 2 - Regression/Section 8 - Decision Tree Regression/Python/Position_Salaries.csv')
x=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values
dtr=DecisionTreeRegressor(random_state=0)
dtr.fit(x,y)
x_grid = np.arange(min(x), max(x), 0.01)
x_grid=x_grid.reshape((len(x_grid),1))
plt.scatter(x,y)

plt.plot(x_grid,dtr.predict(x_grid))

#plt.scatter([[6.5]],dtr.predict([[6.5]]))
plt.show()
