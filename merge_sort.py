## Merge sort ## DIVIDE AND CONQUER APPROACH - LIKE Quicksort
## Complexity is O(nlogn): n for merging two halves of an array into one and logn for splitting an array into halves till the end.
def merge_sort(alist):
	print("Splitting", alist)
	if len(alist)>1:
		mid = len(alist)//2
		lefthalf = alist[:mid] # requires O(k) and hence must be avoided, hence pass the mid point into the merge_sort..
		righthalf =alist[mid:]
		merge_sort(lefthalf)  # first, the left branch and then the right branch.
		merge_sort(righthalf)

		i=0
		j=0
		k=0

		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k] = lefthalf[i]
				i+=1
			else:
				alist[k] = righthalf[j]
				j+=1
			k+=1

		while i<len(lefthalf):
			alist[k]=lefthalf[i]
			i+=1
			k+=1
		while j<len(righthalf):
			alist[k]=righthalf[j]
			j+=1
			k+=1
	print("Merging", alist)

alist = [54,26,93,17,77,31,44,55,20]
merge_sort(alist)
print(alist)
