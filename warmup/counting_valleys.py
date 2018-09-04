#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count, n_valleys = 0, 0
    for c in s:
        if count == -1 and c == "U":
            n_valleys += 1
        count = count + 1 if c == "U" else count - 1
    return n_valleys


# Read from input
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     s = input()
#
#     result = countingValleys(n, s)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

# Toy case
if __name__ == '__main__':
    n, s = 8, "UDDDUDUU"
    result = countingValleys(n, s)
    print(result)