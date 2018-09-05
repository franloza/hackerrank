#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
# def minimumSwaps(arr):
#     swaps = 0
#     for i in range(len(arr)-1):
#         elem = i+1
#         if elem != (arr[i]):
#             # Swap
#             idx = -1
#             for j in range(i+1, len(arr)):
#                 if arr[j] == elem:
#                     idx = j
#                     break
#             arr[idx] = arr[i]
#             arr[i] = elem
#             swaps += 1
#     return swaps

def minimumSwaps(arr):
    swaps = 0
    i = 0
    while i < len(arr)-1:
        if i != arr[i] - 1:
            swaps += 1
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
        else:
            i += 1
    return swaps


# Read from input
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     arr = list(map(int, input().rstrip().split()))
#
#     res = minimumSwaps(arr)
#
#     fptr.write(str(res) + '\n')
#
#     fptr.close()

# Toy case
if __name__ == '__main__':
    arr = [1, 3, 5, 2, 4, 6, 7] # 3
    print(minimumSwaps(arr))
    arr = [4, 3, 2, 1]
    print(minimumSwaps(arr)) # 2
    arr = [4, 3, 1, 2]
    print(minimumSwaps(arr)) # 3