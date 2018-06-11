# This is for the insertion sort implementation
# This also takes O(N2). Although that is the case, insertion sort is preferred over the prev 2 since here, no exchanged but only shiftingself.
# A shifting operation takes 1/3rd the time for exchange because only one assignment is performed in shifting, whereas in exchanging, 3 assignments are performed.

def insertion_sort(alist):
    # start with only one element in the list
    for i in range(1, len(alist)):
        print(alist)
        for j in range(i):
            if alist[j] > alist[i]:
                alist[j], alist[i] = alist[i], alist[j]
    return alist
alist = [54,26,93,17,77,31,44,55,20]
print(insertion_sort(alist))
