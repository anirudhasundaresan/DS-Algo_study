## Reference: http://interactivepython.org/runestone/static/pythonds/Trees/toctree.html
'''
Objectives: 
- Understand trees and how it is used
- Implement a map data structure using trees
- Implement trees using list 
- Implement trees using classes and reference
- Implement trees as a recursive data structure
- Implement a priority queue using a heap
'''
'''
#### Implement tree as a list of lists ####
def BinaryTree(r):
	return [r, [], []]

def insertLeft(root, newBranch):
	t = root.pop(1) # root here corresponds to root_list
	if len(t)>1:
		root.insert(1,[newBranch,t,[]])
	else:
		root.insert(1,[newBranch,[],[]])
	return root

def insertRight(root, newBranch):
	t=root.pop(2)
	if len(t)>1:
		root.insert(2,[newBranch,[],t])
	else:
		root.insert(2,[newBranch,[],[]])
	return root

def getRootVal(root):
	return root[0]

def setRootVal(root, newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))
#### Implementation Done ####
'''


#### Implement tree using nodes and references, classes ####
class BinaryTree:
	def __init__(self, rootObj):
		self.key = rootObj # can be a reference to another object 
		self.LeftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if self.LeftChild==None:
			self.LeftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.LeftChild = self.LeftChild
			self.LeftChild = t

	def insertRight(self, newNode):
		if self.rightChild==None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.LeftChild

	def setRootVal(self, obj):
		self.key = obj

	def getRootVal(self):
		return self.key

'''
r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
#### Implementation Done ####
'''

#### Parse tree to read and evaluate expressions and also for sentence constructs #### -- my guesses
'''
- How to build a parse tree from a fully paranthesized mathematical expression (reading from a stack?, well not really, using stack to store the parent node, because we need to get back to root at times) 
- How to evaluate an expression stored in a parse tree (def inside recursions?, yes but no new defs, check sol.)
- How to recover original mathematical exprerssion stored in a parse tree (using stacks?)

## Building a parse tree from an expression: 
Has 4 main items/ tokens: (,),operators and operands.
Whenever we see a left paranthesis, we know a new expression/ new tree is coming up. Hence, create a new tree.
When we read a right paranthesis, we know that tree is ending. Also, operands are always the leaves and are children of the operators. Every operator will have a left child and a right child.

Algo to build: 
If '(' --> add a new node as left child of the current node and descent to left child.
If 'operand' --> set root value of current node to operand and return to parent
If 'operator' --> set root value of current node to operator, add a new node to the right and descend to it. 
If ')' --> just return to the parent of the current node.

# NOTE: we need to keep track of the current node as well as the parent of the current node.
Current node can be used by utilizing the left node and the right node references in the tree node class, but to get the parent node, we need to use a stack to hold values.
So, when you are on a node, push it to a stack, then descend to child nodes and then when you want to go back, pop the parent node!
'''
'''

def buildParseTree(fpexp): # expression is passed
	fplist = fpexp.split()
	pstack = [] # or call a stack class __init__
	eTree = BinaryTree('') # init a tree with just one root node and with no value in it.
	# print(eTree.key) # this works
	pstack.append(eTree)
	currentTree = eTree
	for i in fplist:
		if i =='(':
			currentTree.insertLeft('')
			pstack.append(currentTree)
			currentTree = currentTree.getLeftChild() # don't forget the paranthesis
		elif i == ')':
			currentTree = pstack.pop()
		elif i in ['+','-','*','/']:
			currentTree.key = i
			pstack.append(currentTree)
			currentTree.insertRight('')
			currentTree = currentTree.getRightChild()
		elif i not in ['+','-','/','*',')']:
			currentTree.key = i
			currentTree = pstack.pop()
		else:
			raise ValueError # when getting a token we do not recognize
	return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )") # pt will contain the root node now
# pt.postorder()  #defined and explained in the next section

### Evaluating a parsetree is postorder traversal --> left, right, root

'''
# How to evaluate the expression in this tree? -- Use recursion and always for recursion, get the base cases right first.
# Here, the base case for a tree will always be a leaf node and for a parse tree, the base case will always be a operand.

'''
import operator 
def evaluate(parseTree): # here, root of the entire tree is passed on as 'parseTree'
	# define a dictionary for convenience. 
	opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv} # all from the operator module in Python

	if parseTree.LeftChild and parseTree.rightChild:
		fn = opers[parseTree.key]
		return fn(evaluate(parseTree.LeftChild), evaluate(parseTree.rightChild))
	else:
		return int(parseTree.key) # needs int casting because it is a string by default. 

print(evaluate(pt)) # prints out 45

'''
'''
##### Tree traversals ##### (Traversal algo works for trees with any no. of children, but here we look only at binary trees)
Different order in which nodes can be traversed in a binary tree. These are all DFS algos. BFS uses Queue and DFS uses stacks.
- preorder: root, left, right
- inorder: left, root, right
- postorder: left, right, root
'''
# there are 2 methods to write a traversal: external OR internal (inside the class)
# external: 
def preorder(tree):
	if tree:
		print(tree.key)
		preorder(tree.LeftChild)
		preorder(tree.rightChild)

# internal
def preorder_int(self):
	print(self.key)
	if self.LeftChild:
		self.LeftChild.preorder_int()
	if self.rightChild:
		self.rightChild.preorder_int()

# Which is better? Most of the time, we have to do some other function on the trees rather than only traversing, hence external functions will be better. Hence, now onwards write only external functions. 

def postorder(tree):
	if tree:
		postorder(tree.LeftChild)
		postorder(tree.rightChild)
		print(tree.key)

# Now, write the evaluate function modeled on the postorder..

def postordereval(tree):
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
	res1 = None
	res2 = None
	if tree:
		res1 = postordereval(tree.LeftChild)
		res2 = postordereval(tree.rightChild)
	if res2 and res1:
		return opers[tree.key](res1, res2)
	else:
		return int(tree.key)

def inorder(tree):
	if tree:
		inorder(tree.LeftChild)
		print(tree.key)
		inorder(tree.rightChild)

## do a inorder parse expression build
def printexp(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      # printexp puts paranthesis around each number 
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal
