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

  def rand_init(self, n):
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
        if j == self.N - 1:
          row_value += 0 if n < 2 else fac(n) / int(2 * (fac((n - 2))))
    return int(row_value)

  def count_diagonals(self):
    queens = 0 #número de rainhas atacantes nas diagonais da esquerda para a direita
    for diag in range(self._N):
      q = 0
      q += np.count_nonzero(self._board.diagonal(diag) == QUEEN)
      if diag != 0:
        q = 0
        q += np.count_nonzero(self._board.diagonal(-diag) == QUEEN)
      if q > 1: queens = attacks_number(q)
    return queens
  #contando o número de rainhas atacantes da diagonal principal
  def count_main_diagonal(self):
    queens = 0
    q = 0
    for diag in range(self._N):
      q += np.count_nonzero(self._board.diagonal(diag) == QUEEN)
      if q > 1: queens = attacks_number(q)
    return queens
  #contado o número de rainhas atacantes nas diagonais da esquerda para direita
  def count_main_inferior_diagonals(self):
    queens = 0
    q = 0
    diag = self._N - 2
    j = 0
    while(diag > 0):
      for n in range(diag):
        i = n + 1
        q += np.count_nonzero(self._board[i,j] == QUEEN)
        j += 1
    if q > 1: queens = attacks_number(q)
    return queens
  def count_main_superior_diagonals(self):
    queens = 0
    q = 0
    diag = self._N - 2
    i = 0
    while(diag > 0):
      for n in range(diag):
        j = n + 1
        q += np.count_nonzero(self._board[i,j] == QUEEN)
        i += 1
    if q > 1: queens = attacks_number(q)
    return queens
  def count_secondary_diagonal(self):
    q = 0
    length = 8
    queens = 0
    for j in range(length):
      i = length - j
      q += np.count_nonzero(self._board[i, j] == QUEEN)
    if q > 1: queens = attacks_number(q)
    return queens
  #def count_secondary_superior_diagonals(self):
  #def count_secondary_inferior_diagonals(self):
  def attacks_number(q):
    return int(fac(q)/(2*(fac(q - 2))))
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
    A(nxn) -> n = i + j, para somente todo elemento da diagonal secundária
    '''
   

  def printBoard(self):
    print(self._board)