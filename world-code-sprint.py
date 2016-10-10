import sys
import itertools

def main():
	#string_construction()
	print compute_valid_permutations(4,2)

def camel_case():
	s = raw_input().strip()
	count = 0
	for c in s:
		if ord(c) >= 65 and ord(c) <= 90:
			print c
			count+=1

	count +=1

	print 'Word Count ' + str(count)


def string_construction():
	n = int(raw_input().strip())
	costs = []
	for i in xrange(n):
		# For each string input
		s = raw_input().strip()
		costs.append(min_cost(s))

	# Print Costs	
	for c in costs:
		print c    

def min_cost(s):
	cost = 0
	while len(s) > 0:
		s = s.replace(s[0],"")
		cost+=1	

	return cost

def is_palindrome(s):
	i = 0
	j = len(s) - 1

	while i <= j:
		if s[i] != s[j]:
			return False
		i+=1
		j-=1

	return True		

def compute_valid_permutations(m,n):
	# Generate prefix
	prefix = list(xrange(1,n))


if __name__ == '__main__':
	main()