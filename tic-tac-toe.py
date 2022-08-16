import random 

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]


currentPlayer = "X" # starting player in X 
continueGame = True
winner = None


def print_board_numbers():
    number_board = [[str(i+1) for i in range(j*3 , (j+1)*3)] for j in range(3)]
    for row in number_board:
        print('| ' + ' | '.join(row) + ' |')


# print game board 
def print_board(board):
    print()
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")
    print()


# check if the player wins by diagonal 
def check_diagonal():
    global continueGame

    diagonal_left = board[0] == board[4] == board[8] != "-"
    diagonal_right = board[2] == board[4] == board[6] != "-"

    # if either one diagonal is filled with the same pattern, game will stop 
    if diagonal_left or diagonal_right:
        continueGame = False     

    if diagonal_left:
        winner = board[0]
        return winner
    elif diagonal_right:
        winner = board[2]
        return winner
    else:
        return None


# check if the player wins by row
def check_row():
    global continueGame

    rowOne = board[0] == board[1] == board[2] != "-"
    rowTwo  = board[3] == board[4] == board[5] != "-"
    rowThree = board[6] == board[7] == board[8] != "-"
    
    # if either one rows are filled with the same patterns, game will stop
    if rowOne or rowTwo or rowThree:
        continueGame = False
    
    if rowOne:
        winner = board[0]
        return winner
    elif rowTwo:
        winner = board[3]
        return winner
    elif rowThree:
        winner = board[6]
        return winner 
    else:
        return None


# check if the player wins by column
def check_col():
    global continueGame

    columnOne = board[0] == board[3] == board[6] != "-"
    columnTwo  = board[1] == board[4] == board[7] != "-"
    columnThree = board[2] == board[5] == board[8] != "-"

    # if either one column is filled with the same pattern, game will end
    if columnOne or columnTwo or columnThree:
        continueGame = False
    
    if columnOne:
        winner = board[0]
        return winner
    elif columnTwo:
        winner = board[1]
        return winner 
    elif columnThree:
        winner = board[2]
        return winner 
    else:
        return None

    
def switchPlayer():
    global currentPlayer

    # if current player was X, then current player is O
    if currentPlayer == "X":
        currentPlayer = "O"
    else: # else, current player is X
        currentPlayer = "X"


def check_tie():
    global continueGame 

    # if the board does not have "-", tie
    if "-" not in board:
        continueGame = False # end the game if tie
        return True
    else:
        return False


def checkWinner():
    global winner 

    # check if winner is row 
    row_winner = check_row()
    # check if winner is diagonal
    diagonal_winner = check_diagonal()
    # check if winner is column
    column_winner = check_col()

    if row_winner:
        winner = row_winner
    elif diagonal_winner:
        winner = diagonal_winner
    elif column_winner:
        winner = column_winner
    else:
        winner = None


def check_game_over():
    checkWinner()
    check_tie()


def player_input(player):
    print("\nPlayer " + player + "'s turn.")
    player_input = input("\nChoose a number from 1-9: ")

    valid = False
    while not valid:
        while player_input not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            player_input = input("Please choose a number from 1-9: ")

        player_input = int(player_input) - 1

        if board[player_input] == "-":
            valid = True
        else:
            print("That spot has already been taken. Please try again.")
            print_board(board)
            
    board[player_input] = player
    
    print_board(board)

def main():


    print("Welcome to the Tic Tac Toe game!\n")
    print("To play, enter the numbers shown on the board to place your letter.\n")
    print_board_numbers()

    while continueGame :
        player_input(currentPlayer)

        check_game_over()

        switchPlayer()

    if winner == "X" or winner == "O":
        print("\nPlayer " + winner + " won!")
    else:
        winner == None
        print("\nIt's a tie!")


    print("\nThank you for playing Tic Tac Toe.")


main()