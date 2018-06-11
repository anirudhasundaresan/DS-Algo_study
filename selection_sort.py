# To implement selection sort. Same as bubble sort but with lesser exchanges and same O(N2).
# Iterative procedure

def selection_sort(alist):
    for i in range(len(alist)-1):
        max = -np.inf
        pos = 0
        for j in range(len(alist)-i):
            if alist[j] > max:
                max = alist[j]
                pos = j
        print(alist)
        alist[pos], alist[len(alist)-i-1] = alist[len(alist)-i-1], alist[pos]
    return alist

alist = [54,26,93,17,77,31,44,55,20]
import numpy as np
print(selection_sort(alist))
