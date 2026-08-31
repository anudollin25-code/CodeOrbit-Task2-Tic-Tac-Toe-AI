# 🎮 Tic-Tac-Toe with Minimax AI

An interactive **Tic-Tac-Toe game with an AI opponent** developed as part of my **CodeOrbit AI Internship**.

The project uses the **Minimax algorithm** to enable the computer to make intelligent decisions while playing against the user.

The game is implemented as a web application using **Python, Flask, HTML, CSS, and JavaScript**.

---

## 📌 Project Overview

This project demonstrates how a simple game-playing AI can make decisions using the **Minimax algorithm**.

The user plays as **X**, while the computer plays as **O**.

After every user move, the computer analyzes the available moves and selects the move with the best possible outcome.

---

## ✨ Features

* 🎮 Interactive Tic-Tac-Toe game
* 👤 Human vs AI gameplay
* 🤖 AI opponent powered by Minimax
* ❌ Player uses X
* ⭕ Computer uses O
* 🏆 Win detection
* 🤖 AI win detection
* 🤝 Draw detection
* 🔄 Restart game button
* 🌐 Web-based interface
* 📱 Responsive design
* 🧪 Separate game-logic testing

---

## 🧠 Minimax Algorithm

The AI uses the **Minimax algorithm**, a decision-making algorithm commonly used in game-playing AI.

The algorithm evaluates possible future moves and assigns scores to different outcomes.

```text
AI wins       → Positive score
Player wins   → Negative score
Draw          → 0
```

The AI chooses the move that provides the best possible outcome.

### Basic Process

```text
Current Board
      ↓
Find Available Moves
      ↓
Simulate Possible Moves
      ↓
Evaluate Future Outcomes
      ↓
Calculate Minimax Score
      ↓
Choose Best Move
      ↓
AI Plays
```

---

## 🏗️ Project Architecture

```text
User
  │
  ▼
Web Interface
  │
  ▼
JavaScript
  │
  ▼
Flask Backend
  │
  ▼
Minimax Algorithm
  │
  ▼
AI Best Move
  │
  ▼
Updated Game Board
```

---

## 📂 Project Structure

```text
CodeOrbit-Task2-Tic-Tac-Toe-AI
│
├── app.py
├── game.py
├── test_game.py
├── requirements.txt
├── README.md
│
├── templates
│   └── index.html
│
└── static
    ├── style.css
    └── script.js
```

---

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **HTML5**
* **CSS3**
* **JavaScript**
* **Minimax Algorithm**

---

## ⚙️ How It Works

### 1. Player Move

The user selects an empty cell.

The selected cell is marked with:

```text
X
```

### 2. Game State Check

The program checks whether:

* The player has won
* The board is full
* The game should continue

### 3. AI Decision

If the game continues, the board is sent to the Flask backend.

The Minimax algorithm evaluates possible moves.

### 4. AI Move

The computer selects the best available move and places:

```text
O
```

### 5. Result

The game checks whether the AI has won or whether the game has ended in a draw.

---

## 🧪 Testing

A separate `test_game.py` file was used to verify the game logic.

Example test results:

```text
Winner: X
Winner: None
Board full: True
AI best move: 2
```

These tests verify:

* Player win detection
* Draw detection
* AI move selection

---

## 🚀 How to Run the Project

### Step 1 — Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2 — Open the project

```bash
cd CodeOrbit-Task2-Tic-Tac-Toe-AI
```

### Step 3 — Install Flask

```bash
pip install -r requirements.txt
```

### Step 4 — Run the application

```bash
python app.py
```

### Step 5 — Open the website

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

---

## 🎯 CodeOrbit Internship Task

**Internship:** CodeOrbit AI Internship

**Task:** Tic-Tac-Toe with Simple AI

### Requirements Completed

| Requirement             | Status |
| ----------------------- | ------ |
| User vs Computer        | ✅      |
| AI opponent             | ✅      |
| Minimax algorithm       | ✅      |
| Board displayed clearly | ✅      |
| Win detection           | ✅      |
| Loss detection          | ✅      |
| Draw detection          | ✅      |
| Restart functionality   | ✅      |
| Web interface           | ✅      |

---

## 📚 Learning Outcomes

Through this project, I learned:

* Fundamentals of game-playing AI
* Minimax algorithm
* Recursive problem solving
* Game-state evaluation
* Python backend development
* Flask routing
* Frontend-backend communication
* JavaScript event handling
* Testing game logic

---

## 👩‍💻 Author

**Anuradha Dollin**

ECE Student | AI/ML Enthusiast

---

⭐ Developed as part of the **CodeOrbit AI Internship**.
