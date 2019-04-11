import numpy as np
from numpy.random import randint as rand
from math import factorial as factorial
from board import Board

QUEEN = -1
N = 8

def init_board():
	board = Board(N)
	board.rand_init()	
  
	return board

board = init_board()
print(board)

def calculate_heuristic(i, j, board):
	d = board.attackers_number()
	r = board.count_attack_row()
	print(d, 'diag')
	print(r, 'row')
	return d + r

def hill_climbing(board):
  prev_h = 17
  prev_i = 0
  prev_j = 0
  loop = 0

  while True:
    if loop > 10:
      board = init_board()
      prev_h = 17
      prev_i = 0
      prev_j = 0
      loop = 0

    j = rand(8)
    for i in range(8):
      h = calculate_heuristic(i,j,board)
      
      if prev_h == 0:
        board[:, prev_j] = 0
        board[prev_i, prev_j] = QUEEN
        print(board.printBoard())
        return board

      if prev_h > h:
        prev_h = h
        prev_i = i
        prev_j = j

    board[:, prev_j] = 0
    board[prev_i, prev_j] = QUEEN
    loop += 1
  
#print(calculate_heuristic(5, 7, board))
hill_climbing(board)
#print(row_value(0, 7, board))
#print(board)