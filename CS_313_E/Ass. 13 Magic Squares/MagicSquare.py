#  File: MagicSquare.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise
def is_magic ( a ):
    
    order = 0
    for i in range(len(a)):
        if (i*i == len(a)):
            order = i
            break

    a2D = list()
    for i in range(order):
        a2D.append([])

    for i in range(order):
        for j in range(order):
            a2D[i].append(a[i*order + j])

    topSum = 0
    bottomSum = 0
    firstColumnSum = 0
    lastColumnSum = 0
    diagonal1Sum = 0
    diagonal2Sum = 0
    for i in range(order):
        # Sum top row
        topSum += a2D[0][i]
        # Sum bottom row
        bottomSum += a2D[order-1][i]
        # Sum first column
        firstColumnSum += a2D[i][0]
        # Sum last column
        lastColumnSum += a2D[i][order-1]
        # Sum 1st diagonal
        diagonal1Sum += a2D[i][i]
        # Sum 2nd diagonal
        diagonal2Sum += a2D[i][order-1-i]

    magicConstant = int( order * (order*order + 1) / 2 )
    
    isRowsMagic = (topSum==magicConstant) and (bottomSum==magicConstant)
    isColumnsMagic = (firstColumnSum==magicConstant) and (lastColumnSum==magicConstant)
    isDiagonalMagic = (diagonal1Sum==magicConstant and diagonal2Sum==magicConstant)

    return (isRowsMagic and isColumnsMagic and isDiagonalMagic)


# this function recursively permutes all magic squares
# a is 1-D list of integers and idx is an index in a
# it stores all 1-D lists that are magic in the list all_magic
def permute ( a, idx, all_magic ):
    permuteList(a,idx)
    global global_perm_a_list
    for i in range(len(global_perm_a_list)):
        if (is_magic(global_perm_a_list[i])):
            all_magic.append(global_perm_a_list[i])




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
    # read the dimension of the magic square
    in_file = open ('magic.in', 'r')
    line = in_file.readline()
    line = line.strip()
    n = int (line)
    in_file.close()

    '''
    # check if you read the input correctly
    print (n)
    '''

    # create an empty list for all magic squares
    all_magic = []

    # create the 1-D list that has the numbers 1 through n^2
    base_list = []
    for i in range(n*n):
        base_list.append(i+1)   
    

    # generate all magic squares using permutation 
    permute(base_list, 0, all_magic)

    # print all magic squares
    for i in all_magic:
        print(i)

if __name__ == "__main__":
    main()




