# Initialize a new array of characters with default values for rows and cols
def createNewBoard(rows, cols):
    matrix = []
    for i in range(rows):
      row = []
      for j in range(cols):
        row.append(0) #initialize values to 0
      matrix.append(row)
      print(row) #print out blank board

#Call createNewBoard function with given parameters
createNewBoard(25, 25)

# Use a nested for loop to initialize the empty board
