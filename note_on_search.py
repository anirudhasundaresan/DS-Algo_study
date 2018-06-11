##  This is to compare different searches and their runtimes.
## Usually in Python, we use the "in" for searching..15 in [1,2,3,15,6,7] returns True.
## Linear search -- Worst case: O(n) and best case: Omega(1) if it is the first element. The list need not be sorted.
def lin_search(key, a):
    for index, i in enumerate(a):
        if i == key:
            print("Array element found at: ", index)
            return True
    print("Array element not found")
    return False

lis = [5, 4, 0, 9, 7, 6]
lin_search(10, lis)
lin_search(0, lis)
lin_search(9, lis)

## Binary search -- Worst case: O(log n) and best case: Omega(1) if the element found is the middle element itself.
## Note: the list has to be sorted

def binary_search(key, a):
    low = 0
    high = len(a)-1
    while high >= low:
        mid = int((high+low)/2.0)
        if a[mid] == key:
            print("Element found at position: ", mid)
            return True
        elif key > a[mid]:
            low = mid+1
        else:
            high = mid-1
    print("Element not found")
    return False

sort_list = sorted(lis)
# sort_list = [0, 4, 5, 6, 7, 9, 10]
binary_search(10, sort_list)
binary_search(6, sort_list)
binary_search(100, sort_list)

## Some more comparisons from Stack Overflow:
# Binary search requires an ordering comparison while linear search requires equality comparisons.
# Binary search requires random access to the data, whereas linear search requires only sequential access.
# This is important because linear search can "stream" data of arbitrary size.

# Another important note: Don't do sorting just to do binary search. The best sorting algorithms take O(n logn) [which is always slower than a linear search].
# Also consider a hash table in such situations.
