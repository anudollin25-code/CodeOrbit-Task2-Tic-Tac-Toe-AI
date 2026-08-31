from flask import Flask, render_template, request, jsonify
from game import check_winner, is_board_full, get_best_move

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/move", methods=["POST"])
def make_move():

    try:
        data = request.get_json()

        print("Received data:", data)

        if not data or "board" not in data:
            return jsonify({
                "error": "Board data was not received."
            }), 400

        board = data["board"]

        print("Received board:", board)
        print("Board length:", len(board))

        # Make sure the board has exactly 9 cells
        if len(board) != 9:
            return jsonify({
                "error": f"Invalid board length: {len(board)}"
            }), 400

        # Check if the player has already won
        winner = check_winner(board)

        if winner:
            return jsonify({
                "board": board,
                "winner": winner
            })

        # Check for draw
        if is_board_full(board):
            return jsonify({
                "board": board,
                "winner": "draw"
            })

        # Find the best move using Minimax
        ai_move = get_best_move(board)

        print("AI selected position:", ai_move)

        if ai_move is not None:
            board[ai_move] = "O"

        # Check whether AI won
        winner = check_winner(board)

        if winner:
            return jsonify({
                "board": board,
                "winner": winner
            })

        # Check draw after AI move
        if is_board_full(board):
            return jsonify({
                "board": board,
                "winner": "draw"
            })

        return jsonify({
            "board": board,
            "winner": None
        })

    except Exception as e:

        print("SERVER ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)