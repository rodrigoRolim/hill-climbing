import signal
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from board.board import Board
from hill_climbing import HillClimbing

try:
  n = 8
  board = Board(n)

  i, j = 4, 0
  board[i, j] = 1
  i, j = 5, 1
  board[i, j] = 1
  i, j = 6, 2
  board[i, j] = 1
  i, j = 3, 3
  board[i, j] = 1
  i, j = 4, 4
  board[i, j] = 1
  i, j = 5, 5
  board[i, j] = 1
  i, j = 6, 6
  board[i, j] = 1
  i, j = 5, 7
  board[i, j] = 1
  board.print()

  #board.rand_init()
  hill_climbing = HillClimbing(board)
  line_plot = []
  for h in hill_climbing.execute():
    line_plot.append(h)
except KeyboardInterrupt:
    print("W: interrupt received, stopping…")
    n = len(line_plot)
    x = range(1, n + 1)
    plt.plot(x, line_plot)
    plt.ylabel('heuristic')
    plt.ylabel('state space')
    plt.show()