import numpy as np
from numpy.random import randint as rand

QUEEN = 1

class HillClimbing:
  
  def __init__(self,board):
    self._board = board
  
  def execute(self):
    print(self._board)
    prev_h = self._heuristic()
    prev_i, prev_j = self._board.find_queen(rand(8))
    loop = 0

    while True:
      if loop > 30:
        self._board.rand_init()
        prev_h = self._heuristic()
        print(prev_h)
        prev_i, prev_j = self._board.find_queen(rand(8))
        loop = 0

      j = rand(8)
      for i in range(8):
        h = self._heuristic()
         
        if prev_h == 0:
          self._board.move_queen(prev_i, prev_j)
          return self._board

        if prev_h > h:
          prev_h = h
          prev_i = i
          prev_j = j

      self._board.move_queen(prev_i, prev_j)
      loop += 1

  def _heuristic(self):
    rv = dv = 0
    rv = self._board.count_atack_row()
    dv = self._board.count_main_diagonal()
    dv += self._board.count_secondary_diagonal()
    return int(rv + dv)