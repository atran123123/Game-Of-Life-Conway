# Conway's Game of Life
# About the game and rules : https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
import random, time, copy
# The Grid will be 40 by 15
WIDTH = 40
HEIGHT = 15

# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # make a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Living Cell
        else:
            column.append(' ') # Dead Cell
    nextCells.append(column) # nextCells is a list of column lists.

while True: # Main program loop.
    print('\n\n\n\n\n') # Separate each iteration with newlines.
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen to make them represent a 40 by 15 grid
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or ' '. Each list in currentCells is a column
        print() # Print a newline at the end of the row.

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # '% WIDTH' makes sure leftCoord is always between 0 and WIDTH - 1 / wraparound
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.

            # Apply Conway's Game of Life rules to next set
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead
                nextCells[x][y] = ' '
    time.sleep(1) # Add a 1-second pause