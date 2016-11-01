from Queue import Queue
'''
Invert a binary tree.
'''

def main():
	root = Node('a')
	root.left = Node('b')
	root.right = Node('c')
	root.left.left = Node('d')
	root.left.right = Node('e')
	root.left.right.right = Node('f')

	tree = BinaryTree(root)
	print 'Tree before: %s' % str(tree)
	invert(root)
	print 'Tree after %s' % str(tree)

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

	def __str__(self):
		output = []

		q = Queue()
		q.put(self.root)

		while(not q.empty()):
			current = q.get()
			output.append(str(current))

			if current.left:
				q.put(current.left)
			if current.right:
				q.put(current.right)

		return ''.join(output)
		

def invert(root):	
	if not root:
		return root

	q = Queue()
	q.put(root)

	while(not q.empty()):
		current = q.get()
		# Swap left and right
		temp = current.left
		current.left = current.right
		current.right = temp

		if current.left:
			q.put(current.left)
		if current.right:
			q.put(current.right)		

if __name__ == '__main__':
	main()