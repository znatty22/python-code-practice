## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.

# n^2 spiral:
# Write a function that prints 1 to n^2 in clockwise spiral order along a square
# input: 3
# output:
# 1 2 3
# 8 9 4
# 7 6 5

# input: 4
# 1 2   3  4
# 12 13 14 5
# 11 16 15 6 
# 10 9  8  7

def create_spiral(n):
   
    spiral = []
    for i in range(n):
        new = []
        spiral.append(new)
        for j in range(n):
           new.append(0)
           
    
    total = n*n + 1
    direction = 'right'
    r = 0
    c = 0
    for count in range(1,total):
        spiral[r][c] = count
        
        if direction == 'right':
            c += 1
            if c >= n - 1 or (spiral[r][c + 1] != 0):
                direction = 'down'
                
        elif direction == 'down':
            r+=1
            if r >= n - 1 or (spiral[r+1][c] != 0):
                direction = 'left'
        
        elif direction == 'left':
            c-=1
            if (c <= 0) or (spiral[r][c - 1] != 0):
                direction = 'up'

        elif direction == 'up':
            r-=1
            if r <= 0 or (spiral[r - 1][c] != 0):
                direction = 'right'

    return spiral
    
def print_spiral(n):
    spiral = create_spiral(n)
    
    output = ''
    for row in spiral:
        output += str(row) + '\n'
    
    print output

print_spiral(3)