import random

def print_board(board):
    for row in board:
        print("|".join(row))
    print("")

def check_winner(board, player):
    for row in board:   # Check horizontal
        for i in range(4):
            if all(cell == player for cell in row[i:i+4]):
                return True

    for col in range(7):   # Check vertical
        for i in range(3):
            if all(board[i+j][col] == player for j in range(4)):
                return True

    for i in range(3):   # Check diagonals
        for j in range(4):
            if all(board[i+k][j+k] == player for k in range(4)):
                return True
            if all(board[i+k][j+3-k] == player for k in range(4)):
                return True

    return False

def is_valid_move(board, col):
    return 0 <= col < 7 and board[0][col] == " "

def make_move(board, col, player):
    for row in range(5, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player
            break

def get_player_move(board):
    while True:
        try:
            col = int(input("Enter your move (column 0-6): "))
            if is_valid_move(board, col):
                return col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_ai_move(board):
    valid_moves = [col for col in range(7) if is_valid_move(board, col)]

    return random.choice(valid_moves)   # Basic heuristic: choose a random valid move

def main():
    player = "X"
    ai = "O"
    board = [[" " for _ in range(7)] for _ in range(6)]

    while True:
        print_board(board)

        player_col = get_player_move(board)   # Player's turn
        make_move(board, player_col, player)

        if check_winner(board, player):
            print_board(board)
            print("Congratulations! You win!")
            break

        ai_col = get_ai_move(board)   # AI's turn
        make_move(board, ai_col, ai)

        if check_winner(board, ai):
            print_board(board)
            print("Sorry, you lose. Try again!")
            break

if __name__ == "__main__":
    main()