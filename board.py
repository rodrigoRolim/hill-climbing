import numpy as np

class Board:

	def __init__(self):
		self.board = np.zeros((8,8), dtype=int)

	def addQueen(self, row, column):
		
		self.board[row, column] = -1