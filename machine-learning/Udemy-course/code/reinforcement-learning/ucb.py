import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv('/Users/prajyotmore/Downloads/study_material/Machine-Learning-A-Z-Codes-Datasets/Part 6 - Reinforcement Learning/Section 32 - Upper Confidence Bound (UCB)/Python/Ads_CTR_Optimisation.csv')
print(dataset)
N=10000
d=10
ads_selected=[]
number_of_times_shown=[0]*d
number_of_times_selected=[0]*d
total_reward=0

for n in range(0,N):
    ad=0
    max_upper_bound = 0
    for i in range(0,d):
        if number_of_times_shown[i]>0:
            average_reward=number_of_times_selected[i]/number_of_times_shown[i]
            delta_i = np.sqrt(3 / 2 * np.log(n + 1) /number_of_times_shown[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound=1e400
        if upper_bound>max_upper_bound:
            max_upper_bound=upper_bound
            ad=i

        ads_selected.append(ad)
        number_of_times_shown[ad]+=1
        reward=dataset.iloc[n,ad]
        number_of_times_selected[ad]+=reward
        total_reward+=reward
plt.figure(figsize=(10,6))
plt.hist(ads_selected, bins=np.arange(d+1)-0.5, rwidth=0.7, color='skyblue', edgecolor='black')
plt.title('Histogram of ads selections using UCB')
plt.xlabel('Ad Index')
plt.ylabel('Number of times each ad was selected')
plt.xticks(range(d))
plt.grid(axis='y')
plt.show()




