from game import check_winner, is_board_full, get_best_move


# Test 1: Player wins
board = [
    "X", "X", "X",
    "O", "O", "",
    "", "", ""
]

print("Winner:", check_winner(board))


# Test 2: Draw
board = [
    "X", "O", "X",
    "X", "O", "O",
    "O", "X", "X"
]

print("Winner:", check_winner(board))
print("Board full:", is_board_full(board))


# Test 3: AI finds a winning move
board = [
    "O", "O", "",
    "X", "X", "",
    "", "", ""
]

print("AI best move:", get_best_move(board))