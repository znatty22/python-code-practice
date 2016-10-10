import sys,os, argparse
from graph_builder import Graph2dBuilder
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

	print result
	
def solve(words_file,dictionary_file):

	# Store the words in the dictionary file
	dict_words = _build_dict(dictionary_file)
	#dict_words = ['quiz']

	# Build the graph from the word search file
	graph = Graph2dBuilder().build(words_file)
	#graph.print_graph()
	
	# Find all words from the dictionary that exist
	# in the graph
	result = []
	for word in dict_words:
		if graph.find_word(word):
			result.append(word)
			
	return result
	
def _build_dict(dictionary_file):
	# Assume case-insensitive
	with open(dictionary_file,'r') as words_file:
		return [word.lower().strip() for word in words_file.readlines()]
	
def _file_exists(fpath):
	if not os.path.isfile(fpath):
		print 'File %s does not exist, exiting program!' % fpath
		sys.exit(1)
	
if __name__ == '__main__':
	main()