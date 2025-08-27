# ***Tic Tac Toe – Python Project***

Tic Tac Toe is a classic two-player game implemented in Python. Players take turns marking X or O on a 3x3 board. The first player to align three marks horizontally, vertically, or diagonally wins. If all cells are filled without a winner, the game ends in a draw.

_______________________________________________________________

# ***Features***

* Two-player gameplay (Player vs Player).

* Random assignment of X and O to players.

* Input validation: only numbers 1–9 allowed, and cannot select an already taken cell.

* Display the board after each move.

* Detects win or draw and announces the result.

* Option to play multiple rounds.

* Clean and easy-to-read code with functions and comments in English.
* 
_______________________________________________________________

# ***How to Run?***

#Run the game directly

'python tic_tac_toe.py'

 _______________________________________________________________

# ***Code Overview***
**Board Functions**

**create_board()**: Creates a new board numbered 1–9.

**show_board(board)**: Displays the current board state.


***Player Functions***

**set_players()**: Randomly assigns X and O to Player 1 and Player 2.

**take_input(board, player)**: Takes input from a player and updates the board.

***Game Logic Functions***

**check_win(board)**: Checks if any player has won the game.

**check_full_board(board)**: Checks if the board is full (draw).


***Main Game***

**play()**: Handles a single round of Tic Tac Toe.

**main()**: Runs the game loop, allows playing multiple rounds.

_______________________________________________________________
# ***Example Gameplay***
Player 1: X  |  Player 2: O

1 | 2 | 3
4 | 5 | 6
7 | 8 | 9

X, choose a position (1-9): 5

1 | 2 | 3
4 | X | 6
7 | 8 | 9

O, choose a position (1-9): 1

...
Player X wins!
Play again? (y/n): n
Thanks for playing!
