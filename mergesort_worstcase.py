from mergesort import mergeSort
import random
from time import time
import matplotlib.pyplot as plt
x,y=[],[]
for n in range(20000,200000,20000):
    randomvalues=list(range(n))[::-1]
    start_time=time()
    i=mergeSort(randomvalues,0,len(randomvalues)-1)
    end_time=time()
    total_time=end_time-start_time

    x.append(n)
    y.append(total_time)

print(x)
print(y)

plt.plot(x,y)
plt.show()
