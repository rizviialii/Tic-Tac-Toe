# create a 3x3 board for the game
board = [[1,2,3], [4,5,6], [7,8,9]]
totalMove = 9

# display the board with the position
def displayBoard():
    return
# add pieces at the specific position
def addPiece(position, option):
    return 
# check for the winner
def winner():
    return True

#driver code
def main():
    print("Welcome to the game!")
    displayBoard()
    while((winner==False) and (totalMove > 0)):
        print("Select Position: ")
        addPiece();
        totalMove = totalMove - 1
        winner()
    if((winner==False)and (totalMove > 0)):
        print("It's a tie!")