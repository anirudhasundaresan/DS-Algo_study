##  This is to compare different searches and their runtimes [also about Hashesa nd hashtables & collisions].
## Usually in Python, we use the "in" for searching..15 in [1,2,3,15,6,7] returns True.

## Also note that if the list is ordered and we want to use 'linear search', we need to search for the value just greater than the key since every other value will be greater than key.
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
## Binary search can be implemented in a recursive method.

def binary_search(key, a):
    low = 0
    high = len(a)-1
    while high >= low:
        mid = int((high+low)/2.0) ## OR use mid = (high + low)//2
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

'''
# Some more comparisons from Stack Overflow:
Binary search requires an ordering comparison while linear search requires equality comparisons.
Binary search requires random access to the data, whereas linear search requires only sequential access.
This is important because linear search can "stream" data of arbitrary size.
Another important note: Don't do sorting just to do binary search. The best sorting algorithms take O(n logn) [which is always slower than a linear search].
Also consider a hash table in such situations.
Derivation of O(log n) for binary search: n/2 elements each time to be searched for...till n/2(power i) = 1.
Thus, i = log n
'''

'''
# NOW, let us look at the concept of hashing:
Hashing can be used for searching in O(1) time.
http://interactivepython.org/courselib/static/pythonds/SortSearch/Hashing.html
An m-slot hash table can be built on a List in Python...And each element of the list is None initially.
Thus, to store a list of numbers so that they can be easily searchable later on, we need to pass it through the hash function which returns a number between 0 and m (including m-1)
Whatever this outputs is the location at which that no. is stored in the list. Typically, all hash functions include some sort of remainder function since the output must be in range(m).

What is load factor?
If only 6 of the 11 elements of the list are filled, then 6/11 is the load factor. (No. of items/ Table size).
Constant time for indexing the value and constant time for lookup. So total searching is in O(1). So far, so good.
Ideally, we need a perfect hash function that outputs a unique hash value for each item, but if the values are not predetermined, then it is impossible to tell if the
hash function is perfect or not. Not to worry! Still, performance efficiency will be maintained! How?

How to define a hash function?
There are a number of ways, 'folding' method, 'mid-sqaure' method, etc.
Computing the slot must be efficient. That is, computation of the hash values must not take more time than binary search, else no purpose.
Always some form of the remainder function will be used to compute the hash value.
For strings, ord(each letter) add them up and %11? if the len(list for storage of slots) = 12. This will fail with anagrams, hence use weighted summing of the ord() returns.

How do we handle collisions?
Why is this important? Because hash functions are not always perfect. There might be a single slot for 2 different values.
Open addressing and linear probing will solve this issue. But, main issue with this: item might tend to get clustered, due to many getting the same output from the hash function
Linear probing at the end of the list is continued at the start (cyclic probing actually).

How to deal with clustering?
Instead of using linear probe with skip=1, use skip=3. And use the table size = prime no. so that all the slots can be reached at one point or the other.
A skip=3 proble means that if a slot is occupied, it looks at the slot 3 steps later (again, in a cyclic manner).
This process is called rehashing.In general, rehash(pos) = (pos+skip)%tablesize.

Any other methods apart from rehashing using linear probing?
Yes! - Quadratic probing and Chaining...

Quadratic Probing - Uses a non-constant skip (linear probing used constant skip) of successive perfect squares.
Chaining - In the case of collisions, items can be appended to a list (can be linked list) at each slot. Each slot has a reference to a chain of items. This can better for small
number of collisions.
'''

'''
The abstract datatype in Python called 'Map' can be implemented using hash tables...
'''
# Let us create a class for hashtable with some slots
class HashTable():
    def __init__(self):
        self.size = 11 # better for it to be a prime no. so that all slots would be eventually covered
        # creating two parallel lists, one for holding the keys and one for holding the data
        self.slots = [None] * self.size # note that this list is for the keys bnecause kesy calculate the slot numbers here. Data is just for entry.
        self.data = [None] * self.size

    def hashfunction (self, key, size):
        return key%size

    def rehash(self, oldhash, size): # no need of key, because it has already been used to get the oldhash
        return (oldhash+1)%size # or use whatever the step is..

    def put(self, key, data): # this is to insert a new key-value pair
        hashvalue = self.hashfunction(key, len(self.slots))
        # if this place is empty, put value here
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot]!=key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data # replacing

    def get(self, key): # get data from a key just like in a dictionary
        startslot = self.hashfunction(key, len(self.slots))
        position = startslot
        found = False
        stop = False
        data = None
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

# to allow acces to function using [], use __init__, those underscores in their names.
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)

H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)
print(H[20])
print(H[17])
H[20] = "duck"
print(H[20])
H.data
print(H[99])
