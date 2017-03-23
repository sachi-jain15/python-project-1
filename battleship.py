'''BATTLESHIP!!!'''
from random import randint # randint will generate matrix of uniformly distributed random integers

board = [] # Empty

for x in range(5): # Loops 5 times
    board.append(["O"] * 5) #For creating a matrix of 5x5 with all elements having value 'O'

# Function to print board is described below:

def print_board(board):
    for row in board:
        print " ".join(row) # to get rid of quote marks and commas while printing the board

print "Let's play Battleship!"
print "  Ocean  :"
print_board(board)

# Function to return a random row from the board matrix is described below:

def random_row(board):
    return randint(0, len(board) - 1)

# Function to return a random column from the board matrix is described below:

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board) #random_row method call
ship_col = random_col(board) #random_col method call

print "You have 4 turns to guess the location of the ship"

for turn in range(4): #To give 4 turns to the user
    print "Turn %d :"%(turn+1)
    guess_row = int(raw_input("Guess Row:"))#To take row input from user
    guess_col = int(raw_input("Guess Col:"))#To take column input from user

    if guess_row == ship_row and guess_col == ship_col: #If condition for the answer is correct
        print "Congratulations! You sunk the battleship!"
        break; # To come out of the loop
    else: #Else condition if the answer is wrongg
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4): # If condition for the index out of range
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"): # Elif condition for the user had already made the guess
            print "You guessed that one already."
        else:
            print "You missed the battleship!"
            board[guess_row][guess_col] = "X" # To print X where the user had made the wrong choice
    print "  Ocean  :"
    print_board(board)
    print "Turn %d over"%(turn+1)
    if (turn==3): # To tell the user that the game is over
        print "Game Over"
print "      ANSWER "
print "Correct ship row: ",ship_row
print "Correct ship column: ",ship_col
