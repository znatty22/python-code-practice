
def main():
	test_stack()

def test_stack():
	s = Stack()
	exp = '([{(())}])'
	symbols = {'(':')','{':'}','[':']'}
	print exp
	for c in exp:
		print 'Char %s' % c
		print 'Stack %s' % s
		if c in symbols:
			s.push(c)
		else:
			s.pop()
	

class Stack:

	def __init__(self):
		self.list = []

	def is_empty(self):
		return (len(self.list) == 0)

	def push(self,item):
		self.list.append(item)

	def pop(self):
		if self.is_empty():
			return None
		else:
			return self.list.pop()

	def peek(self):
		if self.is_empty():
			return None
		else:
			return self.list[-1]

	def __str__(self):
		return str(self.list)


if __name__ == '__main__':
	main()