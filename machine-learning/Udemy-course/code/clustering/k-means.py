import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv('/Users/prajyotmore/Downloads/study_material/Machine-Learning-A-Z-Codes-Datasets/Part 4 - Clustering/Section 24 - K-Means Clustering/Python/Mall_Customers.csv')
x=dataset.iloc[:,3:].values
print(x)
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
dataset['Genre']=le.fit_transform(dataset['Genre'])
from sklearn.cluster import KMeans
inertias=[]
k_range=range(1,11)
for k in k_range:
    model = KMeans(n_clusters=k,random_state=0)
    model.fit(x)
    inertias.append(model.inertia_)
print(inertias)
print(inertias.index(min(inertias)))
model=KMeans(n_clusters=5,init='k-means++',random_state=42)
labels=model.fit_predict(x)
centroids = model.cluster_centers_
print(labels)
print('hey')
print(centroids)

plt.scatter(x[labels==0,0],x[labels==0,1],color='red',label='Cluster 1')
plt.scatter(x[labels==1,0],x[labels==1,1],color='violet',label='Cluster 2')
plt.scatter(x[labels==2,0],x[labels==2,1],color='blue',label='Cluster 3')
plt.scatter(x[labels==3,0],x[labels==3,1],color='yellow',label='Cluster 4')
plt.scatter(x[labels==4,0],x[labels==4,1],color='pink',label='Cluster 5')
plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1],s=200,color='red',label='centers')
plt.legend()
plt.show()

for i, k in enumerate(k_range):
    plt.plot([k, k], [0, inertias[i]], color='gray', linestyle='--')  # vertical line
    plt.plot(k, inertias[i], 'bo')  # dot on top
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method with Sticks to X-axis')
plt.grid(True)
plt.show()



