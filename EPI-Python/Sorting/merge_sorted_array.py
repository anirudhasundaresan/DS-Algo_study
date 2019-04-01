#  this is a naive implementation of merge sort
def merge_sort(arr1, arr2):
    i, j = 0, 0
    res = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            res.append(arr2[j])
            j += 1
            if j == len(arr2):
                res.extend(arr1[i:])
        else:
            res.append(arr1[i])
            i += 1
            if i == len(arr1):
                res.extend(arr2[j:])
    return res


ar1 = [1, 3, 5, 7, 9]
ar2 = [2, 4, 6, 8, 9, 10, 12, 14]
print(merge_sort(ar1, ar2))


# what if you cannot use a spare array, and assume that you have the space needed to make the sorted union at the end of
# one of the arrays
ar1 = [1, 3, 5, 7, 9, '', '', '', '', '', '', '', '', '', '', '', '']
ar2 = [-5, -1, 1, 2, 4, 6, 8, 9, 10, 12, 14, 15]

#  time complexity: O(n+m); space complexity: O(1)
def merge_constrained(arr1, arr2):
    #  idea: start with a pointer at end of second array and a pointer at end of first array, but before the ''
    #  let us assume we know what array has the extra space
    j = len(arr2) - 1
    i = 0
    while arr1[i] != '':
        i += 1
    i -= 1
    place = len(arr1) - 1
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[place] = arr1[i]
            i -= 1
        else:
            arr1[place] = arr2[j]
            j -= 1
        place -= 1
    #  earlier loop breaks due to 2 possibilities - either i < 0 or j < 0; we care when j > 0 since that means j has
    #  smaller elements
    while j >= 0:
        arr1[place] = arr2[j]
        place -= 1
        j -= 1
    return arr1


print(merge_constrained(ar1, ar2))
