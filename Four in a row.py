import os

NUMBER_OF_COLUMNS = 7
NUMBER_OF_ROWS = 6
NUMBER_OF_SQUARES = NUMBER_OF_COLUMNS*NUMBER_OF_ROWS

def print_board(board):
    print(f"  1   2   3   4   5   6   7")
    print(f" ---------------------------")
    
    for row_num in range(NUMBER_OF_ROWS):
        for column in range(NUMBER_OF_COLUMNS):
            print(f"| {board[column][row_num]} ", end = "")
        print(f"|\n ---------------------------")

def winCondition(board, square_content):

    for square_number in range(NUMBER_OF_SQUARES):
        column_length = len(board[0])
        col_num = square_number // column_length
        row_num = square_number % column_length

        try:
            if board[col_num][row_num] == square_content and board[col_num][row_num+1] == square_content and board[col_num][row_num+2] == square_content and board[col_num][row_num+3] == square_content:
                return True
        except:
            pass
        try:     
            if board[col_num][row_num] == square_content and board[col_num+1][row_num] == square_content and board[col_num+2][row_num] == square_content and board[col_num+3][row_num] == square_content:
                return True
        except:
            pass
        try:     
            if board[col_num][row_num] == square_content and board[col_num+1][row_num+1] == square_content and board[col_num+2][row_num+2] == square_content and board[col_num+3][row_num+3] == square_content:
                return True
        except:
            pass
        try:     
            if board[col_num][row_num] == square_content and board[col_num+1][row_num-1] == square_content and board[col_num+2][row_num-2] == square_content and board[col_num+3][row_num+-3] == square_content:
                return True
        except:
            pass

    return False


def emptySquare(column_number, row_number):
    square = board[column_number-1][row_number]

    return square == ' '

def main():
    board = [[' ',' ',' ',' ',' ',' '] for column in range(NUMBER_OF_COLUMNS)]

    os.system('clear')
    print("You're about to play Four in the row_num. Enjoy.")
    print_board(board)
    turn = 1

    while turn <= NUMBER_OF_SQUARES:
        if turn%2 == 0:
            player = "player_2"
        else:
            player = "player_1"
        
        try:
            column_number = int(input("Pick a column: "))
            column = board[column_number-1]
        except (ValueError, IndexError):
            continue

        player_signs_dict = {"player_1" : "O",
                            "player_2" : "X",}

        player_sign = player_signs_dict[player]
        #iteration begins from the last row_num in the column
        row_number = NUMBER_OF_ROWS-1
        
        while row_number >= 0:
            if emptySquare(column_number, row_number):
                column[row_number] = player_sign
                square_content = player_sign
                break
            row_number+=-1
        
        if winCondition(board, square_content):
            os.system('clear')
            print_board(board)
            print("You win!")
            break
        turn+=1
        os.system('clear')
        print_board(board)
    print("Game over.")
    


if __name__ == "__main__":
    main()