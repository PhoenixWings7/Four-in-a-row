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
    # print(f"     1   2   3   4   5   6   7")
    # print(f"    ---------------------------")
    # print(f"   | {board[0][0]} | {board[1][0]} | {board[2][0]} | {board[3][0]} | {board[4][0]} | {board[5][0]} | {board[6][0]} |")
    # print(f"    ---------------------------")
    # print(f"   | {board[0][1]} | {board[1][1]} | {board[2][1]} | {board[3][1]} | {board[4][1]} | {board[5][1]} | {board[6][1]} |")
    # print(f"    ---------------------------")
    # print(f"   | {board[0][2]} | {board[1][2]} | {board[2][2]} | {board[3][2]} | {board[4][2]} | {board[5][2]} | {board[6][2]} |")
    # print(f"    ---------------------------")
    # print(f"   | {board[0][3]} | {board[1][3]} | {board[2][3]} | {board[3][3]} | {board[4][3]} | {board[5][3]} | {board[6][3]} |")
    # print(f"    ---------------------------")
    # print(f"   | {board[0][4]} | {board[1][4]} | {board[2][4]} | {board[3][4]} | {board[4][4]} | {board[5][4]} | {board[6][4]} |")
    # print(f"    ---------------------------")
    # print(f"   | {board[0][5]} | {board[1][5]} | {board[2][5]} | {board[3][5]} | {board[4][5]} | {board[5][5]} | {board[6][5]} |")
    # print(f"    ---------------------------")

    print(f"  1   2   3   4   5   6   7")
    print(f" ---------------------------")
    for row in range(NUMBER_OF_ROWS):
        for column in range(NUMBER_OF_COLUMNS):
            print(f"| {board[column][row]} ", end = "")
        print(f"|\n ---------------------------")

def winCondition(board):
    for i in range(42):
        col = i // len(board[0])
        row = i % len(board[0])

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


def emptySquare(column_number, square_number):
    column = board[column_number-1]
    print(column)
    if column[square_number] == ' ':
        empty = True
    else:
        empty = False
    return empty

def main():
    os.system('clear')
    print("You're about to play Four in the row. Enjoy.")
    print_board()
    turn = 1
    while turn <= 42:
        if turn%2 == 0:
            player = PLAYER_2
        else:
            player = PLAYER_1
        
        column_number = int(input("Pick a column: "))
        column = board[column_number-1]

        if player == PLAYER_1:
            square_number = 5
            while square_number >= 0:
                if emptySquare(column_number, square_number)==True:
                    column[square_number] = PLAYER_1_SIGN
                    content = PLAYER_1_SIGN
                    break
                square_number+=-1
        else:
            square_number = 5
            while square_number >= 0:
                if emptySquare(column_number, square_number) == True:
                    column[square_number] = PLAYER_2_SIGN
                    content = PLAYER_2_SIGN
                    break
                square_number+=-1
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