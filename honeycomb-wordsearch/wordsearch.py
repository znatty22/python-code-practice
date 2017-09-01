import sys,os, argparse
from graph_builder import HexagonGraphBuilder
from pprint import pprint

def main():
	# Read in command line args
	parser = argparse.ArgumentParser()
	parser.add_argument('words_file',help='The puzzle file that will be searched for words')
	parser.add_argument('dictionary_file',help='The file with the list of words to search for in the word search puzzle')
	args = parser.parse_args()
	
	# Do files exist?
	_file_exists(args.words_file)	
	_file_exists(args.dictionary_file)
	
	# Find which dictionary words exist in  words file	
	result = solve(args.words_file,args.dictionary_file)

	# Sort the output
	for word in sorted(result):
		print word
	
def solve(words_file,dictionary_file):
	'''
	Find all the words in dictionary_file that exist in
	words_file.

	** Note **
	This solution works for datasets that can sufficiently 
	be stored in main memory with the appropriate additional 
	space left for processing the data and running the program. 
	
	For datasets that may violate the above constraint, a
	new approach is needed. That approach may involve
	reading the honeycomb file in chunks and storing the
	graph in some sort of distributed data store. 

	Similarly, if the dictionary_file is also very large,
	then it would need to be read in chunks or parallel 
	processed. 

	The search algorithm would also need to be
	capable of running on the distributed data store where
	the graph representing the honeycomb is stored.
	'''

	# Store the words from the dictionary file
	dictionary_words = _build_dict(dictionary_file)
	
	# Build the graph from the word search file
	graph = HexagonGraphBuilder().build(words_file)
	
	# Find all words from the dictionary that exist
	# in the graph
	result = []
	for word in dictionary_words:
		if graph.find_word(word):
			result.append(word)
			
	return result
	
def _build_dict(dictionary_file):
	'''
	Store the words from the dictionary_file in a data structure.

	** Note **:
	Could make use of a trie here to store the dictionary words in
	order to speed up search and processing. Did not have time to
	implement, but please see additional notes in graph.py
	'''
	# Assume case-insensitive
	with open(dictionary_file,'r') as words_file:
		return [word.strip() for word in words_file.read().splitlines()]
	
def _file_exists(fpath):
	'''
	Check if file exists. If not, exit program.
	'''
	if not os.path.isfile(fpath):
		print 'File %s does not exist, exiting program!' % fpath
		sys.exit(1)
	
if __name__ == '__main__':
	main()