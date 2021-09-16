  
#  File: Triangle.py

#  Description: Program that will apply four different approaches to problem solving to this single problem - exhaustive search.
# greedy, divide and conquer (recursive), and dynamic programming.  

#  Student's Name: Peyton Breech

#  Student's UT EID: pb23489

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: 12/8/2019

#  Date Last Modified: 12/9/2019

# DEPENDENCIES
import time
import random

# creates triangle
def makeTriangle(size):
    theTriangle = []
    for i in range (1, size):
        theTriangle.append([random.randint(1, size ** 2) for j in range(i)])
    return (theTriangle)

# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):
    fill = []
    def exhaustiveHelper(grid, total, row, col, fill):
        total += grid[row][col]
        if (row == len(grid) - 1):
            fill.append(total)
        else:
            exhaustiveHelper(grid, total, row + 1, col, fill)
            exhaustiveHelper(grid, total, row + 1, col + 1, fill)
    exhaustiveHelper(grid, 0, 0, 0, fill)
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
def rec_search (grid):
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
def read ():
    in_file = open("C:\\Users\\benjr\\Documents\\GitHub\\Ben_Fiverr\\hasanraza434\\Ass. 15 Greatest Path Sum in Triangle (due 26 Oct 2020)\\triangle.txt", "r")
    num_rows = int(in_file.readline().strip())
    return [[int(num) for num in in_file.readline().strip().split(" ")] for i in range(num_rows)]

def main ():
    # read triangular grid from file
    theTriangle = read()
    #theTriangle = makeTriangle(20)

    ti = time.time()
    # output greatest path from exhaustive search
    print(f"The greatest path sum through exhaustive search is {exhaustive_search(theTriangle)}.")
    tf = time.time()
    del_t = tf - ti
    # print time taken using exhaustive search
    print(f"The time taken for exhaustive search is {del_t} seconds.\n")

    ti = time.time()
    # output greates path from greedy approach
    print(f"The greatest path sum through greedy search is {greedy(theTriangle)}.")
    tf = time.time()
    del_t = tf - ti
    # print time taken using greedy approach
    print(f"The time taken for greedy search is {del_t} seconds.\n")

    ti = time.time()
    # output greates path from divide-and-conquer approach
    print(f"Greatest path from divide-and-conqure approach: {rec_search(theTriangle)}.")
    tf = time.time()
    del_t = tf - ti
    # print time taken using divide-and-conquer approach
    print(f"Time taken using divide-and-conquer approach: {del_t} seconds.\n")

    ti = time.time()
    # output greates path from dynamic programming 
    print(f"Greatest path from dynamic programming: {dynamic_prog(theTriangle)}.")
    tf = time.time()
    del_t = tf - ti
    # print time taken using dynamic programming
    print(f"Time taken using dynaimc programming: {del_t} seconds.")

if __name__ == "__main__":
    main()