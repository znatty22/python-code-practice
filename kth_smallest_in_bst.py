
def main():
	node_data = [10,7,6,15,5,11]
	bst = BinarySearchTree()
	bst.build_from_list(node_data)
	print str(bst)
	print bst.print_level_order()
	k = 7
	print 'Kth smallest for k = %d' % k
	print str(bst.kth_smallest(k))

class Node:
	def __init__(self,key=None,left=None,right=None):
		self.key = key
		self.left = left
		self.right = right
		self._data = {'left_child_count':0}
	
	def inc_left_child_count(self):
		self._data['left_child_count']+= 1
	
	def get_left_child_count(self):
		return self._data['left_child_count']
	
	def __str__(self):
		return 'Node: %s, data = %s' % (str(self.key),str(self._data))
	
class BinarySearchTree:
	def __init__(self,root=None):
		self.root = root
	
	def build_from_list(self,node_list):
		for n in node_list:
			self.insert(n)
	
	def kth_smallest(self,k):
		if self.is_empty():
			return self.root
		return self._kth_smallest(self.root,k)
	
	def is_empty(self):
		return (self.root == None)
		
	def insert(self,key):
		if self.is_empty():
			self.root = Node(key)
		else:
			# Track size of left subtree
			update_left_child_count = True
			# Search for node by key
			node = self.find(key,update_left_child_count)
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
				
	def find(self,key,update_left_child_count=False):
		if self.is_empty():
			return self.root
			
		return self._find(self.root,key,update_left_child_count)
	
	def _find(self,node,key,update_left_child_count=False):
		# Go left
		if key <= node.key:
			if update_left_child_count:
				node.inc_left_child_count()
			if node.left:
				return self._find(node.left,key,update_left_child_count)
			else: 
				return node
		# Go right
		elif key > node.key:
			if node.right:
				return self._find(node.right,key,update_left_child_count)
			else: 
				return node
				
	def _kth_smallest(self,node,k):
		node_k = node.get_left_child_count() + 1
		# Found kth
		if k == node_k:
			return node
			
		# kth smallest is in left subtree
		elif k < node_k:
			if node.left:
				return self._kth_smallest(node.left,k)
			else:
				return node
		# kth smallest is in right subtree
		else:
			if node.right:
				return self._kth_smallest(node.right,k)
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
				
		return '\n'.join(output)
	
	def _inorder(self,node,output):
		if not node:
			return
		self._inorder(node.left,output)
		output.append(str(node))
		self._inorder(node.right,output)
			
if __name__ == '__main__':
	main()