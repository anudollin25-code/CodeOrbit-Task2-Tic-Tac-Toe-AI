# game.py
# Tic-Tac-Toe with Minimax AI
# Player = X
# Computer = O

PLAYER = "X"
AI = "O"


def check_winner(board):
    """
    Check whether there is a winner.
    Returns X, O, or None.
    """

    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:

        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]

    return None


def is_board_full(board):
    """Check whether the board is full."""

    return all(cell != "" for cell in board)


def minimax(board, depth, is_maximizing):
    """
    Minimax algorithm helps the computer choose
    the best possible move.
    """

    winner = check_winner(board)

    # AI wins
    if winner == AI:
        return 10 - depth

    # Player wins
    if winner == PLAYER:
        return depth - 10

    # Draw
    if is_board_full(board):
        return 0

    # AI tries to maximize the score
    if is_maximizing:

        best_score = -float("inf")

        for i in range(9):

            if board[i] == "":

                board[i] = AI

                score = minimax(board, depth + 1, False)

                board[i] = ""

                best_score = max(best_score, score)

        return best_score

    # Player tries to minimize the score
    else:

        best_score = float("inf")

        for i in range(9):

            if board[i] == "":

                board[i] = PLAYER

                score = minimax(board, depth + 1, True)

                board[i] = ""

                best_score = min(best_score, score)

        return best_score


def get_best_move(board):
    """
    Find the best move for the computer using Minimax.
    """

    best_score = -float("inf")
    best_move = None

    for i in range(9):

        if board[i] == "":

            board[i] = AI

            score = minimax(board, 0, False)

            board[i] = ""

            if score > best_score:
                best_score = score
                best_move = i

    return best_move