arr_ = [4, 5, 6, 7, 7.5, 8, 0, 1, 2, 3, 3.3, 3.5, 3.7, 3.8, 3.9, 3.98, 3.99]
arr1 = [1, 3, 5, 6.5, 7, 6, 4, 2, 1.1, 0.9, 0.7, 0]
#  strictly increasing and then decreasing - find the maximum/ peak of this array


#  find the position of the smallest element in the cyclically sorted array
def search_cyclic(arr):
    #  idea: find where the smallest element occurs using binary search
    #  Time complexity: O(log n)
    lo, hi = 0, len(arr) - 1
    small = None
    while lo <= hi:
        mid = (hi + lo) // 2  # to prevent overflow; need to subtract and then add: (hi-lo)//2 + lo
        if arr[mid] > arr[mid+1]:
            small = mid + 1
            break
        elif arr[mid] > arr[hi]:
            #  key step: to check with the rightmost or leftmost element.
            lo = mid + 1
        else:
            hi = mid - 1
    return small


def peak_find(arr):
    #  this is also O(log n)
    lo = 0
    hi = len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid] > arr[mid + 1]:
            hi = mid
        elif arr[mid] > arr[mid - 1]:
            lo = mid


def find_pos(arr, k):
    #  find position of element k in cyclically sorted array
    #  once you find the minimum element, then search only one part of the array (again using binary search) for k
    small = search_cyclic(arr)
    lo = 0
    hi = len(arr) - 1
    if k == arr[small]:
        return small
    elif k > arr[small]:
        lo = small
    else:
        hi = small
    #  do normal binary search on sorted array
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            hi = mid
        else:
            lo = mid


print(search_cyclic(arr_))
print(peak_find(arr1))
print(find_pos(arr_, 3.7))







