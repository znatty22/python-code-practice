
def main():
	node_data = [10,6,15,11,16,7,5]
	root = Node(10)
	root.left= Node(8)
	root.right= Node(2)
	root.right.left = Node(2)
	root.left.left = Node(3)
	root.left.right= Node(5)
	bst = BinarySearchTree(root)
	#bst = BinarySearchTree()
	#bst.build_from_list(node_data)
	bst.print_level_order()
	print 'All paths...'
	print '\n'.join(bst.all_paths())

class Node:
	def __init__(self,key=None,left=None,right=None):
		self.key = key
		self.left = left
		self.right = right
		self._data = {}
	
	def __str__(self):
		#return 'Node: %s, data = %s' % (str(self.key),str(self._data))
		return str(self.key)
		
class BinarySearchTree:
	def __init__(self,root=None):
		self.root = root
	
	def build_from_list(self,node_list):
		for n in node_list:
			self.insert(n)
	
	def is_empty(self):
		return (self.root == None)
	
	def all_paths(self):
		paths = []
		path = []
		if self.is_empty():
			return paths
		self._all_paths(self.root,path,paths)
		
		return paths
	
	def _all_paths(self,node,path,paths):
		if not node:
			return
		# Append node to path
		path.append(str(node))
		# Check for leaf
		if (not node.left) and (not node.right):
			paths.append(','.join(path))
		else:
			self._all_paths(node.left,path,paths)
			self._all_paths(node.right,path,paths)
		path.pop()
		
	def insert(self,key):
		if self.is_empty():
			self.root = Node(key)
		else:
			# Search for node by key
			node = self.find(key)
			# Node already exists
			if key == node.key:
				print 'Node %s already exists!' % str(key)
				return
			# Insert as left child
			elif key <= node.key:
				node.left = Node(key)
			# Insert as right child
			else:
				node.right = Node(key)
				
	def find(self,key):
		if self.is_empty():
			return self.root
			
		return self._find(self.root,key)
	
	def _find(self,node,key):
		# Go left
		if key <= node.key:
			if node.left:
				return self._find(node.left,key)
			else: 
				return node
		# Go right
		elif key > node.key:
			if node.right:
				return self._find(node.right,key)
			else: 
				return node
				
	def __str__(self):
		output = []
		self._inorder(self.root,output)
		return ','.join(output)
	
	def print_level_order(self):
		print '\nLevel order'
		print self._level_order()
	
	def _level_order(self):
		output = []
		if self.is_empty():
			return str(output)
		from Queue import Queue
		q = Queue()
		q.put(self.root)
		
		while(not q.empty()):
			current = q.get()
			output.append(str(current))
			if current.left:
				q.put(current.left)
			if current.right: 
				q.put(current.right)
				
		return ','.join(output)
	
	def _inorder(self,node,output):
		if not node:
			return
		self._inorder(node.left,output)
		output.append(str(node))
		self._inorder(node.right,output)
			
if __name__ == '__main__':
	main()