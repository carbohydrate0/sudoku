import itertools
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

def leftShiftIndex(arr, n): #配列arrをn個左にずらした配列を返す
   result = arr[n:] + arr[:n]
   return result

# sudoku[1] = leftShiftIndex(sudoku[1], 3)
# sudoku[2] = leftShiftIndex(sudoku[2], 6)
# sudoku[3] = leftShiftIndex(sudoku[3], 1)
# sudoku[4] = leftShiftIndex(sudoku[4], 4)
# sudoku[5] = leftShiftIndex(sudoku[5], 7)
# sudoku[6] = leftShiftIndex(sudoku[6], 2)
# sudoku[7] = leftShiftIndex(sudoku[7], 5)
# sudoku[8] = leftShiftIndex(sudoku[8], 8)
#正答例

print(sudoku)


number_not_included = [] #含まれていない数字を二次元配列で格納
number_not_included_all = [] #含まれていない数字の総当たりを格納


num = [1,2,3,4,5,6,7,8,9]

for column in sudoku: #行に含まれていない数字を探す
  if num != [1,2,3,4,5,6,7,8,9]:
    num = [1,2,3,4,5,6,7,8,9]
  for row in column:
    if row != 0:
      # print(num,row)
      num.remove(row)
  number_not_included.append(num)
  number_not_included_all.append(list(itertools.permutations(num)))



def solve():

  def challenge(temporary_list):
    for i in range(9):
      num = 0
      for j in range(9):
        if sudoku[i][j] == 0:
          sudoku[i][j] = temporary_list[num]
          num += 1

    if check_row(sudoku):
      if check_box(sudoku):
        return sudoku
      else:
        return True
    else:
      return True




  temporary_list = []
  finish_count = 1
  count = 0
  for n in number_not_included_all:
    finish_count *= len(n)
  for n1 in number_not_included_all[0]:
    time.sleep(1)
    for n2 in number_not_included_all[1]:
      for n3 in number_not_included_all[2]:
        for n4 in number_not_included_all[3]:
          for n5 in number_not_included_all[4]:
            for n6 in number_not_included_all[5]:
              for n7 in number_not_included_all[6]:
                for n8 in number_not_included_all[7]:
                  for n9 in number_not_included_all[8]:
                    temporary_list = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                    temporary_list = list(temporary_list)
                    if challenge(temporary_list):
                      temporary_list.clear()
                      count += 1
                    else:
                      for str in challenge(temporary_list):
                        print("\n", str)
                print(count,"/", finish_count)
              print("n7",count,"/", finish_count)
            print("n6")
          print("n5")
        print("n4")
      print("n3")
    print("n2")
  print("n1")





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
