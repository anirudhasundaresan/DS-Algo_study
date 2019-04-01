def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i  # maintains a sorted list of arr[:j] at every iteration of j
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        print(arr)
    return arr


arr_ = [24, 13, 9, 64, 7, 23, 34, 47]
print('Final sorted array: ', insertion_sort(arr_))
