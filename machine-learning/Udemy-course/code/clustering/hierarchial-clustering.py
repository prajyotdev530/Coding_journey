import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv('/Users/prajyotmore/Downloads/study_material/Machine-Learning-A-Z-Codes-Datasets/Part 4 - Clustering/Section 24 - K-Means Clustering/Python/Mall_Customers.csv')
x=dataset.iloc[:,3:5].values
import scipy.cluster.hierarchy as sch
dendogram=sch.dendrogram(sch.linkage(x, method="ward"))
plt.xlabel('Customers')
plt.ylabel('eucledian distance')
plt.show()
from sklearn.cluster import AgglomerativeClustering
model=AgglomerativeClustering(n_clusters=5)
model.fit(x)
y_pred=model.labels_
print(model.labels_)
plt.scatter(x[y_pred==0,0],x[y_pred==0,1],color='blue',label='Cluster 1')
plt.scatter(x[y_pred==1,0],x[y_pred==1,1],color='yellow',label='Cluster 2')
plt.scatter(x[y_pred==2,0],x[y_pred==2,1],color='red',label='Cluster 3')
plt.scatter(x[y_pred==3,0],x[y_pred==3,1],color='yellow',label='Cluster 4')
plt.scatter(x[y_pred==4,0],x[y_pred==4,1],color='pink',label='Cluster 5')
plt.legend()
plt.show()



