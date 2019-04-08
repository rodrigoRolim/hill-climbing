import unittest
import sys
sys.path.append('../')
from board import Board

class TestBoard(unittest.TestCase):
  def test_init(self):
    board = Board()
    for i in range(8):
      for j in range(8):
        self.assertTrue(board[i, j] == 0)
    board.print()

  def test_add_queen(self):
    board = Board()
    i, j = 4, 0
    board[i, j] = -1
    self.assertTrue(board[i, j] == -1)
    i, j = 5, 1
    board[i, j] = -1
    self.assertTrue(board[i, j] == -1)
    i, j = 6, 2
    board[i, j] = -1
    self.assertTrue(board[i, j] == -1)
    i, j = 3, 3
    board[i, j] = -1
    self.assertTrue(board[i, j] == -1)
    i, j = 4, 4
    board[i, j] = -1
    self.assertTrue(board[i, j] == -1)
    i, j = 5, 5
    board[i, j] = -1
    self.assertTrue(board[i, j] == -1)
    i, j = 6, 6
    board[i, j] = -1
    self.assertTrue(board[i, j] == -1)
    i, j = 5, 7
    board[i, j] = -1
    self.assertTrue(board[i, j] == -1)
    board.print()
  
  def test_find_queen(self):
    board = Board()
    i, j = 4, 0
    board[i, j] = -1
    k, l = board.find_queen(j)
    self.assertEquals(k, i)
    self.assertEquals(l, j)

if __name__ == '__main__':
	unittest.main()
