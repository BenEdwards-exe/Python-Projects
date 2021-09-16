#  File: Boxes.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
    
    if (idx == len(box_list)):
        if (len(sub_set) >= 2):
            all_box_subsets.append(sub_set)
    else:
        sub_set2 = sub_set[:]
        sub_set.append(box_list[idx])
        if (fits(sub_set)):
            sub_sets_boxes(box_list, sub_set, idx+1, all_box_subsets)
        if (fits(sub_set2)):
            sub_sets_boxes(box_list, sub_set2, idx+1, all_box_subsets)
        else:
            idx += 1


def fits(current_box_list):

    isFit = True
    for i in range(len(current_box_list)-1):
        isFit = does_fit(current_box_list[i], current_box_list[i+1])
        if (not isFit):
            return isFit
    return isFit




# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets (all_box_subsets, largest_size, all_nesting_boxes):

    for i in range(len(all_box_subsets)):
        if (len(all_box_subsets[i]) > largest_size):
            largest_size = len(all_box_subsets[i])
    
    for i in range(len(all_box_subsets)):
        if (len(all_box_subsets[i]) == largest_size):
            all_nesting_boxes.append(all_box_subsets[i])
    
    print(largest_size)
    print(len(all_nesting_boxes))

    return

# returns True if box1 fits inside box2
def does_fit (box1, box2):
    return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
    # read the number of boxes 
    in_file = open ('boxes.in', 'r')
    line = in_file.readline()
    line = line.strip()
    num_boxes = int (line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range (num_boxes):
        line = in_file.readline()
        line = line.strip()
        box = line.split()
        for j in range (len(box)):
            box[j] = int (box[j])
        box.sort()
        box_list.append (box)

    # close the file
    in_file.close()

    '''
    # print to make sure that the input was read in correctly
    print (box_list)
    print()
    '''

    # sort the box list
    box_list.sort()

    '''
    # print the box_list to see if it has been sorted.
    print (box_list)
    print()
    '''

    # create an empty list to hold all subset of boxes
    all_box_subsets = []

    # create a list to hold a single subset of boxes
    sub_set = []

    # generate all subsets of boxes and store them in all_box_subsets
    sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)

    # initialize the size of the largest sub-set of nesting boxes
    largest_size = 0

    # create a list to hold the largest subsets of nesting boxes
    all_nesting_boxes = []

    # go through all the subset of boxes and only store the
    # largest subsets that nest in all_nesting_boxes
    largest_nesting_subsets (all_box_subsets, largest_size, all_nesting_boxes)

    # print the largest number of boxes that fit

    # print the number of sets of such boxes

if __name__ == "__main__":
    main()
