import numpy as np
from random import randint as rand

board = np.arange(64).reshape(8, 8)
print(board)
# begin left-right
print('secondary')

n = len(board)
row = 0
end_row = n
# andar triângulo superior e secundária
while row < end_row:
  i = row
  j = 0
  while i >= 0:
    if i != 0:
      print(board[i, j], end=' ')
    else:
      print(board[i, j])
    i -= 1
    j += 1
  row += 1

# andar sumente triângulo inferior
row = 1
while row < end_row:
  i = end_row - 1
  j = row
  while j < end_row:
    if j != end_row - 1:
      print(board[i, j], end=' ')
    else:
      print(board[i, j])
    i -= 1
    j += 1
  row += 1
# end left-right
print('main')

print(board)

n = len(board)
i = 0
j = 0
column = 0
last_column = n - 1
last_row = n
# andar principal e triângulo superior
while column <= last_column:
  while i < last_row:
    if j == last_column:
      print(board[i][j])
    else:
      print(board[i][j], end=' ')
    i += 1
    j += 1
  column += 1
  last_row -= 1
  i = 0
  j = column

i = 1
j = 0
row = 1
last_row = n - 1
# andar somente triângulo inferior
while row <= last_row:
  while i <= last_row:
    if i == last_row:
      print(board[i][j])
    else:
      print(board[i][j], end=' ')
    i += 1
    j += 1
  row += 1
  i = row
  j = 0