from Queue import Queue

def main():
	data = [5,9,11,14,18,19,21,33,17,27]
	heap = MinHeap(data)
	print 'Initial heap %s' % str(heap)
	heap.push(7)
	print ' heap %s' % str(heap)
	print 'Sorted %s' % str(heap.k_smallest(len(data)))
		
class MinHeap:
	def __init__(self,data_list=None):
		self.heap = []
		if data_list:
			self._build(data_list)
	
	def k_smallest(self,k):
		output = []
		for i in range(k):
			output.append(self.pop())
		return output

	def push(self,data):
		# Add to end of heap
		self.heap.append(data)
		self._percolate_up(self._last())
			
	def pop(self):
		output = self.heap[0]
		self.heap[0] = self.heap[self._last()]
		self.heap.pop()
		self._percolate_down(0)
		return output
	
	def peek(self):
		return self.heap[0]

	def _percolate_down(self,i):
		while((2*i + 2) <= self._last()):
			i_min_child = self._min_child(i)
			# Min Child < Parent, Swap Them
			if self.heap[i_min_child] < self.heap[i]:
				self._swap(i,i_min_child)
			
			i = i_min_child

	def _percolate_up(self,i):
		# Move child up while it's < parent
		n = self._last()
		while((i-1)//2 >= 0):
			i_parent = (i - 1)// 2
			
			# Child < Parent, Swap Them
			if self.heap[n] < self.heap[i_parent]:
				self._swap(n,i_parent)

			i = i_parent

	def _min_child(self,ip):
		il = 2 * ip + 1
		ir = 2 * ip + 2

		min_i = il
		
		if self.heap[ir] <  self.heap[il]:
			min_i = ir

		return min_i

	def _build(self,data_list=None):
		for item in data_list:
			self.push(item)
	
	def _swap(self,i,j):
		tmp = self.heap[i]
		self.heap[i] = self.heap[j]
		self.heap[j] = tmp		

	def _last(self):
		return len(self.heap)-1		

	def __str__(self):
		return str(self.heap)
	
if __name__ == "__main__":
	main()