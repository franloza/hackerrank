#!/bin/python3
import os
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    c = Counter(magazine.split(' '))
    for word in note.split(' '):
        count = c.get(word, 0)
        if count == 0:
            return "No"
        else:
            c[word] -= 1
    return "Yes"

# Read from input
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip()

    note = input().rstrip()

    res = checkMagazine(magazine, note)

    fptr.write(str(res) + '\n')

    fptr.close()

# Toy case
if __name__ == '__main__':
    magazine = "give me one grand today night"
    note = "give one grand today"
    print(checkMagazine(magazine, note)) # Yes