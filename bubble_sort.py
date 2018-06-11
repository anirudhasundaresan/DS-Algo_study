## http://interactivepython.org/courselib/static/pythonds/SortSearch/sorting.html
# Analysis criteria: Number of comparisons. And number of exchanges too.
# Note: swapping in Python can be done simultaneously (a,b = b,a) instead of assigning temporar variables.
# These are codes for sorting..

# Bubble sort: (my method with recursion) [In essence, each item ***bubbles*** up to the location where it belongs.]
# Try not to use recursion, unless it can be logarithmically bounded. Might lead to stack overflow.
# G4G says recursive BS does not have performance advantages..
def bubble_sort(alist):
    if len(alist)==1:
        lis.append(alist[0])
        return
    for i in range(len(alist)-1):
        j = i+1
        if alist[i] > alist[j]:
            alist[i], alist[j] = alist[j], alist[i]
    lis.append(alist[j]) # appending will take O(1) but insertion at the beginning everytime will shift the list everytime and hence more time ~O(N)
    bubble_sort(alist[:-1])
# this implementation is tail recursive and hence the compiler will identify and convert it into iterative procedure.

# Bubble sort: (their implementation without recursion)
def bubble_sort_iter(alist):
    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

lis = []
alist = [54,26,93,17,77,31,44,55,20]
bubble_sort(alist)
print(lis[::-1])
bubble_sort_iter(alist)
print(alist)

# performance: O(N2), is worst case if all the elements need to be exhanged.
# Where would Bubblesort be useful?
# When we need to know if the array is already sorted, the no. of exchanges would be 0 during a pass.
# Thus, for lists requiring only a few passes, this technique, only after a few passes, will figure out that the list has been sorted and thus, can be stopped.

## The above implementation: Short bubble
def bubble_sort_short(alist):
    for i in range(len(alist)-1):
        exchanges = False
        #print(i)
        #print(alist)
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                exchanges = True
        if exchanges == False:
            return alist

newlist = [17,20,26,54,93,77,31,44,55]
print(bubble_sort_short(newlist))
