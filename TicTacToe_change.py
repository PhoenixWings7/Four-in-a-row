# Windows: exec(open("c:/Users/lenovo/Desktop/Code/TicTacToe.py").read())
import os

# lista pustych stringów, każde miejsce to inne pole
# zamiana na X lub O w zależności od miejsca i gracza

squares = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']
winningCombinations = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7]
]

fillers = [" ", "1", "2", "O", "X"]
PLAYER_1 = "1"
PLAYER_2 = "2"
a1 = squares[0]
a2 = squares[1]
a3 = squares[2]
b1 = squares[3]
b2 = squares[4]
b3 = squares[5]
c1 = squares[6]
c2 = squares[7]
c3 = squares[8]

def printBoard():
    a1 = squares[0]
    a2 = squares[1]
    a3 = squares[2]
    b1 = squares[3]
    b2 = squares[4]
    b3 = squares[5]
    c1 = squares[6]
    c2 = squares[7]
    c3 = squares[8]

    print(f"     1   2   3")
    print(f"    -----------")
    print(f" A | {a1} | {a2} | {a3} |")
    print(f"    -----------")
    print(f" B | {b1} | {b2} | {b3} |")
    print(f"    -----------")
    print(f" C | {c1} | {c2} | {c3} |")
    print(f"    -----------")


# winning = [
#     (0, 1, 2),
#     (3, 4, 5), 
#     ...
# ]

def winCondition(x):
    # if board[0] == x and board[1] == x and board[2] == x:
    if a1 == x and a2 == x and a3 == x:
        win = True
    elif b1 == x and b2 == x and b3 == x:
        win = True
    elif c1 == x and c2 == x and c3 == x:
        win = True
    elif a1 == x and b1 == x and c1 == x:
        win = True
    elif a2 == x and b2 == x and c2 == x:
        win = True
    elif a3 == x and b3 == x and c3 == x:
        win = True
    elif a1 == x and b2 == x and c3 == x:
        win = True
    elif a3 == x and b2 == x and c1 == x:
        win = True
    else:
        win = False
    return win

def emptySquare(square_number):
    if squares[square_number] == ' ':
        empty = True
    else:
        empty = False
    return empty

def main():
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3

    print("You're about to play Tic Tac Toe. First player's sign is 'O'.")
    printBoard()
    turn = 1
    while turn <= 9:
        if turn%2 == 0:
            player = PLAYER_2
        else:
            player = PLAYER_1
        square = list(input("Pick a square: "))
        os.system('clear')

        print(square)
        input()

        if square[0] == "a" or square[0] == "A":
            square_number = int(square[1])-1
            if player == PLAYER_1:
                if emptySquare(square_number) == True:
                    squares[square_number] = fillers[3]
                    content = fillers[3]
                else:
                    print("This square is already filled.")
                    input("Press enter.")
                    continue
            else:
                if emptySquare(square_number) == True:
                    squares[square_number] = fillers[4]
                    content = fillers[4]
                else:
                    print("This square is already filled.")
                    continue
            if winCondition(content) == True:
                printBoard()
                print("You win!")
                break
        print(squares)
        input()

        turn+=1
        printBoard()


    # b1 = ...
    # squares[3] = ...
    print("Game over.")
    


if __name__ == "__main__":
    main()