import random


def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print("\n-------------")


def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def get_computer_move(board):
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if check_win(board, "O"):
                    return i, j
                board[i][j] = " "

    
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if check_win(board, "X"):
                    return i, j
                board[i][j] = " "

    
    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if board[i][j] == " ":
            return i, j


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        if player == "X":
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if board[row][col] != " ":
                print("Invalid move! Try again.")
                continue
        else:
            print("Computer's turn...")
            row, col = get_computer_move(board)

        board[row][col] = player
        print_board(board)

        if check_win(board, player):
            print(f"{player} wins!")
            break

        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"


play_game()
