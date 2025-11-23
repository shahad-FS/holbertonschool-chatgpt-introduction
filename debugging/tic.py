#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def is_draw(board):
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Input validation
        try:
            row = int(input(f"Enter row (0-2) for player {player}: "))
            col = int(input(f"Enter column (0-2) for player {player}: "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid position. Must be 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input. Numbers only.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place the move
        board[row][col] = player

        # Check winner AFTER move — winner is current player
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check draw
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


tic_tac_toe()
