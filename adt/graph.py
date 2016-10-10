from pprint import pprint
from Queue import Queue

def main():
	grid = [[1,1,0],
			[0,0,1]]
			
	graph = GraphAdjList(grid)
	print graph
	#print 'Count islands %s ' % graph.count_islands()
	
	s = (0,0)	
	g = (1,2)
	print 'Does a path exist from %s to %s: %s' % (str(s),str(g),str(graph.dfs(s,g))) 

	print '\n Path from %s to %s: %s' % (str(s),str(g),str(graph.dfs_path(s,g))) 

	print '\n Shortest Path from %s to %s: %s' % (str(s),str(g),str(graph.bfs(s,g))) 
	
class GraphAdjList:
	
	def __init__(self,grid):
		self.grid = grid
		self.rows = len(grid)
		self.cols = len(grid[0])
		self._build()
	
	
	def bfs(self):
		pass

	def shortest_path(self):
		pass

	def _dfs(self,start,goal,visited):		
		for n in self.graph[start]:
			if not(n in visited):
				if n == goal:
					print 'Found! node %s ' % str(goal)
					return True
				else:
					visited.append(n)
					return self._dfs(n,goal,visited)
		return False
	
	def dfs(self,start,goal):
		if (start in self.graph) and (goal in self.graph):
			visited = []
			visited.append(start)
			return self._dfs(start,goal,visited)
		else:
			print 'Invalid start node %s or goal node %s - one or both not in graph' % (str(start),str(goal))
			return None
	
	def dfs_path(self,start,goal):
		path = []
		if (start in self.graph) and (goal in self.graph):
			# Initialize ds
			visited = []
			to_explore = []
			parent_map = {}

			# Add to stack
			to_explore.append(start)

			# Does a path exist
			found = self._dfs_path(start,goal,visited,to_explore,parent_map)
			if found:
				# Construct the path from backtracking
				path = self._construct_path(start,goal,parent_map)
			else:
				print 'Node not found, no path exists!'
		else:
			print 'Invalid start node %s or goal node %s - one or both not in graph' % (str(start),str(goal))
		
		return path		

	def _dfs_path(self,start,goal,visited,to_explore,parent_map):
		found = False

		# While stack of neighbors is not empty
		while(len(to_explore) > 0):
			# Get curr node on stack
			curr = to_explore.pop()
			# Is it the goal
			if (curr == goal):
				found = True
				break
			
			# Get curr's neighbors
			neighbors = self.graph[curr]
			for n in neighbors:
				if not(n in visited):
					visited.append(n)
					parent_map[n] = curr
					to_explore.append(n)


		return found

	def bfs(self,start,goal):
		path = []
		if (start in self.graph) and (goal in self.graph):
			# Initialize ds
			visited = []
			to_explore = Queue()
			parent_map = {}

			# Add to stack
			to_explore.put(start)

			# Does a path exist
			found = self._bfs(start,goal,visited,to_explore,parent_map)
			if found:
				# Construct the path from backtracking
				path = self._construct_path(start,goal,parent_map)
			else:
				print 'Node not found, no path exists!'
		else:
			print 'Invalid start node %s or goal node %s - one or both not in graph' % (str(start),str(goal))
		
		return path		

	def _bfs(self,start,goal,visited,to_explore,parent_map):
		found = False

		# While stack of neighbors is not empty
		while(not to_explore.empty):
			# Get curr node on stack
			curr = to_explore.get()
			# Is it the goal
			if (curr == goal):
				found = True
				break
			
			# Get curr's neighbors
			neighbors = self.graph[curr]
			for n in neighbors:
				if not(n in visited):
					visited.append(n)
					parent_map[n] = curr
					to_explore.put(n)


		return found

	def _construct_path(self,start,goal, parent_map):
		path = []
		curr = (goal[0],goal[1])
		while(curr != start):
			path.insert(0,curr)
			curr = (parent_map[curr][0],parent_map[curr][1])

		path.insert(0,start)

		return path

	def dfs_visit_all(self,n,visited):
		# Mark node as visited
		visited[n[0]][n[1]] = True
		
		# Get neighbors
		neighbors = self.graph[n]
		for neighbor in neighbors:
			self.dfs_visit_all(neighbor,visited)
	
	def count_islands(self):
		island_count = 0
		
		# Initialize 2d matrix to track visited nodes
		visited = []
		for r in range(self.rows):
			new = []
			for c in range(self.cols):
				new.append(False)
			visited.append(new)
		
		# Loop through each cell in matrix
		for r in range(self.rows):
			for c in range(self.cols):
				if (not visited[r][c]) and ((r,c) in self.graph):
					self.dfs_visit_all((r,c),visited)
					island_count += 1
		
		return island_count
		
	def add_vertex(self,n):
		if not (n in self.graph):
			self.graph[n] = []
	
	def add_edge(self,n1,n2):
		#if not (n1 in self.graph):
		#	self.add_vertex(n1)
		if (n1 in self.graph) and n2:
			self.graph[n1].append(n2)
		
	def _build(self):
		self.graph = {}
		for r in range(self.rows):
			for c in range(self.cols):
				# Add to graph
				if self.grid[r][c]:
					self.add_vertex((r,c))
				# Populate neighbors
				self._create_neighbors((r,c)) 
	
	def _is_valid_cell(self,row,col):
		valid_row = (row < self.rows) and (row >= 0)
		valid_col = (col < self.cols) and (col >= 0)
		return (valid_row) and (valid_col)
		
	def _create_neighbors(self,n):
		r = n[0]
		c = n[1]
		#       Top           Top Right      Top Left        Bottom      Bottom Left     Bottom Right    Left     Right
		cells = [(r + 1, c), (r + 1, c - 1), (r + 1, c + 1), (r - 1, c), (r - 1, c - 1), (r - 1, c + 1), (r,c-1),(r,c+1)]
		for n1 in cells:
			if (self._is_valid_cell(n1[0],n1[1])):
				if self.grid[n1[0]][n1[1]]:
					self.add_edge(n,n1)
			
	def __str__(self):
		output = ''
		for n in self.graph:
			output += str(n) + ': ' + str(self.graph[n]) + '\n'
		return output
		
if __name__ == '__main__':
	main()