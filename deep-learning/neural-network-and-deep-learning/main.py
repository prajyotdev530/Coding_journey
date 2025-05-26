import numpy as np
import time as t
import random
size=1000000
x=np.random.rand(size)
y=np.random.rand(size)

start_manual=t.time()
sum1=0
for i in range(size):
    sum1+=x[i]*y[i]
end_manual=t.time()

start_vector=t.time()
sum2=np.dot(x,y)
end_vector=t.time()
print(sum1)
print(sum2)
print(f"the time for the manual calculation is{end_manual-start_manual}")
print(f"the time for the vector calculation is{end_vector-start_vector}")

