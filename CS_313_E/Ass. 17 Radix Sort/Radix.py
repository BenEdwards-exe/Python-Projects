
#  File: Radix.py

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

class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # check if the queue if empty
    def is_empty (self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
    longest_word = 0
    for word in a:
        if (len(word) > longest_word):
            longest_word = len(word)

    iterations = longest_word

    # Create a list and keep your Queue objects there.
    list_of_queue_objects = []
    for _ in range(36):
        list_of_queue_objects.append(Queue())

    # Create a dictionary where the key is a character (either a digit or a lower case letter) 
    # and the value is an index in the above list.
    dict_of_indicies = dict()
    index = 0
    for n in range(48, 58):
        dict_of_indicies[chr(n)] = index
        index += 1
    for n in range(97, 123):
        dict_of_indicies[chr(n)] = index
        index += 1


    store_queue = Queue()
    # Loop through a and sort
    for n in range(iterations-1, -1, -1):
        for word in a:
            letter = str()
            if (len(word) <= n):
                store_queue.enqueue(word)
            else:
                letter = word[n]
                index_of_queue_list = dict_of_indicies[letter]
                list_of_queue_objects[index_of_queue_list].enqueue(word)

        # Store queue in store list
        for queue_object in list_of_queue_objects:
            for _ in range(queue_object.size()):
                element = queue_object.dequeue()
                store_queue.enqueue(element)

        a = []
        for _ in range(store_queue.size()):
            a.append(store_queue.dequeue())
            
            

    return a

def main():
    # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int (line)

    # create a word list
    word_list = []
    for _ in range (num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append (word)

    '''
    # print word_list
    print (word_list)
    '''    

    # use radix sort to sort the word_list
    sorted_list = radix_sort (word_list)

    # print the sorted_list
    print (sorted_list)

if __name__ == "__main__":
  main()
