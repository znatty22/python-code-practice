from Queue import Queue

def main():
	heap = MaxHeap([9,10,11])
	print heap
	
class HeapNode:

	def __init__(self,data=None,parent=None,left=None,right=None):
		self.data = data
		self.parent = parent
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.data)
		
class MaxHeap:
	def __init__(self,data_list=None):
		self.root = None
		if data_list:
			self._build(data_list)
	
	def push(self,data):
		if self.root:
			# Find last node
			q = Queue()
			current = self.root
			q.put(current)
			while not q.empty:
				current = q.get()
				if current.left and current.right:
					q.put(current.left)
					q.put(current.right)
				else:
					return current
					
			# Insert new node
			child = HeapNode(data,current,None,None)
			if not current.left:
				current.left = child
			else:
				current.right = child
			
			# Check for rearrange
			while current.parent and child.data > current.data:
				# Swap parent and child
				current.data = child.data
				child = current
				current = current.parent
		else:
			self.root = HeapNode(data)
			
	def pop(self):
		pass
	
	def peek(self):
		return self.root.data
	
	def _build(self,data_list=None):
		for item in data_list:
			self.push(item)
	
	def __str__(self):
		out = []
		q = Queue()
		current = self.root
		q.put(current)
		
		while not q.empty:
			current = q.get()
			out.append(str(current))
			if current.left:
				q.put(current.left)
			if current.right:
				q.put(current.right)
		
		return str(out)
	
if __name__ == "__main__":
	main()