import numpy as np
from random import randint as rand
from math import factorial as fac

QUEEN = 1

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
    return int(row_value)

  def count_main_diagonal(self):
    length = 8
    queens = 0
    for diag in range(length):
      q = 0
      q += np.count_nonzero(self._board.diagonal(diag) == QUEEN)
      queens += 0 if q < 2 else int(fac(q) / (2 * (fac((q - 2)))))
      if diag != 0:
        q = 0
        q += np.count_nonzero(self._board.diagonal(-diag) == QUEEN)
        queens += 0 if q < 2 else int(fac(q) / (2 * (fac((q - 2)))))
    return queens

  def count_secondary_diagonal(self):
    '''
    00 01 02 03 04
    10 11 12 13 14
    20 21 22 23 24
    30 31 32 33 34
    40 41 42 43 44

    00
    10 01           i = i - 1; j = j + 1
    20 11 02        i = i - 1; j = j + 1
    30 21 12 03     i = i - 1; j = j + 1
    40 31 22 13 04  i = i - 1; j = j + 1
    '''
    length = 8
    queens = 0
    for k in range(length):
      i = k
      j = 0
      aux = 0
      while i >= 0:
        if i != 0:
          aux += self._board[i, j]
        else:
          aux += self._board[i, j]
          queens += 0 if aux < 2 else int(fac(aux) / (2 * (fac((aux - 2)))))
          aux = 0
        i -= 1
        j += 1

    for k in range(1, length):
      i = length - 1
      j = k
      aux = 0
      while j <= length - 1:
        if j != 7:
          aux += self._board[i, j]
        else:
          aux += self._board[i, j]
          queens += 0 if aux < 2 else int(fac(aux) / (2 * (fac((aux - 2)))))
          aux = 0
        i -= 1
        j += 1
    return queens

  def printBoard(self):
    print(self._board)