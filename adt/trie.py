from queue import Queue
from pprint import pprint
from collections import defaultdict

def main():
	words = ['homes']
	trie = Trie(words)
	print 'Searching for %s, Found: %s ' % (words[0],trie.search(words[0]))
	print 'Searching for %s, Found: %s ' % ('home',trie.search('home'))

class TrieNode:
	def __init__(self,is_word=False):
		self.is_word = is_word
		self.children = defaultdict(TrieNode)

class Trie:
	
	def __init__(self,words=None):
		self.root = TrieNode()
		if words:
			self._build(words)

	def _build(self,words):
		for word in words:
			self.insert(list(word))

	def insert(self,word):
		node = self.root
		for c in word:
			node = node.children[c]
		node.is_word = True

	def search(self,word,full_word=True):
		node = self.root
		for c in word:
			if c not in node.children:
				return False
			node = node.children[c]

		# Searching full word	
		if full_word:
			return node.is_word

		# Searching prefix
		else:
			return True
		

	def starts_with(self,prefix):
		return self.search(prefix,False)


if __name__ == '__main__':
	main()

