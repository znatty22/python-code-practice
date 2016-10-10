
def main():
	q = Queue()
	q.enqueue(1)
	q.enqueue(2)
	print 'Queue %s' % str(q)
	print 'Dequeue %s' % q.dequeue()
	q.enqueue(3)
	q.enqueue(4)
	print 'Queue %s' % str(q)
	print 'Dequeue %s' % q.dequeue()
	print 'Queue %s' % str(q)

class StackQueue:
	
	# Efficient queue using 2 stacks

	def __init__(self):
		self.instack = []
		self.outstack = []

	def is_empty(self):
		return (len(self.instack) == 0)

	def enqueue(self,item):
		self.instack.append(item)

	def dequeue(self):
		if self.outstack:
			return self.outstack.pop()
		else:
			while (self.instack):
				self.outstack.append(self.instack.pop())

			if self.outstack:		
				return self.outstack.pop()
			else:
				return None
	
	def peek(self):
		if self.outstack:
			return self.outstack[-1]
		else:
			while (self.instack):
				self.outstack.append(self.instack[-1])

			if self.outstack:		
				return self.outstack[-1]
			else:
				return None

	def __str__(self):
		if self.is_empty():
			return ''
		else:
			output = []

			i = len(self.outstack) - 1
			while (i >= 0):
				output.append(self.outstack[i])
				i-=1

			outstack = []	
			j = len(self.instack) - 1
			while (j >= 0):
				outstack.append(self.instack[j])
				j-=1

			while outstack:
				output.append(outstack.pop())

			return str(output)

class Queue:

	def __init__(self):
		self.list = []

	def enqueue(self,item):
		self.list.insert(0,item)

	def dequeue(self):
		if self.is_empty():
			return None
		else:
			return self.list.pop()
	
	def peek(self):
		if self.is_empty():
			return None
		else:
			return self.list[-1]

	def is_empty(self):
		return (len(self.list) == 0)

	def __len__(self):
		return len(self.list)

	def __str__(self):
		if self.is_empty():
			return ''
		else:
			q = []
			i = len(self.list) - 1
			while (i  >= 0):
				q.append(self.list[i])
				i-=1
			return str(q)

if __name__ == '__main__':
	main()

