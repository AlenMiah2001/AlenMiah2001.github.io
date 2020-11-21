import random 

grid = [" "  for number in range(9)]

def placeMarker(marker, space):
    grid[space-1] = marker

def isSpaceEmpty(space):
    return grid[space-1] == " "

def createGrid(grid):
    for x in [0,3,6]:
        print("   |   |   ")
        print(" " + grid[x] + " | " + grid[x+1] + " | " + grid[x+2] + " ")
        print("   |   |   ")
        if x <= 3:
                print("-----------")


def wins(grid, marker):
    for x in [0,3,6]:
        if(grid[x] == grid[x+1] == grid[x+2] == marker):
            return True
    for x in range(3):
        if(grid[x] == grid[x+3] == grid[x+6] == marker):
            return True
    if(grid[0] == grid[4] == grid[8] == marker or grid[2] == grid[4] == grid[6] == marker):
        return True
    return False

def playersMove():
    space = float(input("Where would you like to place an X? (1-9) "))
    space = int(space)
    while space > 9 or space < 1 or isSpaceEmpty(space) == False:
        if space > 9 or space < 1:   
            print("\nThat space is out of the range (1-9)")
        elif isSpaceEmpty(space) == False:
            print("That space is occupied!")
        space = float(input("Where would you like to place an X? (1-9) "))
        space = int(space)    
    placeMarker("X", space)
        

def computersMove():
    possibleMoves = [x for x, marker in enumerate(grid) if marker == " "]
    space = 10
    
    for marker in ["O", "X"]:
        for move in possibleMoves:
            gridCopy = grid[:]
            gridCopy[move] = marker
            if wins(gridCopy, marker):
                space = move + 1
                return space
            
    openCorners = []
    for move in possibleMoves:
        if move in [0,2,6,8]:
            openCorners.append(move + 1)
    if len(openCorners) >= 1:
        space = random.choice(openCorners)
        return space
    
    if 5 in possibleMoves:
        space = 5
        return space
    
    openEdges = []
    for move in possibleMoves:
        if move in [1,3,5,7]:
            openEdges.append(move + 1)
    if len(openEdges) >= 1:
        space = random.choice(openEdges)
        
    return space

def noMoreEmptySpaces(grid):
    if " " in grid:
        return False
    else:
        return True

def main():
    print("Welcome to Tic Tac Toe!")
    playAgain = "yes"
    while(playAgain.lower() == "yes" or playAgain.lower() == "y"):
        for x in range(9):
            grid[x] = " "
        createGrid(grid)
        while(noMoreEmptySpaces(grid) == False):
            if(wins(grid, 'O')):
                print("\nThe computer won!")
                break
            else:
                playersMove()
                createGrid(grid)
        
            if(wins(grid, 'X')):
                print("\nYou won!")
                break
            elif(noMoreEmptySpaces(grid) == False):    
                space = computersMove()
                placeMarker("O", space)
                print("The computer placed an O in space " + str(space))
                createGrid(grid)
    
        if(noMoreEmptySpaces(grid)):
            print("\nIts a tie!")

        playAgain = input("Would you like to play again? (Yes / No) ")
            
        
main()
        

    