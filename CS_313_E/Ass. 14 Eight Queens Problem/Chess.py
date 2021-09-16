
#  File: Chess.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys

class Queens (object):
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()
    print ()

  # check if a position on the board is valid
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True
    
  # do the recursive backtracking
  def recursive_solve (self, col):
    if (col == self.n):
      return True
    else:
      for i in range (self.n):
        if (self.is_valid (i, col)):
          self.board[i][col] = 'Q'
          if (self.recursive_solve(col + 1)):
            return True
          self.board[i][col] = '*'
      return False

  # if the problem has a solution print the board
  def solve (self):
    for i in range (self.n):
      if (self.recursive_solve(i)):
        self.print_board()

  # Reset the board (make all positions '*')
  def reset_board (self):
    for row in range(self.n):
      for col in range(self.n):
        self.board[row][col] = '*'

  # Place queens on board
  def place_queens (self, queen_pos):
    for col in range(self.n):
      self.board[queen_pos[col]][col] = 'Q'



# Helper Function
# Permutes a 1D list and stores the permutations in global_perm_list
global_perm_a_list = []
def permuteList (a, lo):
  global global_perm_a_list
  hi = len(a)
  if (lo == hi):
    n = len(global_perm_a_list)
    global_perm_a_list.append([])
    global_perm_a_list[n] += a
    return
  else:
    for i in range (lo, hi):
      a[lo], a[i] = a[i], a[lo]
      permuteList(a, lo + 1)
      a[lo], a[i] = a[i], a[lo]



def main():
    # read the size of the board
    line = sys.stdin.readline()
    line = line.strip()
    n = int (line)

    # create a chess board
    game = Queens (n)


    # place the queens on the board and count the solutions
    num_range = list()
    for i in range(n):
        num_range.append(i)
    permuteList(num_range, 0)
    possible_positions = global_perm_a_list

    solutions = list()

    for test_positions in possible_positions:
      if len(test_positions)==len(set(test_positions[i]+i for i in range(len(test_positions))))==len(set(test_positions[i]-i for i in range(len(test_positions)))):
        solutions.append(test_positions)

    # print the number of solutions
    print(len(solutions))
 
if __name__ == "__main__":
  main()