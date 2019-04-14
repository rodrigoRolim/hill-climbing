import numpy as np
from numpy.random import randint as rand

QUEEN = 1
H = 2

class HillClimbing:
  
  def __init__(self,board):
    self._board = board
    self._N = board.getN()
    self._current_node = self._make_node()
  
  def _make_node(self):
    i, j = self._board.find_queen(rand(8))
    return [i, j, self._heuristic()]

  def _find_best_value(self):
    best_value = [self._current_node[0], self._current_node[1], self._current_node[H]]
    for column in range(self._N):
      for row in range(self._N):
        i, j = self._board.move_queen(row, column)
        neighbor = [row, column, self._heuristic()]
        self._board.move_queen(i, j)
        if best_value[H] >= neighbor[H]:
          best_value = neighbor
    return best_value
    
  def execute(self):
    yield self._current_node[H]
    while True:
      h = self._find_best_value()
      if self._current_node[H] >= h[H]:
        self._board.move_queen(h[0], h[1])
        yield h[H]
      if self._current_node[H] == 0:
        self._board.print()

  def _heuristic(self):
    rv = dv = 0
    rv = self._board.count_atack_row()
    dv = self._board.count_main_diagonal()
    dv += self._board.count_secondary_diagonal()
    return int(rv + dv)