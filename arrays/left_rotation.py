#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    a = list(a) # Copy the list, we don't want to modify the reference. Just in case...
    for i in range(d):
        a.append(a.pop(0))
    return a

# Read from input
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     nd = input().split()
#
#     n = int(nd[0])
#
#     d = int(nd[1])
#
#     a = list(map(int, input().rstrip().split()))
#
#     result = rotLeft(a, d)
#
#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()

# Toy case
if __name__ == '__main__':
    n, d = 5, 4
    a = [1, 2, 3, 4, 5]
    print(rotLeft(a, d))
