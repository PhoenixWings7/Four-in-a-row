import os

def selecting_players(number_of_players):
    player_signs_dict = {}
    players_names = []
    while number_of_players > 0:
        name = input("Enter the name of a player: ")
        if name in player_signs_dict:
            input("Sorry! This player already exists! Press enter to try again.")
            continue
        
        sign = input(f"Enter {name}'s sign in the game (a single letter or number): ")
        if sign in player_signs_dict.values():
            input("This is another player's sign. Press enter to start from your name.")
            continue
        elif len(list(sign)) != 1:
            input("This is not a valid sign. Press enter to start from your name.")
            continue
        
        player_signs_dict[f"{name}"] = f"{sign}"
        players_names.append(name)
        number_of_players+=-1
    return player_signs_dict, players_names
        
def selecting_number_of_players(MAXIMUM_NUMBER_OF_PLAYERS):
    valid_player_number = list(map(str, range(1,MAXIMUM_NUMBER_OF_PLAYERS+1)))
    number_of_players = input(f"Enter number of players (max number of players is {MAXIMUM_NUMBER_OF_PLAYERS}): ")
    while number_of_players not in valid_player_number:
        number_of_players = input(f"Enter number of players (max number of players is {MAXIMUM_NUMBER_OF_PLAYERS}): ")
    number_of_players = int(number_of_players)
    return number_of_players

def selecting_number_of_columns(MAXIMUM_NUMBER_OF_COLUMNS):
    valid_column_number = list(map(str, range(1,MAXIMUM_NUMBER_OF_COLUMNS+1)))
    number_of_columns = input(f"Enter number of columns (max number of columns is {MAXIMUM_NUMBER_OF_COLUMNS}): ")
    while number_of_columns not in valid_column_number:
        number_of_columns = input(f"Enter number of columns (max number of columns is {MAXIMUM_NUMBER_OF_COLUMNS}): ")
    number_of_columns = int(number_of_columns)
    return number_of_columns

def selecting_number_of_rows(MAXIMUM_NUMBER_OF_ROWS):
    valid_row_number = list(map(str, range(1,MAXIMUM_NUMBER_OF_ROWS+1)))
    number_of_rows = input(f"Enter number of rows (max number of rows is {MAXIMUM_NUMBER_OF_ROWS}): ")
    while number_of_rows not in valid_row_number:
        number_of_rows = input(f"Enter number of rows (max number of rows is {MAXIMUM_NUMBER_OF_ROWS}): ")
    number_of_rows = int(number_of_rows)
    return number_of_rows

def print_board(board, NUMBER_OF_COLUMNS, NUMBER_OF_ROWS):
    NUMBER_OF_LINES_PER_COLUMN = 3
    AMOUNT_OF_SPACES_BEETWEEN_COLUMNS = NUMBER_OF_COLUMNS-1

    column_numbers = [column_number for column_number in range(1, NUMBER_OF_COLUMNS+1)]
    #prints columns numbers and spaces beetween them
    print("  ", end = "")
    for column_number in column_numbers:
        print(f"{column_number}   ", end = "" )
    #prints a dividing line
    print(f"\n " + "-"*NUMBER_OF_COLUMNS*NUMBER_OF_LINES_PER_COLUMN + "-"*AMOUNT_OF_SPACES_BEETWEEN_COLUMNS)
    
    #prints the rest of the board
    for row_num in range(NUMBER_OF_ROWS):
        #prints one row of squares divided by "|"
        for column in range(NUMBER_OF_COLUMNS):
            print(f"| {board[column][row_num]} ", end = "")
        print(f"|\n " + "-"*NUMBER_OF_COLUMNS*NUMBER_OF_LINES_PER_COLUMN + "-"*AMOUNT_OF_SPACES_BEETWEEN_COLUMNS)

def winCondition(board, square_content, NUMBER_OF_SQUARES):

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

def emptySquare(board, column_number, row_number):
    square = board[column_number-1][row_number]
    return square == ' '

def fullColumn(board, column_number):
    square = board[column_number-1][0]
    return (square != ' ')

def main():
    os.system('clear')
    print("You're about to play Four in the row_num. Enjoy.")

    MAXIMUM_NUMBER_OF_PLAYERS = 5
    MAXIMUM_NUMBER_OF_COLUMNS = 9
    MAXIMUM_NUMBER_OF_ROWS = 12
    
    number_of_players = selecting_number_of_players(MAXIMUM_NUMBER_OF_PLAYERS)
    player_signs_dict, players_names = selecting_players(number_of_players)
    NUMBER_OF_COLUMNS = selecting_number_of_columns(MAXIMUM_NUMBER_OF_COLUMNS)
    NUMBER_OF_ROWS = selecting_number_of_rows(MAXIMUM_NUMBER_OF_ROWS)
    NUMBER_OF_SQUARES = NUMBER_OF_COLUMNS*NUMBER_OF_ROWS
    board = [[' ']*NUMBER_OF_ROWS for column in range(NUMBER_OF_COLUMNS)]
    
    os.system('clear')
    print_board(board, NUMBER_OF_COLUMNS, NUMBER_OF_ROWS)
    turn = 1

    while turn <= NUMBER_OF_SQUARES:        
        player = players_names[turn%number_of_players]
        print(f"{player}'s turn.")
        try:
            column_number = int(input("Pick a column: "))
            column = board[column_number-1]
        except (ValueError, IndexError):
            continue
        

        player_sign = player_signs_dict[player]
        #iteration begins from the last row_num in the column
        row_number = NUMBER_OF_ROWS-1
        
        if fullColumn(board, column_number):
            input("This column is full! Press enter to continue.")
            continue
        
        while row_number >= 0:
            if emptySquare(board, column_number, row_number):
                column[row_number] = player_sign
                square_content = player_sign
                break
            row_number+=-1
        
        if winCondition(board, square_content, NUMBER_OF_SQUARES):
            os.system('clear')
            print_board(board, NUMBER_OF_COLUMNS, NUMBER_OF_ROWS)
            print(f"{player} wins!")
            break
        turn+=1
        os.system('clear')
        print_board(board, NUMBER_OF_COLUMNS, NUMBER_OF_ROWS)
    print("Game over.")

if __name__ == "__main__":
    main()