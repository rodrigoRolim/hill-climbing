import numpy as np
from random import randint as rand
from math import factorial as fac

QUEEN = 1

class Board:
  ''' class Board '''
  def __init__(self, n):
    ''' init with 0s '''
    self._N = n
    self._board = np.zeros((n,n), dtype=int)
    self._last_i = -1
    self._last_j = -1
    self._last_value = 0

  def rand_init(self):
    self._board = np.zeros((self._N,self._N), dtype=int)
    for j in range(self._N):
      i = rand(0, self._N - 1)
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
    for i in range(self._N):
      n = 0
      for j in range(self._N):
        n += self._board[i, j]
        if j == self._N - 1:
          row_value += 0 if n < 2 else fac(n) / int(2 * (fac((n - 2))))
    return int(row_value)

  def count_main_diagonal(self):
    n = self._N
    i = 0
    j = 0
    column = 0
    last_column = n - 1
    last_row = n
    diag_sum = 0
    diag_slice = 0
    # andar principal e triângulo superior
    while column <= last_column:
      while i < last_row:
        if j == last_column:
          #print(self._board[i][j])
          diag_slice += self._board[i][j]
          diag_sum += 0 if diag_slice < 2 else fac(diag_slice) / int(2 * (fac((diag_slice - 2))))
          diag_slice = 0
        else:
          #print(self._board[i][j], end=' ')
          diag_slice += self._board[i, j]
        i += 1
        j += 1
      column += 1
      last_row -= 1
      i = 0
      j = column

    i = 1
    j = 0
    row = 1
    last_row = n - 1
    # andar somente triângulo inferior
    while row <= last_row:
      while i <= last_row:
        if i == last_row:
          #print(self._board[i][j])
          diag_slice += self._board[i, j]
          diag_sum += 0 if diag_slice < 2 else fac(diag_slice) / int(2 * (fac((diag_slice - 2))))
          diag_slice = 0
        else:
          #print(self._board[i][j], end=' ')
          diag_slice += self._board[i, j]
        i += 1
        j += 1
      row += 1
      i = row
      j = 0
    return int(diag_sum)

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
    n = self._N
    row = 0
    end_row = n
    diag_sum = 0
    # andar triângulo superior e secundária
    while row < end_row:
      i = row
      j = 0
      diag_slice = 0
      while i >= 0:
        if i != 0:
          #print(self._board[i, j], end=' ')
          diag_slice += self._board[i, j]
        else:
          #print(self._board[i, j])
          diag_slice += self._board[i, j]
          diag_sum += 0 if diag_slice < 2 else fac(diag_slice) / int(2 * (fac((diag_slice - 2))))
          diag_slice = 0
        i -= 1
        j += 1
      row += 1

    # andar sumente triângulo inferior
    row = 1
    diag_slice = 0
    while row < end_row:
      i = end_row - 1
      j = row
      while j < end_row:
        if j != end_row - 1:
          #print(self._board[i, j], end=' ')
          diag_slice += self._board[i, j]
        else:
          #print(self._board[i, j])
          diag_slice += self._board[i, j]
          diag_sum += 0 if diag_slice < 2 else fac(diag_slice) / int(2 * (fac((diag_slice - 2))))
          diag_slice = 0
        i -= 1
        j += 1
      row += 1
    return int(diag_sum)

  def print(self):
    print(self._board)