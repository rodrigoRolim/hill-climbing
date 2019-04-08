import numpy as np

class Board:
  '''Board class'''
  def __init__(self):
    '''Board class init with 0s'''
    self.board = np.zeros((8,8), dtype=int)
  
  def __getitem__(self, key):
    '''get item e.g. board[x, y]'''
    return self.board[key]
  
  def __setitem__(self, key, value):
    self.board[key] = value
    return self.board
  
  def find_queen(self, column):
    '''return: indices i, j'''
    return np.where(self.board[:, column] == -1)[0][0], column

  def remove_queen(self, row, column):
    '''to do'''
    
  def print(self):
    print(self.board)