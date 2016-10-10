import sys

'''
This problem could be solved in a more generic way such that a lot more arithmetic operations
can be supported and any grouping operator can be supported. I looked into using
3rd party python libraries like asteval, sympy, etc but decided to go with my own
approach since the assignment asked for my own implementation instead of existing ones.

Alternate Solutions:
http://stackoverflow.com/questions/34106484/evaluating-a-mathematical-expression-function-for-a-large-number-of-input-valu
'''

def main():
	expression = raw_input('Enter a mathematical expression\n')
	print (Expression(expression).evaluate())	

	#print Expression('(8/3*5)+10-6').evaluate()

class Expression:
	'''
	This class defines provides an API to evaluate a mathematical expression expression string.
	Currently supports elementary arithmetic expressions (+, -, *, /) and parenthesis grouping operators. 
	'''

	operator_precedence = {'*':3, '/':3,'+':2,'-':2,'(':1,')':None}
	symbols = {'(':')','{':'}','[':']'}	

	def __init__(self,expression):
		# Remove whitespaces
		self.expression = "".join(expression.split())

	def evaluate(self):
		''' 
		Evaluates a mathematical expression by converting from infix to postfix notation. 
		'''

		# Check if expression is just a single number
		try:
			return float(self.expression)
		except: 
			pass

		# Check if balanced
		if self.is_balanced():
			# Convert from infix to postfix
			postfix = self.infix_to_postfix(self.expression)
			
			# Evaluate postfix expression
			try:
			 	return float(self.eval_postfix(postfix))
			except TypeError, e:
				sys.exit(1)
		else:
			print 'Expression %s is unbalanced!' % self.expression
			sys.exit(1)

	def infix_to_postfix(self,expression):
		''' Converts an infix formatted expression to postfix format'''

		# Remove white spaces
		expression = "".join(expression.split())

		operator_stack = Stack()
		postfix = []
		for c in expression:

			# c is an operator
			if c in Expression.operator_precedence:

				# c is an openers
				if c == '(':
					operator_stack.push(c)

				# c is a closer
				elif c == ')':
					# Add other operators to postfix until we've found opener
					if not operator_stack.is_empty():
						op = operator_stack.pop()
					
					while (op != '('):
						postfix.append(op)
						op = operator_stack.pop()
						
				# c is an arithmetic operator
				else:
					
					c_precedence = Expression.operator_precedence[c]
					while (not operator_stack.is_empty()) and (Expression.operator_precedence[operator_stack.peek()] >= c_precedence):
						# Move higher precedence operators to postfix
						postfix.append(operator_stack.pop())

					operator_stack.push(c)
					
			# c is an operand (number)
			else:
				try:
					# Is this a valid operand? 
					n = float(c)
					# Push to operand stack
					postfix.append(n)

				except ValueError:
					print 'Invalid character %s in expression!' % c

		while(not operator_stack.is_empty()):
			postfix.append(operator_stack.pop())

		return postfix

	def eval_postfix(self,expression):
		''' Mathematically evaluates a postfix formatted expression'''

		result = 0
		operand_stack = Stack()
		for c in expression:
			# c is an operater, do math
			if c in Expression.operator_precedence:
				op1 = operand_stack.pop()
				op2 = operand_stack.pop()
				result = self.operate(c,op1,op2)
				operand_stack.push(result)
				
			# c is an operand, push to stack
			else:
				try:
					# Convert to float
					n = float(c)

					# Push to operand stack
					operand_stack.push(n)

				except ValueError:
					print 'Invalid character %s in expression!' % c
					sys.exit(1)

		return operand_stack.pop()

	def operate(self,op,op1,op2):
		'''	
		Performs a mathematical operation between two operands and outputs result. 
		Currently supports elementary arithmetic only: addition, subtraction, multiplication, and division. 
		'''

		try:
			if op == '*':
				return op1 * op2
			elif op == '/':
				return op1/op2
			elif op == '+':
				return op1 + op2
			elif op == '-':
				return op1 - op2
			else:
				print 'Unsupported operation found % s' % op
		
		except TypeError, e:
			print 'Invalid expression! %s ' % self.expression
			sys.exit(1)

	def is_balanced(self):
		''' Checks if the expression string is balanced - For every opening operator there exists a closing operator'''

		# 1 character is balanced
		if len(self.expression) == 1:
			return True

		s = Stack()
		for c in self.expression:

			# Character c is an opener, push to stack
			if c in Expression.symbols:
				s.push(c)
			# Character c is not an opener
			else:
				# Is character a closer?
				if c in Expression.symbols.values():
					if s.is_empty():
						return False
					
					opener = s.pop()
					closer = Expression.symbols[opener]
					if closer != c:
						return False	

		# Stack still has openers, expression's unbalanced
		if not s.is_empty():
			return False
	
		return True


class Stack:
	'''
	This class uses a python list to represent a Stack - last-in, first-out behavior. 
	'''

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