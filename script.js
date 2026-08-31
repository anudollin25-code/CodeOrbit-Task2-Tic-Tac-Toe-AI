const cells = document.querySelectorAll(".cell");
const statusText = document.getElementById("status");
const restartButton = document.getElementById("restart-button");

let board = ["", "", "", "", "", "", "", "", ""];
let gameOver = false;
let playerTurn = true;


// Player clicks a cell
cells.forEach(cell => {

    cell.addEventListener("click", async function () {

        const index = Number(this.dataset.index);

        // Ignore invalid moves
        if (!playerTurn || gameOver || board[index] !== "") {
            return;
        }

        // Player makes move
        board[index] = "X";

        updateBoard();

        // Check player win
        if (checkWinner(board) === "X") {
            gameOver = true;
            statusText.textContent = "🎉 You won!";
            return;
        }

        // Check draw
        if (isBoardFull()) {
            gameOver = true;
            statusText.textContent = "🤝 It's a draw!";
            return;
        }

        // Give control to AI
        playerTurn = false;

        statusText.textContent = "🤖 AI is thinking...";

        disableEmptyCells();

        await getAIMove();
    });
});


// Send board to Flask
async function getAIMove() {

    try {

        const response = await fetch("/move", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                board: board
            })
        });

        const data = await response.json();

        console.log("AI response:", data);

        if (!response.ok) {

            console.error("Server error:", data.error);

            statusText.textContent =
                "⚠️ Server error. Check the terminal.";

            return;
        }

        // Update board with AI move
        board = data.board;

        updateBoard();

        // Check game result
        if (data.winner === "O") {

            gameOver = true;
            statusText.textContent = "🤖 AI won!";
            return;
        }

        if (data.winner === "draw") {

            gameOver = true;
            statusText.textContent = "🤝 It's a draw!";
            return;
        }

        // Give turn back to player
        playerTurn = true;

        statusText.textContent =
            "Your turn — You are X";

        enableEmptyCells();

    } catch (error) {

        console.error("Connection error:", error);

        statusText.textContent =
            "⚠️ Could not connect to the AI.";

    }
}


// Update board display
function updateBoard() {

    cells.forEach((cell, index) => {

        cell.textContent = board[index];

        if (board[index] === "X") {
            cell.style.color = "#4f46e5";
        }
        else if (board[index] === "O") {
            cell.style.color = "#9333ea";
        }
        else {
            cell.style.color = "";
        }

    });
}


// Check winner
function checkWinner(currentBoard) {

    const combinations = [

        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]

    ];

    for (const combination of combinations) {

        const [a, b, c] = combination;

        if (
            currentBoard[a] !== "" &&
            currentBoard[a] === currentBoard[b] &&
            currentBoard[a] === currentBoard[c]
        ) {
            return currentBoard[a];
        }
    }

    return null;
}


// Check draw
function isBoardFull() {

    return board.every(cell => cell !== "");

}


// Disable empty cells
function disableEmptyCells() {

    cells.forEach((cell, index) => {

        if (board[index] === "") {
            cell.disabled = true;
        }

    });
}


// Enable empty cells
function enableEmptyCells() {

    cells.forEach((cell, index) => {

        cell.disabled = board[index] !== "";

    });
}


// Restart game
restartButton.addEventListener("click", function () {

    board = ["", "", "", "", "", "", "", "", ""];

    gameOver = false;
    playerTurn = true;

    updateBoard();
    enableEmptyCells();

    statusText.textContent =
        "Your turn — You are X";

});