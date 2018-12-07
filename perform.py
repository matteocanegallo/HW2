import time
from mergesort import mergeSort
from quicksort import quickSort

import random

difference = []
for i in range(1,10):
    arr = []
    for x in range(1000):
        arr.append(random.randint(1,1000))
    s = time.time()
    quickSort(arr, 0, len(arr)-1)
    e = time.time()
    time1 = e-s
    s = time.time()
    mergeSort(arr)
    e = time.time()
    time2 = e-s
    difference.append(time2-time1)
    print(i, "quickSort: ", time1, "mergeSort: ", time2)
    print( "The average difference in running time is: ", sum(difference)/len(difference))
