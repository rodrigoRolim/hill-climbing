from board.board import Board
from hill_climbing import HillClimbing

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
print(hill_climbing.execute())

