def merge_(ar1, ar2):
    i, j = 0, 0
    new_ls = []
    while i < len(ar1) and j < len(ar2):
        if ar1[i] < ar2[j]:
            new_ls.append(ar1[i])
            i += 1
            if i == len(ar1):
                new_ls.extend(ar2[j:])
        else:
            new_ls.append(ar2[j])
            j += 1
            if j == len(ar2):
                new_ls.extend(ar1[i:])
    print(new_ls)
    return new_ls


def merge_sort(arr):
    res_ = [[x] for x in arr]
    while len(res_) != 1:
        res = [x for x in res_]
        print(res)
        res_ = []
        for i in range(0, len(res), 2):
            res_.append(merge_(res[i], res[i+1]))
        print(res_, '\n')
    return res_[0]


arr_ = [9, 2, 6, 5, 3, 10, 1, 7]
print(merge_sort(arr_))
# creating new arrays here, not a great solution: think how you can use the indices to sort elements in-place
