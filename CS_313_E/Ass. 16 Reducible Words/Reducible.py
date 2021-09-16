#  File: Reducible.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
    if (n == 1):
        return False

    limit = int (n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
    pass

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
    pass

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
    pass

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
    pass

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
    pass

def make_word_dict():
    d = dict()
    fin = open("words.txt")
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', 'o', '']:
        d[letter] = letter
    return d


memo = {}
memo[''] = ['']


def is_reducible2(word, word_dict):
     # if have already checked this word, return the answer
    if word in memo:
        return memo[word]

    # check each of the children and make a list of the reducible ones
    res = []
    for child in children(word, word_dict):
        t = is_reducible2(child, word_dict)
        if t:
            res.append(child)

    # memoize and return the result
    memo[word] = res
    return res


def children(word, word_dict):
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)
    return res


def all_reducible(word_dict):
    res = []
    for word in word_dict:
        t = is_reducible2(word, word_dict)
        if t != []:
            res.append(word)
    return res


def print_trail(word):
    if len(word) == 0:
        return
    print (word)


def print_length_10(word_dict):
    words = all_reducible(word_dict)

    # use DSU to sort by word length
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    # print length 10 words
    length10 = []
    for length, word in t:
        if (length == 10):
            length10.append(word)

    length10.sort()
    for word in length10:
        print(word)

def main():

    word_dict = make_word_dict()
    print_length_10(word_dict)

    # create an empty word_list

    # open the file words.txt

    # read words from words.txt and append to word_list

    # close file words.txt

    # find length of word_list

    # determine prime number N that is greater than twice
    # the length of the word_list

    # create an empty hash_list

    # populate the hash_list with N blank strings

    # hash each word in word_list into hash_list
    # for collisions use double hashing 

    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than 
    # 0.2 * size of word_list

    # populate the hash_memo with M blank strings

    # create an empty list reducible_words

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words

    # find words of length 10 in reducible_words

    # print the words of length 10 in alphabetical order
    # one word per line

if __name__ == "__main__":
  main()