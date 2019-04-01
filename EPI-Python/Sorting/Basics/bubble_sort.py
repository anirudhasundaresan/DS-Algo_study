def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    return arr


# Time complexity: O(n^2)
arr_ = [5, 9, 2, 7]
print('Final sorted array: ', bubble_sort(arr_))
arr_ = [100, 5, 9, 2, 7, 1, 0, -1, 4, -100]
print('Final sorted array: ', bubble_sort(arr_))

