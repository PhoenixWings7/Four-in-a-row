import os

NUMBER_OF_COLUMNS = 7
NUMBER_OF_ROWS = 6
NUMBER_OF_SQUARES = NUMBER_OF_COLUMNS*NUMBER_OF_ROWS
MAXIMUM_NUMBER_OF_PLAYERS = 5

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
        

def selecting_number_of_players():
    valid_player_number = list(map(str, range(1,MAXIMUM_NUMBER_OF_PLAYERS+1)))
    number_of_players = input(f"Enter number of players (max number of players is {MAXIMUM_NUMBER_OF_PLAYERS}): ")
    while number_of_players not in valid_player_number:
        number_of_players = input(f"Enter number of players (max number of players is {MAXIMUM_NUMBER_OF_PLAYERS}): ")
    number_of_players = int(number_of_players)
    return number_of_players

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

def emptySquare(board, column_number, row_number):
    square = board[column_number-1][row_number]

    return square == ' '

def main():
    board = [[' ']*NUMBER_OF_ROWS for column in range(NUMBER_OF_COLUMNS)]

    os.system('clear')
    print("You're about to play Four in the row_num. Enjoy.")

    number_of_players = selecting_number_of_players()
    player_signs_dict, players_names = selecting_players(number_of_players)
    
    print_board(board)
    turn = 1

    while turn <= NUMBER_OF_SQUARES:        
        player = players_names[turn%number_of_players]

        try:
            column_number = int(input("Pick a column: "))
            column = board[column_number-1]
        except (ValueError, IndexError):
            continue
        

        player_sign = player_signs_dict[player]
        #iteration begins from the last row_num in the column
        row_number = NUMBER_OF_ROWS-1
        
        while row_number >= 0:
            if emptySquare(board, column_number, row_number):
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