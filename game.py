# 4.7.2.1 PROJECT
#
# Do an interactive Tic Tac Toe using multidimesional lists
#
from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+"+"-------+"*3+"\n|"+"       |"*3)
    print("|  ", board[0][0],"  |  ", board[0][1], "  |  ", board[0][2], "  |")
    print("|"+"       |"*3+"\n+"+"-------+"*3+"\n|"+"       |"*3)
    print("|  ", board[1][0],"  |  ", board[1][1], "  |  ", board[1][2], "  |")
    print("|"+"       |"*3+"\n+"+"-------+"*3+"\n|"+"       |"*3)
    print("|  ", board[2][0],"  |  ", board[2][1], "  |  ", board[2][2], "  |")
    print("|"+"       |"*3+"\n+"+"-------+"*3)
    return

def enter_move(board):
    while True:
        try:
            userInput = int(input("Enter your move: "))-1
            if userInput < 0 or userInput > 8:
                continue
        except:
            print("Only numbers 1 - 9 allowed.")
            continue
        if type(freeFields[userInput]) is tuple:
            x, y = freeFields[userInput]
            board[x][y] = "O"
            freeFields[userInput] = "O"
            if victory_for(board, "O"):
                print('+++++++ Player \'O\' wins! +++++++')
                return True
            return
        else:
            print('Invalid move, choose another.')
    
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    return

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    for x in range(3):
        for y in range(3):
            freeFields.append((x,y))
    freeFields[4] = "X"
    return freeFields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if freeFields[0] == sign and freeFields[1] == sign and freeFields[2] == sign:
        return True
    elif freeFields[3] == sign and freeFields[4] == sign and freeFields[5] == sign:
        return True
    elif freeFields[6] == sign and freeFields[7] == sign and freeFields[8] == sign:
        return True
    elif freeFields[0] == sign and freeFields[3] == sign and freeFields[6] == sign:
        return True
    elif freeFields[1] == sign and freeFields[4] == sign and freeFields[7] == sign:
        return True
    elif freeFields[2] == sign and freeFields[5] == sign and freeFields[8] == sign:
        return True
    elif freeFields[0] == sign and freeFields[4] == sign and freeFields[8] == sign:
        return True
    elif freeFields[2] == sign and freeFields[4] == sign and freeFields[6] == sign:
        return True
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    contale = 0
    while True:
        computerInput = randrange(9)
        #print('.',computerInput+1,'.', end="") #debug
        contale += 1  # give computer 50 times of trying available random number
        if contale > 50:
            print('computer turn took more than 50 randoms')
            break
        if type(freeFields[computerInput]) is tuple:
            print("\nComputer's turn: ")
            print(computerInput+1)
            x, y = freeFields[computerInput]
            board[x][y] = "X"
            freeFields[computerInput] = "X"
            if victory_for(board, "X"):
                print('+++++++ Player \'X\' wins! +++++++')
                return True
            return
    return


############
### MAIN ###
############
#
# Initialization
print("\nWelcome to Tic Tac Toe !\nComputer starts at center with X.\n")

#computer's turn, always starts at center with X
board = [[1,2,3],
         [4,"X",6],
         [7,8,9]]

freeFields = []
freeFields = make_list_of_free_fields(board)
display_board(board)

#gameOver = False
emptySlots = 8
tictactoe = True

while emptySlots:

    # users move:
    if enter_move(board):
        tictactoe = False
        break
    emptySlots -= 1
    display_board(board)


    #computer's move
    if draw_move(board):
        tictactoe = False
        break
    emptySlots -= 1
    display_board(board)
    
if not tictactoe:
    display_board(board)
    print("Game over!")
else:
    print("Game Over, Tic Tac Toe.")

### END
