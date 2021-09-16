# Input: n a positive integer
# Output: a bit string
def f ( n ):
    if (n == 0):
        return "0"
    elif (n == 1):
        return "1"
    elif (n > 1):
        return f(n - 1) + f(n - 2)


# Input: s and p are bit strings
# Output: an integer that is the number of times p occurs in s
def count_overlap (s, p):

    if (len(p)>len(s)):
        return 0

    count = 0
    for i in range(len(s)-len(p)):
        if (p == s[i:i+len(p)]):
            count += 1
    return count


def main():
    # read n and p from standard input
    n = input()
    p = input()

    # compute the bit string f(n)
    bitStr = f(int(n))

    # determine the number of occurrences of p in f(n)
    occr = count_overlap(bitStr, p)

    # print the number of occurrences of p in f(n)
    print(occr)


if __name__ == "__main__":
    main()