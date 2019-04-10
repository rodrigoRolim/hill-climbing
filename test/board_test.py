import unittest
from board import Board

class TestBoard(unittest.TestCase):

  def setUp(self):
    self._N = 8
    self.board = Board(self._N)
   
  def test_init(self):
    board = Board(self._N)
    for i in range(self._N):
      for j in range(self._N):
        self.assertTrue(board[i, j] == 0)
    board.printBoard()

  def test_add_queen01(self):
    i, j = 0, 0
    self.board[i, j] = 1
    self.board.printBoard()
    self.assertEquals(self.board[i, j], 1)

  def test_add_queen02(self):
    i, j = 4, 0
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 5, 1
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 6, 2
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 3, 3
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 4, 4
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 5, 5
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 6, 6
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 5, 7
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    self.board.printBoard()
  
  def test_find_queen(self):
    i, j = 4, 0
    self.board[i, j] = 1
    k, l = self.board.find_queen(j)
    self.assertEquals(i, k)
    self.assertEquals(j, l)
  
  def test_remove_queen(self):
    i, j = 3, 2
    self.board[i, j] = 1
    k, l = self.board.remove_queen(j)
    self.assertEquals(i, k)
    self.assertEquals(j, l)

  def test_move_queen_on_empty_board(self):
    i, j = 7, 7
    k, l = self.board.move_queen(i, j)
    self.assertEquals(self.board[i, j], 1)
    self.assertEqual(i, k)
    self.assertEqual(j, l)
  
  def test_undo_last_add_queen(self):
    i, j = 6, 2
    self.board[i, j] = 1
    self.assertEqual(self.board[i, j], 1)
    self.board.undo_last_move()
    self.assertEqual(self.board[i, j], 0)

  def test_undo_last_remove_queen(self):
    i, j = 2, 2
    self.board[i, j] = 1
    self.assertEqual(self.board[i, j], 1)
    self.board.remove_queen(j)
    self.assertEqual(self.board[i, j], 0)
    self.board.undo_last_move()
    self.assertEqual(self.board[i, j], 1)

  def test_count_atack_row(self):
    i, j = 4, 0
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 5, 1
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 6, 2
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 3, 3
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 4, 4
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 5, 5
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 6, 6
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 5, 7
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    self.board.printBoard()

    self.assertEquals(5, self.board.count_atack_row())

  def test_count_main_diagonal(self):
    i, j = 4, 0
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 5, 1
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 6, 2
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 3, 3
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 4, 4
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 5, 5
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 6, 6
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 5, 7
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    self.board.printBoard()

    self.assertEquals(9, self.board.count_main_diagonal())

  def test_count_secondary_diagonal(self):
    i, j = 4, 0
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 5, 1
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 6, 2
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 3, 3
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 4, 4
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 5, 5
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 6, 6
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    i, j = 5, 7
    self.board[i, j] = 1
    self.assertTrue(self.board[i, j] == 1)
    self.board.printBoard()

    self.assertEquals(3, self.board.count_secondary_diagonal())

if __name__ == '__main__':
	unittest.main()
