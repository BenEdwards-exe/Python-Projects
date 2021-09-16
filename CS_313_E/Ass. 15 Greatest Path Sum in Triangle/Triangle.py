#  File: Triangle.py

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

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):
    fill = []
    def brute_force_helper(grid, total, row, col, fill):
        total += grid[row][col]
        if (row == len(grid) - 1):
            fill.append(total)
        else:
            brute_force_helper(grid, total, row + 1, col, fill)
            brute_force_helper(grid, total, row + 1, col + 1, fill)
    brute_force_helper(grid, 0, 0, 0, fill)
    fill.sort() 
    return (fill[-1])

# returns the greatest path sum using greedy approach
def greedy (grid):
    idx = 1
    triangleSpot = 0
    greatest = grid[0][triangleSpot]
    while (idx < len(grid) and triangleSpot < len(grid[idx]) - 1):
        if (grid[idx][triangleSpot] < grid[idx][triangleSpot + 1]):
            triangleSpot += 1
        greatest += grid[idx][triangleSpot]
        idx += 1
    return (greatest)

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
    def recHelper(grid, row, col):
        if (row == len(grid) - 1):
            if (col == row):
                return (grid[row][col])
            return (max(grid[row][col], grid[row][col + 1]))
        else:
            return (grid[row][col] + max(recHelper(grid, row + 1, col), recHelper(grid, row + 1, col + 1)))
    return (recHelper(grid, 0, 0))

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    theTriangle = [[0 for num in row] for row in grid]
    for i in range(len(theTriangle) - 1, -1, -1):
        for j in range(len(theTriangle[i])):
            if (i == len(theTriangle) - 1):
                theTriangle[i][j] = grid[i][j]
                if (j == len(theTriangle) - 2):
                    theTriangle[i][j + 1] = grid[i][j + 1]
            else:
                theTriangle[i][j] = grid[i][j] + max(theTriangle[i + 1][j], theTriangle[i + 1][j + 1])
   
    return (theTriangle[0][0])

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
     # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int (line)

    # create an empty grid with 0's
    grid = [[0 for i in range (n)] for j in range (n)]

    # read each line in the input file and add to the grid
    for i in range (n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list (map (int, row))
        for j in range (len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid

def create_triangle_grid(grid: list):
    triangle_grid = list()
    for row in range(len(grid)):
        triangle_grid.append(list())
        for col in range(len(grid[row])):
            if (int(grid[row][col]) != 0):
                triangle_grid[row].append(0)
                triangle_grid[row][col] = int(grid[row][col])
    return triangle_grid


def main ():
    # read triangular grid from file
    grid = read_file()

    '''
    # check that the grid was read in properly
    print (grid)
    '''
    triangle_grid = create_triangle_grid(grid)

    # output greatest path from exhaustive search
    times = timeit ('brute_force({})'.format(triangle_grid), 'from __main__ import brute_force', number = 10)
    times = times / 10
    print("The greatest path sum through exhaustive search is ")
    print(brute_force(triangle_grid))
    # print time taken using exhaustive search
    print("The time taken for exhaustive search in seconds is ")
    print(times)
    print()

    # output greatest path from greedy approach
    times = timeit ('greedy({})'.format(triangle_grid), 'from __main__ import greedy', number = 10)
    times = times / 10
    print("The greatest path sum through greedy search is ")
    print(greedy(triangle_grid))
    # print time taken using greedy approach
    print("The time taken for greedy approach in seconds is")
    print(times)
    print()

    # output greatest path from divide-and-conquer approach
    times = timeit ('divide_conquer({})'.format(triangle_grid), 'from __main__ import divide_conquer', number = 10)
    times = times / 10
    print("The greatest path sum through recursive search is ")
    print(dynamic_prog(triangle_grid))
    # print time taken using divide-and-conquer approach
    print("The time taken for recursive search in seconds is ")
    print(times)
    print()

    # output greatest path from dynamic programming 
    times = timeit ('dynamic_prog({})'.format(triangle_grid), 'from __main__ import dynamic_prog', number = 10)
    times = times / 10
    print("The greatest path sum through dynamic programming is ")
    print(dynamic_prog(triangle_grid))
    # print time taken using dynamic programming
    print("The time taken for dynamic programming in seconds is ")
    print(times)
    print()

if __name__ == "__main__":
    main()
