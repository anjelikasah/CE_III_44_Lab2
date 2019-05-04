from insertionsort import insertion
import random
from time import time
import matplotlib.pyplot as plt
x,y=[],[]
sample_size=1000
for n in range(sample_size,sample_size*12,sample_size):
    randomvalues=random.sample(range(n),n)
    start_time=time()
    i=insertion(randomvalues)
    end_time=time()
    total_time=end_time-start_time

    x.append(n)
    y.append(total_time)

print(x)
print(y)

plt.plot(x,y)
plt.show()
