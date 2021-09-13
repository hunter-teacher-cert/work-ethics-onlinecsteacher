# createNewBoard initializes a new array of characters with default values for rows and cols
# Use a nested for loop to initialize the empty board
def createNewBoard(rows, cols):
    matrix = []
    for i in range(rows):
      row = []
      for j in range(cols):
        row.append(0) #initialize values to '-'
      matrix.append(row)
    return matrix

#setCell function takes in the board and a row and column coordinate to initialize to 1
def setCell(board, r, c, val):
    board[r][c] = val

#printBoard prints out the board row by row
def printBoard(board):
    for rows in board:
        print(rows)

# return number of living neigbours of board[r][c]
def countNeighbors(board, r, c):
    livingNeighbors = 0 #initialize variable livingNeighbors

    for i in range(r-1,r+2): # from one row before to one after
        if(i >= 0 and i < len(board)): # within row bounds
            for j in range(c-1, c+2): # from one column before to one after
                if(j >= 0 and j < len(board[r])): # within column bounds if(board[i][j] == 'X')
                    if(board[i][j] == 1): #if cell is alive
                        livingNeighbors += 1 # add to livingNeighbors

    if(board[r][c] == 1): # if current cell alive...
        livingNeighbors -= 1; # ...it's not a 'neighbor'

    return livingNeighbors

def getNextGenCell(board, r, c):
    nextGenCell = 0; # default: dead stays dead

    if(board[r][c] == 1): # For a space that is populated:
      # Each cell with one or no neighbors dies, as if by solitude.
      # Each cell with four or more neighbors dies, as if by overpopulation.
      # Each cell with two or three neighbors survives.
      if(countNeighbors(board, r, c) < 2 or countNeighbors(board, r, c) > 3):
          nextGenCell = 0 # alive becomes dead
      else:
          nextGenCell = 1 # alive stays alive

    elif(countNeighbors(board, r, c) == 3): # already know it's not populated
        nextGenCell = 1 # Each cell with three neighbors becomes alive. (dead becomes alive)
    # only other possibility: dead stays dead

    return nextGenCell


def generateNextBoard(board):
    # create new board with same dimensions as board
    newBoard = [[0 for i in range(len(board))] for j in range(len(board[0]))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            newBoard[i][j] = getNextGenCell(board, i, j)

    return newBoard


#MAIN PROGRAM

#Create a new two-dimensional array called board
board = [[]]

#Call createNewBoard function with given parameters
board = createNewBoard(5, 5)

# Breathe life into some cells:
setCell(board, 0, 1, 1);
setCell(board, 1, 2, 1);
setCell(board, 2, 0, 1);
setCell(board, 2, 1, 1);
setCell(board, 2, 2, 1);

#Print out the initialized board
print("Gen X:")
printBoard(board)
print()

# Generate the next board
print("Gen X + 1:")
board = generateNextBoard(board)
printBoard(board)
print()

# Generate the next board
print("Gen X + 2:")
board = generateNextBoard(board)
printBoard(board)

"""
# testing countNeighbors()
print("0,0 living neighbors: " + str(countNeighbors(board,0,0))); # should be 1
print("0,1 living neighbors: " + str(countNeighbors(board,0,1))); # should be 1
print("1,0 living neighbors: " + str(countNeighbors(board,1,0))); # should be 3
print("1,1 living neighbors: " + str(countNeighbors(board,1,1))); # should be 5
print("2,2 living neighbors: " + str(countNeighbors(board,2,2))); # should be 2
print("1,2 living neighbors: " + str(countNeighbors(board,1,2))); # should be 3
print("1,3 living neighbors: " + str(countNeighbors(board,1,3))); # should be 3


# testing getNextGenCell()
myR = 0
myC = 0
# should print 0
print(str(myR) + ", " + str(myC) + " next gen: " + str(getNextGenCell(board,myR,myC)))

myR = 0
myC = 1
# should print 0
print(str(myR) + ", " + str(myC) + " next gen: " + str(getNextGenCell(board,myR,myC)))

myR = 1
myC = 1
# should print 0
print(str(myR) + ", " + str(myC) + " next gen: " + str(getNextGenCell(board,myR,myC)))

myR = 2
myC = 2
# should print 1
print(str(myR) + ", " + str(myC) + " next gen: " + str(getNextGenCell(board,myR,myC)))

myR = 1
myC = 2
# should print 1
print(str(myR) + ", " + str(myC) + " next gen: " + str(getNextGenCell(board,myR,myC)))

myR = 1
myC = 3
# should print 1
print(str(myR) + ", " + str(myC) + " next gen: " + str(getNextGenCell(board,myR,myC)))

"""
