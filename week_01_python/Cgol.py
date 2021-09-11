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

def setCell(board, r, c, val):
    board[r][c] = val

def printBoard(board):
    for rows in board:
        print(rows)


#MAIN PROGRAM

#Create a new two-dimensional array called board
board = [[]]

#Call createNewBoard function with given parameters
board = createNewBoard(25, 25)

# Breathe life into some cells:
setCell(board, 0, 1, 1);
setCell(board, 1, 2, 1);
setCell(board, 2, 0, 1);
setCell(board, 2, 1, 1);
setCell(board, 2, 2, 1);

#Print out the initialized board
#Should be printBoard function
printBoard(board)
#printBoard(board, board[rows], board[cols])
