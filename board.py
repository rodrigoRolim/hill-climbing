import numpy as np
from random import randint as rand
from math import factorial as fac

class Board:
  ''' class Board '''
  def __init__(self):
    ''' init with 0s '''
    self._board = np.zeros((8,8), dtype=int)
    self._last_i = -1
    self._last_j = -1
    self._last_value = 0

  def rand_init(self):
    for j in range(8):
      i = rand(0, 7)
      self._board[i][j] = 1

  def __getitem__(self, key):
    return self._board[key]
  
  def __setitem__(self, key, value):
    self._last_value = self._board[key]
    self._last_i = key[0]
    self._last_j = key[1]
    self._board[key] = value
    return self._board

  def find_queen(self, column):
    n = np.where(self._board[:, column] == 1)
    if n[0].size == 0:
      return -1, -1
    else:
      return n[0][0], column
  
  def remove_queen(self, column):
    i, j = self.find_queen(column)
    if i != -1:
      self._last_value = self._board[i, j]
      self._last_i = i
      self._last_j = j
      self._board[i, j] = 0
      return i, j
    else:
      self._last_value = 0
      self._last_i = 0
      self._last_j = column
      return 0, column
  
  def move_queen(self, row, column):
    i, j = self.find_queen(column)
    if i == -1:
      self._last_value = 0
      self._last_i = row
      self._last_j = column
      self._board[row, column] = 1
      return row, column
    else:
      self._last_value = 1
      self._last_i = i
      self._last_j = j
      self._board[row, column] = 1
      return i, j

  def undo_last_move(self):
    self._board[self._last_i, self._last_j] = self._last_value

  def count_atack_row(self):
    row_value = 0
    for i in range(8):
      n = 0
      for j in range(8):
        n += self._board[i, j]
        if j == 7:
          row_value += 0 if n < 2 else fac(n) / int(2 * (fac((n - 2))))
    return row_value

  def print(self):
    print(self._board)