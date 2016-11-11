from pprint import pprint
'''
Given a value V, if we want to make change for V cents,
and we have infinite supply of each of 
C = { C1, C2, .. , Cm} valued tokens, what is the minimum 
number of tokens to make the change?

Examples:
Input: tokens[] = {25, 10, 5}, V = 30
Output: Minimum 2 tokens required
We can use one token of 25 cents and one of 5 cents 

Input: tokens[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 tokens required
We can use one token of 6 cents and 1 token of 5 cents
'''

'''
Dynamic programming solution
'''

def _min_tokens(change,token_list,computed_mins):
	min_tokens = None
	if change in token_list:
		computed_mins[change] = 1
		return 1
		
	# Compute min # of tokens needed for change
	for c in token_list:
		diff = change - c
		if (diff) >= 0:
			result = 1 + computed_mins[diff]
			if (not min_tokens) or (result < min_tokens):
				min_tokens = result
			
	computed_mins[change] = min_tokens
	
def min_tokens(change, token_list):
	computed_mins = {0:0}
	for i in xrange(1,change+1):
		_min_tokens(i,token_list,computed_mins)
	
	return computed_mins[change]

change = 11
token_list = [1, 5, 10, 25]
print 'Find min # of tokens for %d, given token list %s: %d' % (change,str(token_list),min_tokens(change,token_list))
	