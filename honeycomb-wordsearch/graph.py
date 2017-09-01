from pprint import pprint

def main():
	pass
		
class WordSearchGraph():
	'''
	A graph containing a dict that maps unique letters
	to the nodes whose data is equal to the same letter.
	For example:
	{
		'a': (0,0,'a'), (0,1,'a')
	}
	For the letter 'a', there are two nodes which contain 
	'a'. One is at row = 0, col = 0 and the other is
	at row = 0, col = 1.

	The graph also contains an adjacency list that maps 
	each unique node in the graph to all of its neighbors.
	'''
			
	def __init__(self):
		self.letter_to_nodes = {}
		self.graph = {}

	def add_nodes(self,nodes):
		'''
		Add list of nodes to graph
		'''
		for node in nodes:
			self.add_node(node)
	
	def add_node(self,node):
		'''
		Add a node to the graph's adjacency list
		and to the graph's letter to node map.
		'''
		# Add to adj list
		if node not in self.graph:
			self.graph[node] = set()

		# Add to letter-node map
		letter = node[-1]
		if letter not in self.letter_to_nodes:
			self.letter_to_nodes[letter] = set()
		self.letter_to_nodes[letter].add(node)
					

	def create_neighbors(self,nodes):
		'''
		Build neighbor relationships among all nodes in list.
		Neighbor relationship is a bidirectional link. 
		Update graph adjacency list with neighbors
		'''
		# Add first node to end of list to create loop
		nodes.append(nodes[0])
		
		# Clockwise
		for i,node in enumerate(nodes):
			if i < len(nodes) - 1:
				self.graph[node].add(nodes[i+1]) 	
				
		# Counterclockwise
		nodes.reverse()  
		for i,node in enumerate(nodes):
			if i < len(nodes) - 1:
				self.graph[node].add(nodes[i+1])	

	def find_word(self,word,dict_words=None):
		'''
		Find word in word search graph. 
		dict_words is an optional parameter containing
		a trie. Dfs can be sped up with the use of a trie to
		store the dictionary words.
		'''
		if word[0] in self.letter_to_nodes:
			start_nodes = self.letter_to_nodes[word[0]]
			for start in start_nodes:
				if self.dfs(start,word,dict_words):
					return True
			
		return False

	def dfs(self,start,word,dict_words):
		'''
		Depth first search for a particular path (word).

		** Note **
		May be possible to implement more efficiently 
		with a trie or prefix tree. If implemented with 
		a trie, then keep track of current path in dfs. 
		Always check if path exists as a prefix in the 
		trie. If it does not exist in trie, then exit 
		current iteration and move on.
		'''
		visited = set()
		letter_index = 0
		stack = [(start,letter_index)]
		
		while len(stack) > 0:
			current,letter_index = stack.pop()
			if current not in visited:
				letter = current[2]
				if word[letter_index] == letter:
					if (letter_index+1) > (len(word) - 1):
						return True

					visited.add(current)
					letter_index += 1
					stack.extend([(neighbor,letter_index) for neighbor in self.graph[current]])

		return False
	
	def print_letter_node_map(self):
		'''
		Print graph's letter to node map.
		'''
		for k,node_list in self.letter_to_nodes.iteritems():
			graph_entry = []
			for n in node_list:
				graph_entry.append(str(n))
			print k + ': ' + ','.join(graph_entry)

	def print_graph(self):
		pprint(self.graph)
			
if __name__ == '__main__':
	main()
	
