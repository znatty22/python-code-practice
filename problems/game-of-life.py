
'''
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.
'''

ALIVE = 1
DEAD = 0

def next_state(board):
	rows = len(board)
	cols = len(board[0])
	next_board = board

	for r in range(rows):
		for c in range(cols):
			set_cell_state(board,next_board,r,c,rows,cols);

	return next_board


def set_cell_state(board,next_board,r,c,rows,cols):
	current_state = board[r][c]
	neighbors = get_neighbors(board,r,c,rows,cols)
	alive_count = 0;
	for n in neighbors:
		cell_state = board[n[r]][n[c]]
		if cell_state == ALIVE:
			alive_count+=1

	# Already Alive 
	if current_state == ALIVE:
		if !(alive_count == 2 or alive_count == 3):
			next_board[r][c] = DEAD	
	# Already Dead
	else:
		if (alive_count == 3):
			next_board[r][c] = ALIVE

def get_neighbors(board,r,c,nr,nc):

	neighbors = []

	# Top
	neighbors.append((r+1,c))
	# Bottom 
	neighbors.append(r-1,c)
	# Top Left
	neighbors.append((r+1,c-1))
	# Top Right
	neighbors.append((r+1,c+1))
	# Bottom Left
	neighbors.append((r-1,c-1))
	# Bottom Right
	neighbors.append((r-1,c+1))

	for point in neighbors:
		if valid_cell(board,point[0],point[1],nr,nc) == False:
			neighbors.remove(point)

	return neighbors		

def valid_cell(board,r,c,nr,nc):
	
	valid_row = (r >=0) and (r < nr)
	valid_col = (c >=0) and (c < nc)

	return valid_row & valid_col
