import math 

'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
For example, given binary tree {3,9,20,#,#,15,7},
return its level order traversal as [[15,7], [9,20],[3]]
'''
NULL_DELIMITER = '#'

def main():
	arr = [3,9,20,'#','#',15,7]

	print bottom_up(arr)

def bottom_up(tree_array):
	output = []
	if not tree_array:
		return output

	# Num levels in tree	
	levels = int(math.log(len(tree_array)+1,2)) 
	i = 0
	# For each level in tree
	for l in range(levels):
		nodes_in_level = []
		# Num of nodes in level
		node_count = 2**l
		while node_count > 0:
			# Add to output if not null node
			if tree_array[i] != NULL_DELIMITER:
				nodes_in_level.append(tree_array[i])
			node_count-=1
			i+=1
		output.append(nodes_in_level)

	output.reverse()	
		
	return output

if __name__ == '__main__':
	main()