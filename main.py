#! /bin/env python3
# Noughts and Crosses
# Emily Probin and Rob Probin
#  _  _               _   _                     _                            "
# | \| |___ _  _ __ _| |_| |_ ___  __ _ _ _  __| |  __ _ _ ___ ______ ___ ___
# | .` / _ \ || / _` | ' \  _(_-< / _` | ' \/ _` | / _| '_/ _ (_-<_-</ -_|_-<
# |_|\_\___/\_,_\__, |_||_\__/__/ \__,_|_||_\__,_| \__|_| \___/__/__/\___/__/
#               \___/
# https://peps.python.org/pep-0008/

from ansi import CLS
import unittest


class NoughtsAndCrosses:

  def __init__(self, number_of_players):
    self._players = number_of_players
    self._finished = False
    self.player1_character = "X"
    self.player2_character = "O"
    self.board_state = [[" "] * 3 for i in range(3)]
    self._plays = 0
    self.winner = None

  def load_board(self, str):
    # [X][Y]
    self.board_state[0][0] = str[0]
    self.board_state[1][0] = str[1]
    self.board_state[2][0] = str[2]
    self.board_state[0][1] = str[3]
    self.board_state[1][1] = str[4]
    self.board_state[2][1] = str[5]
    self.board_state[0][2] = str[6]
    self.board_state[1][2] = str[7]
    self.board_state[2][2] = str[8]

  def save_board(self):
    output = ""
    for Y in range(len(self.board_state)):
      output += self.board_state[0][Y]
      output += self.board_state[1][Y]
      output += self.board_state[2][Y]

    return output

  def board_to_text(self):
    output = ""
    for counter in range(len(self.board_state)):
      line_to_draw = str(" " + self.board_state[0][counter] + " | ")
      line_to_draw += str(self.board_state[1][counter] + " | ")
      line_to_draw += str(self.board_state[2][counter])
      output += line_to_draw + "\n"

      if counter < 2:
        output += "---+---+--\n"

    return output

  def draw_board(self):
    CLS()
    print(self.board_to_text(), end='')

  def _write(self, X, Y, player):
    if player == 1:
      character = self.player1_character
    else:
      character = self.player2_character

    self.board_state[X][Y] = character
    self._plays += 1
    print(self._plays)
    if self._plays >= 9:
      self._finished = True

  def player_move(self, player):

    print("=================================")
    print("Player", player)
    while True:
      move = 0
      while move < 1 or move > 9:
        try:
          move = int(input("Enter position 1-9: "))
        except ValueError:
          move = 0

      move -= 1
      X = move % 3
      Y = move // 3
      #print(X, Y)
      if self.board_state[X][Y] != " ":
        print("This position is already taken")
      else:
        break
    self._write(X, Y, player)

  def computer_move(self, player):
    pass

  def check_winner(self):
    winner_char = ""
    #check for 3 in a row horizontally
    for x in range(3):
      if self.board_state[x][0] == self.board_state[x][1] and self.board_state[
          x][0] == self.board_state[x][2]:
        if self.board_state[x][0] != ' ':
          winner_char = self.board_state[x][0]

      #check for 3 in a row vertically
    for y in range(3):
      if self.board_state[0][y] == self.board_state[1][y] and self.board_state[
          0][y] == self.board_state[2][y]:
        if self.board_state[0][y] != ' ':
          winner_char = self.board_state[0][y]

      #check for 3 in a row diagonally
      if self.board_state[0][0] == self.board_state[1][1] and self.board_state[
          1][1] == self.board_state[2][2]:
        if self.board_state[1][1] != ' ':
          winner_char = self.board_state[1][1]
      if self.board_state[2][0] == self.board_state[1][1] and self.board_state[
          1][1] == self.board_state[0][2]:
        if self.board_state[1][1] != ' ':
          winner_char = self.board_state[1][1]

    if winner_char == self.player1_character and winner_char != "":
      self.winner = "Player 1"
      self._finished = True
    elif winner_char == self.player2_character and winner_char != "":
      self.winner = "Player 2"
      self._finished = True

  def who_is_winner(self):
    return self.winner

  def finished(self):
    self.check_winner()
    return self._finished


def main():
  while True:
    while True:
      try:
        players = int(input("Number of players: "))
      except ValueError:
        print("Please enter a whole number")
        continue

      if players > 2:
        print("Can only play with up to 2 players")
      elif players < 0:
        print("Can't have a negative number of players")
      elif players == 0 or players == 1:
        print("No AI coded yet")
      else:
        break

    this_game = NoughtsAndCrosses(players)
    while not this_game.finished():
      this_game.draw_board()
      this_game.player_move(1)

      if this_game.finished():
        break
      this_game.draw_board()
      #this_game.computer_move(2)
      this_game.player_move(2)

    this_game.draw_board()
    if this_game.who_is_winner() is None:
      print("Game is a draw")
    else:
      print("Winner is", this_game.who_is_winner())
    again = ""
    while again != "Y" and again != "YES" and again != "N" and again != "NO":
      again = input("Do you want to play again? Y/N ").upper().strip()

    if again == "N" or again == "NO":
      break


class NoughtsAndCrossesTests(unittest.TestCase):
  # Returns True or False.
  def test(self):
    # tests on a blank board
    game = NoughtsAndCrosses(2)
    self.assertEqual(game.save_board(), " " * 9)
    self.assertEqual(
      game.board_to_text(),
      "   |   |  \n---+---+--\n   |   |  \n---+---+--\n   |   |  \n")
    self.assertFalse(game.finished())

    # tests on a specific condition
    Xwinner = "XXX O  OO"
    game.load_board(Xwinner)
    self.assertEqual(game.save_board(), Xwinner)
    self.assertEqual(
      game.board_to_text(),
      " X | X | X\n---+---+--\n   | O |  \n---+---+--\n   | O | O\n")
    self.assertTrue(game.finished())
    self.assertEqual(game.who_is_winner(), "Player 1")

    various_tests = [
      ("X X O  OO", False, None),
      ("X X O OOO", True, "Player 2"),
      ("XOX O O O", False, None),
      ("XOX O OOO", True, "Player 2"),
      ("O  O  O  ", True, "Player 2"),  # column 1 win
      (" O  O  O ", True, "Player 2"),  # column 2 win
      ("  O  O  O", True, "Player 2"),  # column 3 win
      ("OOO      ", True, "Player 2"),  # row 1 win
      ("   OOO   ", True, "Player 2"),  # row 2 win
      ("      OOO", True, "Player 2"),  # row 3 win
      ("O   O   O", True, "Player 2"),  # diagonal 1 win
      ("  O O O  ", True, "Player 2"),  # diagonal 2 win
      ("X  X  X  ", True, "Player 1"),  # column 1 win
      (" X  X  X ", True, "Player 1"),  # column 2 win
      ("  X  X  X", True, "Player 1"),  # column 3 win
      ("XXX      ", True, "Player 1"),  # row 1 win
      ("   XXX   ", True, "Player 1"),  # row 2 win
      ("      XXX", True, "Player 1"),  # row 3 win
      ("X   X   X", True, "Player 1"),  # diagonal 1 win
      ("  X X X  ", True, "Player 1"),  # diagonal 2 win
      ("  X X X  ", True, "Player 1"),  # diagonal 2 win
      ("XOXXOXOXO", False, None),  # draw
    ]
    for i, test in enumerate(various_tests):
      board, finished, winner = test
      game = NoughtsAndCrosses(2)
      game.load_board(board)
      self.assertEqual(game.finished(), finished,
                       str(i) + " Finished " + repr(board))
      self.assertEqual(game.who_is_winner(), winner,
                       str(i) + " Winner " + repr(board))

    # how about tests for player moves - legal and illegal?


if __name__ == '__main__':
  NoughtsAndCrossesTests().test()
  main()

  # https://www.tutorialspoint.com/name-a-special-variable-in-python
  # https://www.freecodecamp.org/news/whats-in-a-python-s-name-506262fe61e8/
