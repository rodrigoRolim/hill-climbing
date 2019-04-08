import numpy as np

class Board:
  def __init__(self):
    self.board = np.zeros((8,8), dtype=int)

  def get(self, row, column):
    return self.board[row, column]
  
  def __getitem__(self, key):
    return self.board[key]
  
  def __setitem__(self, key, value):
    self.board[key] = value
    return self.board
  
  def find_queen(self, column):
    return np.where(self.board[:, column] == -1)[0][0], column
    
  def print(self):
    print(self.board)