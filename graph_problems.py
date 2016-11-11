from Queue import Queue
from pprint import pprint

def main():
	grid = [[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0]]
	
	gp = GraphProblems(grid)
	print 'Island count %d' % gp.count_islands()
	
class GraphProblems:
	
	def __init__(self,grid):
		self.grid = grid
		self.rows = len(self.grid)
		self.cols = len(self.grid[0])

	def count_islands(self):
		visited = {}
		count = 0
		for row in range(self.rows):
			for col in range(self.cols):
				if self.grid[row][col] and (row,col) not in visited:
					self._bfs(row,col,visited)
					count+=1
		return count

	def _bfs(self,row,col,visited):
		q = Queue()
		q.put((row,col))
		while(not q.empty()):
			current = q.get()
			for n in self._get_neighbors(current[0],current[1]):
				if n not in visited:
					visited[n] = 1
					q.put(n)
	
	def _get_neighbors(self,row,col):
		# Top, Left, Bottom, Right
		r_inc = [1,0,-1,0]
		c_inc = [0,1,0,-1]
		neighbors = []
		rows = [row+inc for inc in r_inc]
		cols = [col+inc for inc in c_inc]
		for n_r,n_c in zip(rows,cols):
			if self._is_valid_cell(n_r,n_c) and (self.grid[n_r][n_c] == 1):
				neighbors.append((n_r,n_c))
		
		return neighbors
	
	def _is_valid_cell(self,row,col):
		valid_row = (row >= 0) and (row < self.rows)
		valid_col = (col >= 0) and (col < self.cols)
		return valid_row and valid_col

if __name__ == '__main__':
	main()
	