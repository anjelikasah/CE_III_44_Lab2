from insertionsort import insertion
import random
from time import time
import matplotlib.pyplot as plt
x,y=[],[]
sample_size=1000
for n in range(1000000,10000000,2000000):
    #randomvalues=random.sample(range(n),n)
    randomvalues=list(range(n))
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
