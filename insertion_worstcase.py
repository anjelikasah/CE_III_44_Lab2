from insertionsort import insertion
import random
from time import time
import matplotlib.pyplot as plt
x,y=[],[]
for n in range(2000,20000,2000):
    randomvalues=list(range(n))[::-1]
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
