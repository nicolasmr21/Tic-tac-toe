import re
import random

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self):
    game = [self.board[0:3] ,self.board[3:6]  , self.board[6:9] ]
    if game[0][0] == game[2][2] == game[1][1] != None or game[0][2] == game[1][1] == game[2][0] != None: #Diag
      self.winner = 'X' if game[1][1] is 'x' else 'O'
      return True
    for x in range(0, 3):
      if game[x][0] == game[x][1] == game[x][2] != None: #Columns
        self.winner = 'X' if game[x][0] is 'x' else 'O'
        return True
      elif game[0][x] == game[1][x] == game[2][x] != None:#Rows
        self.winner = 'X' if game[0][x] is 'x' else 'O'
        return True
    if self.board.count(None) == 0:
      self.winner = 'D'
      return True
    return False

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER
    self.is_game_over = self.is_over()

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self): # TODO: 
    cell = random.randint(0,8)
    if self.board[cell] is None:
      self.board[cell] = _MACHINE_SYMBOL
      return

    self.machine_turn()

  def format_board(self):
    row0 = "|".join(list(map(lambda c: " " if c is None else c, self.board[0:3])))
    row1 = "|".join(list(map(lambda c: " " if c is None else c, self.board[3:6])))
    row2 = "|".join(list(map(lambda c: " " if c is None else c, self.board[6:9])))

    return "\n".join([row0, row1, row2])

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self): # TODO: Finish this function in order to print the result based on the *winner*
    print("You win" if self.winner is 'X' else ("Machine win" if self.winner is 'O' else "Draw"))
