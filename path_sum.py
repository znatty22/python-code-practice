from Queue import Queue

def main():
	node_data = [10,7,6,15,9,11]
	bst = BinarySearchTree()
	bst.build_from_list(node_data)
	#bst.print_level_order()
	#test_max_depth(bst)
	test_min_depth(bst)

def test_min_depth(bst):
	print 'Min depth: %d' % bst.min_depth()	
	
def test_max_depth(bst):
	print 'Max depth: %d' % bst.max_depth()

def test_path_sum(bst):
	path_sum = 23
	found = str(bst.is_path_sum(path_sum))
	print '\nDoes path sum %d exist: %s ' % (path_sum,found)
	
class Node:
	def __init__(self,key=None,left=None,right=None):
		self.key = key
		self.left = left
		self.right = right
		self._data = {'path_sum':self.key if self.key else 0}
	
	def is_leaf(self):
		return ((not self.left) and (not self.right))
	
	def inc_path_sum(self,value):
		self._data['path_sum']+= value
	
	def get_path_sum(self):
		return self._data['path_sum']
	
	def __str__(self):
		return 'Node: %s, data = %s' % (str(self.key),str(self._data))
	
class BinarySearchTree:
	def __init__(self,root=None):
		self.root = root
	
	def build_from_list(self,node_list):
		for n in node_list:
			self.insert(n)
			
	def is_empty(self):
		return (self.root == None)
		
	def min_depth(self):
		# Length of shortest path
		depth = 0
		if self.is_empty():
			return min_depth
		
		q = Queue()
		q.put(self.root)
		
		while(not q.empty()):
			current = q.get()
			if current.is_leaf():
				return depth
			else:
				depth+=1
				if current.left:
					q.put(current.left)
				if current.right:
					q.put(current.right)
		
	def max_depth(self):
		max_depth = 0
		if self.is_empty():
			return max_depth
			
		return self._max_depth(self.root)
	
	def _max_depth(self,node):
		if not node:
			return 0
		else:
			return max(self._max_depth(node.left),self._max_depth(node.right)) + 1	
		
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
			if key < node.key:
				node.left = Node(key)
				node.left.inc_path_sum(int(node.get_path_sum()))
			# Insert as right child
			else:
				node.right = Node(key)
				node.right.inc_path_sum(int(node.get_path_sum()))
	
	def is_path_sum(self,path_sum):
		found = False
		if not self.is_empty():
			found = self._is_path_sum(self.root,path_sum)
		return found
	
	def _is_path_sum(self,node,path_sum):
		if not node:
			return False
		if node.is_leaf() and (int(node.get_path_sum()) == int(path_sum)):
			return True
		
		return (self._is_path_sum(node.left,path_sum) or self._is_path_sum(node.right,path_sum))
		
	def find(self,key):
		if self.is_empty():
			return self.root
			
		return self._find(self.root,key)
	
	def _find(self,node,key):
		# Found it
		if key == node.key:
			return node
		# Go left
		if key < node.key:
			if node.left:
				return self._find(node.left,key)
			else: 
				return node
		# Go right
		else:
			if node.right:
				return self._find(node.right,key)
			else: 
				return node
				
	def __str__(self):
		output = []
		self._inorder(self.root,output)
		return '\n'.join(output)
	
	def print_level_order(self):
		print '\nLevel order'
		print self._level_order()
	
	def _level_order(self):
		output = []
		if self.is_empty():
			return '\n'.join(output)
		
		q = Queue()
		q.put(self.root)
		
		while(not q.empty()):
			current = q.get()
			output.append(str(current))
			if current.left:
				q.put(current.left)
			if current.right: 
				q.put(current.right)
				
		return '\n'.join(output)
	
	def _inorder(self,node,output):
		if not node:
			return
		self._inorder(node.left,output)
		output.append(str(node))
		self._inorder(node.right,output)
			
if __name__ == '__main__':
	main()