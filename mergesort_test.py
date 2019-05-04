import time
import random
from mergesort import mergeSort
A=[6,7,8,4,2]
print(A)
start=time.time()
mergeSort(A,0,len(A)-1)
end=time.time()
print(A)
print("execution time",start-end)
