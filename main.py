

board = [" " for _ in range(9)]

def print_board(board):
    print("   1   2   3")
    for i, row in enumerate([board[i*3:(i+1)*3] for i in range(3)]):
        print(" +---+---+---+")
        print(f"{i+1}| " + " | ".join(row) + " |")
    print(" +---+---+---+")

def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), # columns
                      (0, 4, 8), (2, 4, 6)]           # diagonals
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    return " " not in board

def get_move(board):
    while True:
        try:
            move = int(input("Enter a position (1-9): ")) - 1
            if board[move] == " ":
                return move
            else:
                print("This position is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")


def tic_tac_toe():
    board = [" " for _ in range(9)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        move = get_move(board)
        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()