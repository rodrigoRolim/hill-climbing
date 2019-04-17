import os
import signal
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint as rand
from board.board import Board
from hill_climbing import HillClimbing

def _get_experiment_number():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  path = os.path.join(dir_path, 'experiment_number' + '.' + 'txt')
  experiment = open(path,'r')
  number = experiment.readline()
  number = int(number)
  number += 1
  experiment.close()
  _set_experiment(number)
  return number

def _set_experiment(number):
  dir_path = os.path.dirname(os.path.realpath(__file__))
  path = os.path.join(dir_path, 'experiment_number' + '.' + 'txt')
  experiment = open(path,'w')
  experiment.write(str(number))
  experiment.close()
  return number

def _save_board_setup(path, hill_climbing):
  text_board = open(path,'a+')
  text_board.write('\n\n')
  text_board.write(np.array2string(hill_climbing.get_board(), separator=' '))
  text_board.close()

def _board_setup_5_steps_from_solution(board):
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

def _board_setup_flat(board):
  i, j = 0, 6
  board[i, j] = 1
  i, j = 1, 4
  board[i, j] = 1
  i, j = 2, 1
  board[i, j] = 1
  i, j = 3, 3
  board[i, j] = 1
  i, j = 4, 5
  board[i, j] = 1
  i, j = 5, 7
  board[i, j] = 1
  i, j = 6, 2
  board[i, j] = 1
  i, j = 7, 0
  board[i, j] = 1
  board.print()

try:
  n = 8
  board = Board(n)

  #_board_setup_5_steps_from_solution(board)
  exp_num = _get_experiment_number()
  board.rand_init()
  #_board_setup_flat(board)

  hill_climbing = HillClimbing(board)

  path = 'figures/'
  path += str(exp_num)
  path += '-experiment'
  path += '.txt'

  _save_board_setup(path, hill_climbing)

  line_plot = []

  for h in hill_climbing.execute():
    line_plot.append(h)
except KeyboardInterrupt:
    print("W: interrupt received, stopping…")
finally:
    n = len(line_plot)
    x = range(1, n + 1)
    plt.plot(x, [-x for x in line_plot])
    plt.ylabel('heuristic')
    plt.xlabel('state space')
    path = 'figures/'
    path += str(exp_num)
    path += '-experiment'
    plt.savefig(path)
    path += '.txt'
    _save_board_setup(path, hill_climbing)
    plt.show()