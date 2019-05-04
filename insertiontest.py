import time
import random
from insertionsort import insertion
A=[6,7,8,4,2]
print(A)
start=time.time()
insertion(A)
end=time.time()
print(A)
print("execution time",start-end)
