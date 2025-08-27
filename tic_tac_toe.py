import random

# Board Functions
# ____________________________________________

def create_board():
   """Create a new Tic Tac Toe board (1-9)"""
   return ['1','2','3','4','5','6','7','8','9']


"""Show Board"""
def show_board(board):
   for row in board:
      for col in row:
         print(col, end="\t")
      print("\t")



# Player Functions
# ___________________________________________

"""Set Players Function"""
def set_players():
   
   player1 = random.choice(["X","O"])
   player2 = "O" if player1 == "X" else "X"
   return player1, player2


"""## Take Input"""

def take_input(board, player):
   """Take input from player and update board"""
   while True:
         choice = input(f"{player}, choose a position (1-9): ")
         if choice.isdigit() and int(choice) in range(1,10):
            pos = int(choice) - 1
            if board[pos] not in ["X","O"]:
               board[pos] = player
               break
            else:
               print("Position already taken.")
         else:
            print("Invalid input. Enter 1-9.")



# Game Logic Functions
# __________________________

"""## Check Win"""

def check_win(board):
   """Check if a player has won"""
   combos = [
      [0,1,2],[3,4,5],[6,7,8],
      [0,3,6],[1,4,7],[2,5,8],
      [0,4,8],[2,4,6]]

   for c in combos:
      if board[c[0]] == board[c[1]] == board[c[2]]:
         return True
   return False


"""## Check Full Board"""

def check_full_board(board):
   return all(pos in ["X","O"] for pos in board)



# Main Game Loop
# ___________________________-

def play():
   """Play one round of Tic Tac Toe"""
   player1, player2 = set_players()
   board = create_board()
   player1, player2 = set_players()
   print(f"Player 1: {player1}  |  Player 2: {player2}")
   show_board(board)

   while True:
      for player in [player1, player2]:
         take_input(board, player)
         show_board(board)
         if check_win(board):
            print(f"Player {player} wins!")
            return
         if check_draw(board):
            print("It's a draw!")
            return


# Entry Point
# ____________________
def main():
   """Run the game, allow multiple rounds"""
   while True:
      play_game()
      again = input("Play again? (y/n): ").lower()
      if again != "y":
         print("Thanks for playing!")
         break

if __name__ == "__main__":
   main()