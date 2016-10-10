from stack import Stack
import sys

def main():
	#test_stack()
	
	# Paranthesis Balance Check
	input_string = 'a'
	print 'Balanced? %s' % check_balance(input_string) 

	# String to Integer Conversion
	#_integer = 6
	#print '%d in binary? %s' % (_integer,integer_to_binary(_integer)) 

	# TO DO - infix_to_postfix isn't working yet!!
	#exp = '456*+'
	#e = Expression(exp)
	#print 'Evaluate expression %s = %d' % (exp,int(e.evaluate()))
	#exp = '5 * 6 + 4'
	#print 'Infix %s to postfix %s' % (exp,e.infix_to_postfix(exp))

class Expression:
	operator_precedence = {'*':3, '/':3,'+':2,'-':2,'(':1}

	def __init__(self,expression):
		self.expression = str(expression)

	def evaluate(self):
		# Convert from infix to postfix
		postfix = self.infix_to_postfix(self.expression)
		# Evaluate postfix expression
		return self.eval_postfix(postfix)

	def infix_to_postfix(self,expression):
		operator_stack = Stack()
		postfix = []
		# Remove white spaces
		expression = "".join(expression.split())
		for c in expression:
			if c in Expression.operator_precedence:
				# Look for corresponding opening paranthesis
				if c == ')':
					# Add other operators to postfix
					op = operator_stack.peek()
					while (not operator_stack.is_empty() and op != '('):
							postfix.append(operator_stack.pop())
							op = operator_stack.peek()
				else:
					# Move higher precedence operators to postfix
					c_precedence = Expression.operator_precedence[c]
					prec = Expression.operator_precedence[operator_stack.peek()]
					while (not operator_stack.is_empty() and prec>=c_precedence):
						postfix.append(operator_stack.pop())
						prec = Expression.operator_precedence[operator_stack.peek()]

					operator_stack.push(c)	
			else:
				try:
					# Convert to float
					n = float(c)
					# Push to operand stack
					postfix.append(n)

				except ValueError:
					print 'Invalid character in expression!'

		while(not operator_stack.is_empty()):
			postfix.append(operator_stack.pop())

	def eval_postfix(self,expression):
		result = 0
		operand_stack = Stack()
		
		for c in expression:
			# Character is an operater, do math
			if c in Expression.operator_precedence:
				op1 = operand_stack.pop()
				op2 = operand_stack.pop()
				result = self.operate(c,op1,op2)
				operand_stack.push(result)
				
			# Character is an operand, push to stack
			else:
				try:
					# Convert to float
					n = float(c)

					# Push to operand stack
					operand_stack.push(n)

				except ValueError:
					print 'Invalid character in expression!'
					sys.exit(1)

		return operand_stack.pop()

	def operate(self,op,op1,op2):
		if op == '*':
			return op1 * op2
		elif op == '/':
			return op1/op2
		elif op == '+':
			return op1 + op2
		elif op == '-':
			return op1 - op2
		else:
			print 'Unsupported operand found! % s' % op

	def is_balanced(self):
		symbols = {'(':')','{':'}','[':']'}

		# Expression has only 1 character
		if len(self.expression) == 1:
			return True

		s = Stack()
		for c in self.expression:
			# Character c is an opener, push to stack
			if c in symbols:
				s.push(c)
			# Character c is not an opener
			else:
				if s.is_empty():
					return False
				else:
					# Is character a closer?
					if c in symbols.values():
						opener = s.pop()
						closer = symbols[opener]
						if closer != c:
							return False	

		# Stack still has openers, expression's unbalanced
		if not s.is_empty():
			return False

def integer_to_binary(_integer):
	if _integer == 0:
		return 0
	
	s = Stack()
	while (_integer != 0):
		remainder = _integer % 2
		s.push(remainder)
		_integer = _integer // 2

	binary_string = []	
	while (not s.is_empty()):
		binary_string.append(str(s.pop()))

	return ''.join(binary_string)

	
	return True 


if __name__ == '__main__':
	main()