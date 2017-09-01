from graph import WordSearchGraph

def main():
	gb = HexagonGraphBuilder()
	graph = gb.build('honeycomb.txt')
	print '\nGraph'
	graph.print_graph()

class HexagonGraphBuilder():
	'''
	Utility class that builds a graph representing 
	a symmetrical honeycomb structure.
	'''
	
	def __init__(self):
		self.honeycomb_rows = None
		self.triangles = 6
	
	def build(self,inputfile):
		'''
		Read an input file containing a honeycomb structure.
		Each line is a layer in the honeycomb structure.
		Read honeycomb structure into a 2D grid
		Build the word search graph from the honeycomb_grid.
		'''
		g = WordSearchGraph()
		with open(inputfile, 'r') as puzzle_file:
			# Read in data			
			honeycomb_grid = [list(line.strip()) for line in puzzle_file.read().splitlines()[1:]]
			self.honeycomb_rows = len(honeycomb_grid)
			
			# Preprocess honeycomb_grid
			self._preprocess(honeycomb_grid)

			# Build honeycomb_graph
			self._build_graph(g,honeycomb_grid)
				
		return g


	def _build_graph(self,graph,honeycomb_grid):
		'''
		Traverse 2d grid representing a hexagon and build a 
		WordSearchGraph: 

		Split the hexagon up into 6 triangles
		Example: 
			Triangle 0 has the following vertices:
				(0,0,A), (4,0,L), (4,4,G)
			Triangle 1 has the following vertices:
				(0,0,A), (4,4,G), (4,8,X)
			Etc...
		Loop through the nodes in each row (layer) in each
		triangle. Add each node to graph and create neighbor
		relationships among all nodes within a triangle.
		'''
		
		# For each triangle in honeycomb hexagon
		for triangle_index in range(self.triangles):
		
			# For each row in honeycomb grid
			for row in range(self.honeycomb_rows):
			
				# Compute col indices for this row
				start_col = row*triangle_index
				end_col = start_col + row 

				#self._debug(honeycomb_grid,row,start_col,end_col)

				# For each node in honeycomb row in current triangle
				for col in range(start_col,end_col+1):
					# Insert node and its neighbors into graph
					self._add_node_and_neighbors(graph,honeycomb_grid,row,col,triangle_index)

	def _add_node_and_neighbors(self,graph,honeycomb_grid,row,col,triangle_index):
		'''
		Create a node for current row,col
		Create the 2 neighbor nodes - top and top right w.r.t to current
		Insert all 3 nodes into graph
		Create neighbor relationship for all 3 nodes in the graph
		'''

		# Skip last row of triangle, since no rows exist after it
		if row == self.honeycomb_rows - 1:
			return

		# Create current node and neighbor nodes
		current_node = (row,col,honeycomb_grid[row][col])
		# Top
		neighbor_row = row + 1
		neighbor_col = col+triangle_index
		top_node = (neighbor_row,neighbor_col,honeycomb_grid[neighbor_row][neighbor_col])
		# Top Right
		neighbor_row = row + 1
		neighbor_col = col+triangle_index+1
		top_right_node = (neighbor_row,neighbor_col,honeycomb_grid[neighbor_row][neighbor_col])

		# If last triangle, remap copied edge nodes to original nodes in honeycomb_grid
		if triangle_index == 5:
			new_nodes = self._remap_nodes([current_node,top_node,top_right_node],honeycomb_grid)
		else:
			new_nodes = [current_node,top_node,top_right_node]

		# Add nodes to graph
		graph.add_nodes(new_nodes)
		
		# Create neighbors
		graph.create_neighbors(new_nodes)

	def _remap_nodes(self,nodes,honeycomb_grid):
		'''
		If any node has a column index >= total columns 
		in the original honeycomb grid, then it must be
		one of the column 0 nodes which have been copied
		to end of a honeycomb row to form a loop. Need to 
		make sure those nodes are mapped back to node from
		original honeycomb_grid.
		'''
		new_nodes = []
		for node in nodes:
			row = node[0]
			col = node[1]
			org_cols = len(honeycomb_grid[row]) - 1
			if col >= org_cols:
				new_nodes.append((row,0,honeycomb_grid[row][0]))
			else:
				new_nodes.append(node)
		
		return new_nodes

	def _preprocess(self,honeycomb_grid):
		'''
		Need to append first node in each layer to end of row
		in honeycomb_grid in order for them to be included
		in the last triangle.
		'''
		for row in range(self.honeycomb_rows):
			honeycomb_grid[row].append(honeycomb_grid[row][0])

if __name__ == '__main__':
	main()