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

""" def main_diagonal(i, j, board):
	length = len(board)
	queen_i = np.where(board[:, j] == QUEEN)[0][0]
	queen_j = j
	board[:, j] = 0
	board[i, j] = QUEEN
	queens = 0
	for diag in range(length):
		q = 0
		q += np.count_nonzero(board.diagonal(diag) == QUEEN)
		queens += 0 if q < 2 else int(factorial(q) / (2 * (factorial((q - 2)))))
		if diag != 0:
			q = 0
			q += np.count_nonzero(board.diagonal(-diag) == QUEEN)
			queens += 0 if q < 2 else int(factorial(q) / (2 * (factorial((q - 2)))))
	board[:, j] = 0
	board[queen_i, queen_j] = QUEEN
	return queens


def secondary_diagonal(row, column, board):
	length = len(board)
	queen_i = np.where(board[:, column] == QUEEN)[0][0]
	queen_j = column
	board[:, column] = 0
	board[row, column] = QUEEN

	queens = 0
	for k in range(length):
		i = k
		j = 0
		aux = 0
		while i >= 0:
			if i != 0:
				aux += np.count_nonzero(board[i, j] == QUEEN)
			else:
				aux += np.count_nonzero(board[i, j] == QUEEN)
				queens += 0 if aux < 2 else int(factorial(aux) / (2 * (factorial((aux - 2)))))
				aux = 0
			i -= 1
			j += 1

	for k in range(1, length):
		i = length - 1
		j = k
		aux = 0
		while j <= length - 1:
			if j != 7:
				aux += np.count_nonzero(board[i, j] == QUEEN)
			else:
				aux += np.count_nonzero(board[i, j] == QUEEN)
				queens += 0 if aux < 2 else int(factorial(aux) / (2 * (factorial((aux - 2)))))
				aux = 0
			i -= 1
			j += 1

	board[:, column] = 0
	board[queen_i, queen_j] = QUEEN
	return queens """


""" def diagonal_value(i, j, board):
	return main_diagonal(i, j, board) + secondary_diagonal(i, j, board )"""


""" def row_value(i, j, board):
	queen_i = np.where(board[:, j] == QUEEN)[0][0]
	queen_j = j
	board[:, j] = 0
	board[i, j] = QUEEN
	queens = 0
	for row in range(8):
		q = np.count_nonzero(board[row, :] == QUEEN)
		queens += 0 if q < 2 else int(factorial(q) / (2 * (factorial((q - 2)))))
	board[:, j] = 0
	board[queen_i, queen_j] = QUEEN
	return queens """


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