# Windows: exec(open("c:/Users/lenovo/Desktop/Code/TicTacToe.py").read())
import os

columns = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]

#z kółka i krzyżyk
winningCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

PLAYER_1 = "1"
PLAYER_1_SIGN = "O"
PLAYER_2 = "2"
PLAYER_2_SIGN = "X"

def printBoard():
    print(f"     1   2   3   4   5   6   7")
    print(f"    ---------------------------")
    print(f"   | {columns[0][0]} | {columns[1][0]} | {columns[2][0]} | {columns[3][0]} | {columns[4][0]} | {columns[5][0]} | {columns[6][0]} |")
    print(f"    ---------------------------")
    print(f"   | {columns[0][1]} | {columns[1][1]} | {columns[2][1]} | {columns[3][1]} | {columns[4][1]} | {columns[5][1]} | {columns[6][1]} |")
    print(f"    ---------------------------")
    print(f"   | {columns[0][2]} | {columns[1][2]} | {columns[2][2]} | {columns[3][2]} | {columns[4][2]} | {columns[5][2]} | {columns[6][2]} |")
    print(f"    ---------------------------")
    print(f"   | {columns[0][3]} | {columns[1][3]} | {columns[2][3]} | {columns[3][3]} | {columns[4][3]} | {columns[5][3]} | {columns[6][3]} |")
    print(f"    ---------------------------")
    print(f"   | {columns[0][4]} | {columns[1][4]} | {columns[2][4]} | {columns[3][4]} | {columns[4][4]} | {columns[5][4]} | {columns[6][4]} |")
    print(f"    ---------------------------")
    print(f"   | {columns[0][5]} | {columns[1][5]} | {columns[2][5]} | {columns[3][5]} | {columns[4][5]} | {columns[5][5]} | {columns[6][5]} |")
    print(f"    ---------------------------")


def winCondition(x):
    column_number = 0
    column = columns[column_number]
    n=0 #square position in a column
    while column_number <= 6:
        while n <= 2:
            if column[n] == x and column[n+1] == x and column[n+2] == x:
                win = True
                return win
            n+=1
        column_number+=1

    column_number = 0
    n=0 #square position in a column
    while column_number <= 3:
        while n <= 5:
            if columns[column_number][n] == x and columns[column_number+1][n] == x and columns[column_number+2][n] == x:
                win = True
                return win
            n+=1
        column_number+=1
    win = False
    return win


def emptySquare(column_number, square_number):
    column = columns[column_number-1]
    print(column)
    if column[square_number] == ' ':
        empty = True
    else:
        empty = False
    return empty

def main():
    os.system('cls')
    print("You're about to play Four in the row. Enjoy.")
    printBoard()
    turn = 1
    while turn <= 42:
        if turn%2 == 0:
            player = PLAYER_2
        else:
            player = PLAYER_1
        
        column_number = int(input("Pick a column: "))
        column = columns[column_number-1]

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
        if winCondition(content) == True:
            os.system('cls')
            printBoard()
            print("You win!")
            break
        turn+=1
        os.system('cls')
        printBoard()
    print("Game over.")
    


if __name__ == "__main__":
    main()