import unittest
from board.board import Board

class TestBoard(unittest.TestCase):

  def setUp(self):
    self._N = 8
    self._board = Board(self._N)

  def test_init(self):
    self._board
    for i in range(8):
      for j in range(8):
        self.assertTrue(self._board[i, j] == 0)
    self._board.print()

  def test_add_queen01(self):
    i, j = 0, 0
    self._board[i, j] = 1
    self._board.print()
    self.assertEquals(self._board[i, j], 1)

  def test_add_queen02(self):
    i, j = 4, 0
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 5, 1
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 6, 2
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 3, 3
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 4, 4
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 5, 5
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 6, 6
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 5, 7
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    self._board.print()
  
  def test_find_queen(self):
    i, j = 4, 0
    self._board[i, j] = 1
    k, l = self._board.find_queen(j)
    self.assertEquals(i, k)
    self.assertEquals(j, l)
  
  def test_remove_queen(self):
    i, j = 3, 2
    self._board[i, j] = 1
    k, l = self._board.remove_queen(j)
    self.assertEquals(i, k)
    self.assertEquals(j, l)

  def test_move_queen_on_empty_board(self):
    i, j = 7, 7
    k, l = self._board.move_queen(i, j)
    self.assertEquals(self._board[i, j], 1)
    self.assertEqual(i, k)
    self.assertEqual(j, l)
  
  def test_undo_last_add_queen(self):
    i, j = 6, 2
    self._board[i, j] = 1
    self.assertEqual(self._board[i, j], 1)
    self._board.undo_last_move()
    self.assertEqual(self._board[i, j], 0)

  def test_undo_last_remove_queen(self):
    i, j = 2, 2
    self._board[i, j] = 1
    self.assertEqual(self._board[i, j], 1)
    self._board.remove_queen(j)
    self.assertEqual(self._board[i, j], 0)
    self._board.undo_last_move()
    self.assertEqual(self._board[i, j], 1)

  def test_count_atack_row(self):
    i, j = 4, 0
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 5, 1
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 6, 2
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 3, 3
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 4, 4
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 5, 5
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 6, 6
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 5, 7
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    self._board.print()

    self.assertEquals(5, self._board.count_atack_row())

  def test_count_main_diagonal(self):
    i, j = 4, 0
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 5, 1
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 6, 2
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 3, 3
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 4, 4
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 5, 5
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 6, 6
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 5, 7
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    self._board.print()

    self.assertEquals(9, self._board.count_main_diagonal())

  def test_count_secondary_diagonal(self):
    i, j = 4, 0
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 5, 1
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 6, 2
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 3, 3
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 4, 4
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 5, 5
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 6, 6
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    i, j = 5, 7
    self._board[i, j] = 1
    self.assertTrue(self._board[i, j] == 1)
    self._board.print()

    self.assertEquals(3, self._board.count_secondary_diagonal())

if __name__ == '__main__':
	unittest.main()
