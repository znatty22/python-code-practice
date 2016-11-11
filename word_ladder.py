from Queue import Queue
import string
from pprint import pprint

def main():
	start = 'hit'
	goal = 'cog'
	dictionary = ['hot','dot','dog','lot','log']
	wl = WordLadder(start,goal,dictionary)
	print wl.shortest_transforms()
	
class WordLadder:
	
	def __init__(self,start_word,goal_word,word_list):
		# Create a set for dictionary 
		word_list.append(goal_word)
		self.dictionary = set(word_list)
		self.start_word = start_word
		self.goal_word = goal_word

	def shortest_transforms(self):
		return self.bfs(self.start_word,self.goal_word)
		
	def bfs(self,start=None,goal=None):
		all_paths = {}
		if not start:
			start = self.start_word
		if not goal:
			start = self.goal_word
			
		# Graph BFS
		parent_map = {}
		visited = {}
		q = Queue()
		q.put(start)
		
		while(not q.empty()):
			current = q.get()
			if current == goal:
				all_paths.append(self._construct_path(parent_map))
				
			for child in self._get_children(current):
				if child not in visited:
					visited[child] = 1
					parent_map[child] = current
					q.put(child)
		
		return all_paths
	
	def _construct_path(self,parent_map):
		path = []
		current = self.goal_word
		while(current != self.start_word):
			path.append(parent_map[current])
			current = parent_map[current]
		if path:
			path.reverse()
			path.append(self.goal_word)
		
		return path
		
	def _get_children(self,word):
		alphabet = list(string.lowercase)
		#alphabet = ['o']
		chars_in_word = list(word)
		children = []
		# For each character in word
		for i,character in enumerate(chars_in_word):
			prefix = chars_in_word[0:i]
			suffix = chars_in_word[i+1:]
			# Create variation of word for each char in alphabet
			for letter in alphabet:
				new_word = []
				new_word.extend(prefix)
				new_word.append(letter)
				new_word.extend(suffix)
				# Only keep words found in dictionary
				new_word = ''.join(new_word)
				if new_word in self.dictionary:
					children.append(new_word)
	
		return children

if __name__ == '__main__':
	main()
	