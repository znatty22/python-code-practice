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

	'''
			
	def __init__(self):
		self.letter_to_nodes = {}
		self.graph = {}

	def print_letter_node_map(self):
		for k,node_list in self.letter_to_nodes.iteritems():
			graph_entry = []
			for n in node_list:
				graph_entry.append(str(n))
			print k + ': ' + ', '.join(graph_entry)

	def print_graph(self):
		for k,node_list in self.graph.iteritems():
			graph_entry = []
			for n in node_list:
				graph_entry.append(str(n))
			print str(k) + ': ' + ', '.join(graph_entry)
	
	def find_word(self,word,dict_words=None):
		print 'Find word %s' % word
		if word[0] in self.letter_to_nodes:
			start_nodes = self.letter_to_nodes[word[0]]
			for start in start_nodes:
				if self.dfs(start,word):
					print 'Word found! '
					return True

		print 'Word not found'			
		return False

	def dfs(self,start,word):
		visited = set()
		stack = []

		letter_index = 0
		stack.append(start)
		
		while len(stack) > 0:
			current = stack.pop()
			if current not in visited:
				letter = current[-1]
				if word[letter_index] == letter:
					if letter_index == len(word) - 1:
						return True

					visited.add(current)
					letter_index += 1
					stack.extend(self.graph[current])

		return False
	

	def add_node(self,node):
		# Add to adj list
		if node not in self.graph:
			self.graph[node] = []

		# Add to letter-node map
		letter = node[-1]
		if letter in self.letter_to_nodes:
			self.letter_to_nodes[letter].append(node)
		else:
			self.letter_to_nodes[letter] = [node]					

	def add_edge(self,n1,n2):
		self.graph[n1].append(n2)

if __name__ == '__main__':
	main()
	
