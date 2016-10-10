from graph import Graph2dNode
from graph import WordSearchGraph

def main():
	gb = Graph2dBuilder()
	gb.build('words.txt')

class Graph2dBuilder():
	
	def __init__(self):
		self.rows = None
		self.cols = None
	
	def build(self,inputfile):
		'''
		Reads an input file containing lines of equal length strings
		and builds a word search graph.
		'''
		g = WordSearchGraph()
		with open(inputfile, 'r') as puzzle_file:
			# Read in data
			grid = [list(line.replace(' ','').strip()) for line in puzzle_file.readlines()[1:]]
			
			# Read in size of wordsearch
			self.rows = len(grid)
			self.cols = len(grid[0])

			# Build graph
			for row in xrange(self.rows):
				for col in xrange(self.cols):
					n = (row,col,grid[row][col])
					# Add to graph
					g.add_node(n)
					# Create neighbor nodes
					self._create_neighbors(n,grid,g)
				
		return g

	def _create_neighbors(self,node,grid,graph):
		'''
		Determines valid neighboring cells of node in grid
		and adds the valid neighbors to node's neighbors
		'''

		nr = node[0]
		nc = node[1]
		# Directions
		#		   T 	TR	R 	BR 	 B 	  BL  L	 TL
		row_inc = [1,	1,	0,  -1,  -1,  -1, 0,  1]
		col_inc = [0,   1,  1,   1,   0,  -1, -1, -1]

		for i in xrange(len(row_inc)):
			row = nr + row_inc[i]
			col = nc + col_inc[i]
			if self._is_cell_valid(row,col):
				graph.add_edge(node,(row,col,grid[row][col]))

		
	def _is_cell_valid(self,row,col):
		'''
		Determines whether the row,col pair exists within
		bounds of the grid. Row and Col must be positive
		and less than total # of rows/cols in grid.
		'''
		valid_row = (row < self.rows) and (row >= 0)
		valid_col = (col < self.cols) and (col >= 0)
		
		return valid_row and valid_col

if __name__ == '__main__':
	main()