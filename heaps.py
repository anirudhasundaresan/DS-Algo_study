## Priority Queues with Binary Heaps:
'''
In a priority queue, FIFO, but on insertion, if the element has a high priority, it goes to the beginning. [If you implement this with lists and subsequent sorting, you will get O(nlogn) since the fastest sorting is O(nlogn)]
Using binary heaps, implementing these priority queues will take O(log n) only.
Heaps are generally expressed as a list internally, and we are going to see 'min-heap' where the smallest key is at the beginning.


- BinHeap() creates a new empty binary heap
- insert(k) adds a new item to the heap
- findMin() returns the item with the minimum key value, leaving item in the heap
- delMin() returns the item with the minimum key value, and removes the item from the heap
- isEmpty() returns true if the heap is empty, false otherwise
- size() returns the no. of items in the heap 
- buildHeap(list) builds a new heap from a list of keys
- Also, percUp and percDown for item reassignments during insert/ delete.


BINARY HEAP IMPLEMENTATION: 
- structure property 
- heap order property
- heap operations

- Structure Property: 
Take advantage of logaithmic property of binary tree.
In order to do that, we need it to be balanced.
Heap structure should be that of a complete binary tree so that the nodes are completed from left to right.
We can represent this using a single list.
The left nodes of a subtree with parent node at p, is at position 2p of the list and the right node is at 2p+1. Also, we can find the parent node from the child node. 
If child node is at n, parent node is at n//2 (python integer division).
While making this list, we use a 0 for starting, because then index=1 will correspond to the root of the tree. 
- Heap Order Property: For every node x with parent p, the key in p is smaller than or equal to the key in x. 
- Heap Operations:
'''

class BinHeap():
	def __init__(self):
		self.currentSize = 0
		self.heapList = [0] # we are using an element 0 for the beginning so that we can do integers

# for insert, we have to just append to the list; guarantees that it will maintain the complete tree property. But the heap order property (min at the top) might get violated, so write a new
# function percUp for insertion if it's a small element. Use percUp to compare the new incoming node with it's parent. If it is smaller, exchange with parent.
# So, most of the work in insertion is done by percUp, only list appending happens in def insert (data abstraction).

	def insert(self, k):
		self.heapList.append(k)
		self.currentSize +=1
		self.percUp(self.currentSize) # will take in the index of the newly added element.

	def percUp(self, i): # this could have been done with recursion, but aviod it if possible as it takes up space and readability decreases.
		# compare each node with its parent till the root if needed
		while i//2 > 0:
			if self.heapList[i] < self.heapList[i//2]:
				self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
			i = i//2

# for insertion - percolate upwards
# for deletion - percolate downwards. Why?

# for deletion of the minimum element, we remove the root and put the last element of the list as the root. Then, we need to check the order property. For that, use percDown, by finding and swapping
# with the minimum of the two child nodes if the root node is smaller than any of them.

	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[currentSize]
		self.heapList[currentSize]-=1
		self.heapList.pop()
		self.percDown(1)
		return retval

	def percDown(self, i):
		# can percolate down till the leaf nodes
		while (i*2) <= self.currentSize:
			mc = self.minChild(i) # to find the minimum child out of the 2 children
			if self.heapList[i] > self.heapList[mc]:
				self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i] 
			i = mc

	def minChild(self, i):
		if i*2 + 1 > self.currentSize:
			return i*2
		else:
			if self.heapList[i*2] < self.heapList[i*2 + 1]:
				return i*2
			else:
				return i*2 + 1

	# Buld a heap from a list of keys
	def buildHeap(self, alist):
		i = len(alist)//2 # to access the middle level of the tree
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while (i > 0):
			self.percDown(i)
			i = i -1

	## this is O(n); proof not shown but since we use i = len()//2 we are dealing with a list traversal smaller than log n.


bh = BinHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())