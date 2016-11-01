from Queue import Queue
'''
Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization 
algorithm should work. You just need to ensure that a binary tree 
can be serialized to a string and this string can be deserialized 
to the original tree structure.
'''
NULL_DELIMITER = '_'

def main():
	root = Node('a')
	root.left = Node('b')
	root.right = Node('c')
	root.left.left = Node('d')
	root.left.right = Node('e')
	root.left.right.right = Node('f')

	tree = BinaryTree(root)

	tree_str = serialize(tree)
	print 'Original tree %s' % tree_str
	print 'Deserializing...'
	tree = deserialize(tree_str)
	print serialize(tree)

class Node:

	def __init__(self,data=None,left=None,right=None):
		self.data = data
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.data)

class BinaryTree:

	def __init__(self,root=None):
		self.root = root

def deserialize(tree_string):
	tree = BinaryTree()
	if not tree_string:
		return tree

	data = list(tree_string)
	root = Node(data[0])
	q = Queue()
	q.put(root)
	i = 0
	while (not q.empty()):
		current = q.get()

		# Create left
		ldata = data[2*i+1]
		if ldata != NULL_DELIMITER:
			current.left = Node(ldata)
			q.put(current.left)

		# Create right
		rdata = data[2*i+2]
		if rdata!= NULL_DELIMITER:
			current.right = Node(rdata)
			q.put(current.right)

		i =i+1

	tree.root = root

	return tree

def serialize(tree):
	'''
	Convert tree into string. Traverse
	tree in level order and add each Node
	to output string
	'''

	output = []
	if tree.root:
		output.append(tree.root.data)

		# Level order traversal
		q = Queue()
		q.put(tree.root)

		while (not q.empty()):
			current = q.get()
			# Left node
			if current.left:
				output.append(current.left.data)
				q.put(current.left)
			else:
				output.append(NULL_DELIMITER)

			# Right node	
			if current.right:
				output.append(current.right.data)
				q.put(current.right)
			else:
				output.append(NULL_DELIMITER)

	return ''.join(output)	


if __name__ == '__main__':
	main()