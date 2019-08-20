# Windows: exec(open("c:/Users/lenovo/Desktop/Code/TicTacToe.py").read())
import os


PLAYER_1 = "1"
PLAYER_1_SIGN = "O"
PLAYER_2 = "2"
PLAYER_2_SIGN = "X"
NUMBER_OF_COLUMNS = 7
NUMBER_OF_ROWS = 6
NUMBER_OF_SQUARES = 42
board = [[' ',' ',' ',' ',' ',' '] for column in range(NUMBER_OF_COLUMNS)]

def print_board():
    print(f"  1   2   3   4   5   6   7")
    print(f" ---------------------------")
    for row in range(NUMBER_OF_ROWS):
        for column in range(NUMBER_OF_COLUMNS):
            print(f"| {board[column][row]} ", end = "")
        print(f"|\n ---------------------------")

def winCondition(board):

    for i in range(42):
        column_length = len(board[0])
        col = i // column_length
        row = i % column_length

        signs = ["X", "O"]

        for item in signs:
            try:
                if board[col][row] == item and board[col][row+1] == item and board[col][row+2] == item and board[col][row+3] == item:
                    return True
            except:
                pass
            try:     
                if board[col][row] == item and board[col+1][row] == item and board[col+2][row] == item and board[col+3][row] == item:
                    return True
            except:
                pass
            try:     
                if board[col][row] == item and board[col+1][row+1] == item and board[col+2][row+2] == item and board[col+3][row+3] == item:
                    return True
            except:
                pass
            try:     
                if board[col][row] == item and board[col+1][row-1] == item and board[col+2][row-2] == item and board[col+3][row+-3] == item:
                    return True
            except:
                pass


def emptySquare(column_number, row_number):
    square = board[column_number-1][row_number]
    if square == ' ':
        empty = True
    else:
        empty = False
    return empty

def main():
    os.system('clear')
    print("You're about to play Four in the row. Enjoy.")
    print_board()
    turn = 1
    while turn <= NUMBER_OF_SQUARES:
        if turn%2 == 0:
            player = PLAYER_2
        else:
            player = PLAYER_1
        try:
            column_number = int(input("Pick a column: "))
            column = board[column_number-1]
        except (ValueError, IndexError):
            continue

        if player == PLAYER_1:
            row_number = NUMBER_OF_ROWS-1 #iteration begins from the last row in the column
            while row_number >= 0:
                if emptySquare(column_number, row_number)==True:
                    column[row_number] = PLAYER_1_SIGN
                    content = PLAYER_1_SIGN
                    break
                row_number+=-1
        else:
            row_number = NUMBER_OF_ROWS-1
            while row_number >= 0:
                if emptySquare(column_number, row_number) == True:
                    column[row_number] = PLAYER_2_SIGN
                    content = PLAYER_2_SIGN
                    break
                row_number+=-1
        if winCondition(board):
            os.system('clear')
            print_board()
            print("You win!")
            break
        turn+=1
        os.system('clear')
        print_board()
    print("Game over.")
    


if __name__ == "__main__":
    main()