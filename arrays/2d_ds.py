#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglass_sums = []
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            hourglass_sums.append(sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3]))
    return max(hourglass_sums)

# Read from input
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     arr = []
#
#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))
#
#     result = hourglassSum(arr)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

# Toy case
if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]]
    print(hourglassSum(arr))
    
    arr = [[1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 9, 2, -4, -4, 0],
           [0, 0, 0, -2, 0, 0],
           [0, 0, -1, -2, -4, 0]]
    print(hourglassSum(arr))
