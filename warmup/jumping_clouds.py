#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    current_cloud = 0
    jumps = 0
    while current_cloud < len(c) - 1:
        if current_cloud + 2 < len(c) and c[current_cloud + 2] != 1:
            current_cloud += 2
        else:
            current_cloud += 1
        jumps += 1
    return jumps

# Read from input
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     c = list(map(int, input().rstrip().split()))
#
#     result = jumpingOnClouds(c)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

# Toy case
if __name__ == '__main__':
    n = 6

    c = [0, 0, 0, 0, 1, 0]

    result = jumpingOnClouds(c)

    print(result)
