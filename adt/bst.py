from Queue import Queue

def main():
	bst = BinarySearchTree([8,2,1,3,5,10,11,9])
	print bst
	bst.print_level_order()

class BinarySearchTree:
	
	def __init__(self,nodes):
		self.root = None
		self.size = 0
		for d in nodes:
			self.insert(d)

	def __str__(self):
		nodes = []
		self._print_in_order(self.root,nodes)
		return str(nodes)

	def __len__(self):
		return self.size

	def __contains__(self,data):
		found = self.find(data)

		if not found or (found.data != data):
			return False
		else:
			return True	

	def is_empty(self):
		if not self.root:
			print 'Tree is empty!'
			return True
		else:
			return False

	def find(self,data,node=None):
		if self.is_empty():
			return None
		else:
			# Start at root
			if not node:
				node = self.root

			return self._find(data,node)

	def _find(self,data,node):
		# Data was found or we cannot traverse tree further	
		if (data == node.data):
			return node
		
		# Data is less than current, go left	
		elif data < node.data:
			if node.left:
				return self.find(data,node.left)
			else:
				return node

		# Data is greater than current, go right
		else:
			if node.right:
				return self.find(data,node.right)
			else:
				return node

	def insert(self,data):
		# Find returns parent node of where new node will be inserted as child
		found = self.find(data)
		
		# If found = None, tree was empty, insert at root
		if not found:
			print 'Creating root'
			self.root = Node(data)
		
		# Insert node as left or right child
		else:
			if found.data == data:
				print 'Cannot insert node ' + str(data) + ', already exists!'	
			elif data < found.data:
				found.left = Node(data,None,None,found)
			else:
				found.right = Node(data,None,None,found)
		self.size += 1


	def remove(self,data,node=None):
		found = self.find(data,node)
		# Data doesn't exist, cannot remove it
		if found and found.data != data:
			print 'Cannot remove '+ str(data) + ' does not exist'
		else:
			# Remove root
			if found == self.root:
				self.root = None
				return

			# Case 1: Node is a leaf
			if found.is_leaf():
				if found.parent.left and found.parent.left == found:
					found.parent.left = None
				else:
					found.parent.right = None

			# Case 3: Node has 2 children	
			elif (found.left and found.right):
				successor = self.min(found.right)
				self.remove(successor.data)
				found.data = successor.data

			# Case 2: Node has 1 child	
			else:
				# Get the target's child
				if found.left:
					child = found.left
				else:
					child = found.right

				# Target is a left child
				if found.parent.left == found:
					found.parent.left = child

				# Target is a right child
				else:
					found.parent.right = child


			self.size -= 1

	def find_successor(self,data,node=None):
		if not node:
			node = self.root
		self._find_successor(data,node)

	def _find_successor(self,data,node):
		pass
	
	def min(self,node=None):
		if not node:
			node = self.root

		return self._min(node)

	def _min(self,node):
		if (node.left == None):
			return node
		else:
			self._min(node.left)

	def max(self,node=None):
		if not node:
			node = self.root

		return self._max(node)

	def _max(self,node):
		if (node.right == None):
			return node
		else:
			self._max(node.right)			

	def print_level_order(self):
		if self.is_empty():
			return

		node_string = ''
		queue = Queue()
		queue.put(self.root)
		while (not queue.empty()):
			node = queue.get()
			node_string += str(node) + ' '
			if node.left:
				queue.put(node.left)
			if node.right:
				queue.put(node.right)

		print node_string			

	def print_in_order(self):
		nodes = []
		self._print_in_order(self.root,nodes)
		print nodes

	def _print_in_order(self,node,nodes):
		if not node:
			return
		
		# Recurse left
		self._print_in_order(node.left,nodes)
		
		# Print
		nodes.append(str(node)) 

		# Recurse right
		self._print_in_order(node.right,nodes)


class Node:
	def __init__(self,data,left=None,right=None,parent=None):
		self.parent = parent
		self.left = left
		self.right = right
		self.data = data

	def __str__(self):
		return str(self.data)

	def __eq__(self,other):
		return isinstance(self,other.__class__) and (self.data == other.data)

	def __lt__(self,other):
		return self.data < other.data

	def __gt__(self,other):
		return self.data > other.data	

	def is_leaf(self):
		return (self.left == None) and (self.right == None)	

if __name__ == '__main__':
	main()
