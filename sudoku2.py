import itertools
from itertools import product
import time
from tqdm import tqdm


sudoku = [
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
]

sudoku = [
  list(range(1,10)),
  list(range(1,10)),
  list(range(1,10)),
  list(range(1,10)),
  list(range(1,10)),
  list(range(1,10)),
  list(range(1,10)),
  list(range(1,10)),
  list(range(1,10))
]
sudoku = [
  [3,1,0,7,5,9,2,0,6],
  [2,5,0,0,0,0,0,9,0],
  [8,7,0,6,0,3,4,5,1],
  [0,0,0,9,6,0,0,3,4],
  [0,0,5,0,0,8,0,0,0],
  [0,3,0,0,0,0,6,0,8],
  [0,9,1,2,0,6,0,0,0],
  [0,6,0,0,0,0,0,4,0],
  [0,0,3,5,8,0,1,0,0],
]


def solve():
  no_use_all = []
  for i in range(9):
    for j in range(9):
      if sudoku[i][j] == 0:
        no_use = find_no_use_num(i, j)
        no_use_all.append(no_use)
  print(no_use_all)
  # a = 1
  # for n in no_use_all:
  #   a *= len(n)
  # print(a)
  combination = [*map(list, product(*no_use_all))]#ここの計算量膨大
  print(len(combination))
  



def find_no_use_num(row, column):
  num = [1,2,3,4,5,6,7,8,9]
  for r in sudoku[row]:
    if r in num:
      num.remove(r)
  for s in sudoku:
      if s[column] in num:
        num.remove(s[column])
  if (row+1) % 3 == 0:
    row1, row2 = row-1, row-2
  elif (row+1) % 3 == 2:
    row1, row2 = row-1, row+1
  else:
    row1, row2 = row+1, row+2

  if (column+1) % 3 == 0:
    column1, column2 = column-1, column-2
  elif (column+1) % 3 == 2:
    column1, column2 = column-1, column+1
  else:
    column1, column2 = column+1, column+2

  # print(row, row1, row2, column,column1, column2)

  if sudoku[row1][column1] in num:
    num.remove(sudoku[row1][column1])
  if sudoku[row1][column2] in num:
    num.remove(sudoku[row1][column2])
  if sudoku[row2][column1] in num:
    num.remove(sudoku[row2][column1])
  if sudoku[row2][column2] in num:
    num.remove(sudoku[row2][column2])

  return num




def check_row(sudoku):
  count = 0
  for i in range(9):
    num_sum = 0
    for column in sudoku:
      num_sum += column[i]
    if num_sum != 45:
      return False
    count += 1
    if count == 9:
      return True

def check_box(sudoku):
  def check(t1, t2, b1, b2):
    num_sum = 0
    for i in range(t1, b1):
      for j in range(t2, b2):
        num_sum += sudoku[i][j]
    if num_sum != 45:
      return False
    else:
      return True

  if not check(0, 0, 3, 3):
    return False
  if not check(0, 3, 3, 6):
    return False
  if not check(0, 6, 3, 9):
    return False
  if not check(3, 0, 6, 3):
    return False
  if not check(3, 3, 6, 6):
    return False
  if not check(3, 6, 6, 9):
    return False
  if not check(6, 0, 9, 3):
    return False
  if not check(6, 3, 9, 6):
    return False
  if not check(6, 6, 9, 9):
    return False

  return True




solve()
