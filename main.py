from tic_tac_toe import TicTacToeGame

def play():
  game = TicTacToeGame()

  while not game.is_game_over:
    game.play()
    game.print()

  game.print_result()

if __name__ == "__main__":
  play()
