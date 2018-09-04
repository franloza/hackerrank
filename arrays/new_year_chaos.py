#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
# def minimumBribes(q):
#     bribes = [0] * len(q)
#     for i in reversed(range(1, len(q)+1)):
#         num_to_place = i
#         while q[i-1] != num_to_place:
#             idx_num_to_place = q.index(num_to_place)
#             # Swap
#             if bribes[num_to_place-1] < 2:
#                 q[idx_num_to_place], q[idx_num_to_place+1] = q[idx_num_to_place+1], q[idx_num_to_place]
#                 bribes[num_to_place-1] += 1
#             else:
#                 return "Too chaotic"
#     return sum(bribes)

def minimumBribes(q):
    for i, elem in enumerate(q):
        if elem - i > 3:
            return "Too chaotic"
    swaps, swapped = 0, False
    for i in range(len(q)-1):
        for j in range(0, len(q)-i-1):
            if q[j] > q[j+1]:
                # Swap
                q[j], q[j+1] = q[j+1], q[j]
                swaps +=1
                swapped = True
        # If there were no swaps in the iteration, we are done
        if swapped:
            swapped = False
        else:
            break
    return swaps

# Read from input
# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     fptr = open('a.txt', 'w')
#
#     t = int(input())
#
#     for t_itr in range(t):
#         n = int(input())
#
#         q = list(map(int, input().rstrip().split()))
#
#         result = minimumBribes(q)
#
#         fptr.write(str(result))
#         fptr.write('\n')
#
#     fptr.close()

# # Toy case
if __name__ == '__main__':
    print(minimumBribes([2, 1, 5, 3, 4])) # 3
    print(minimumBribes([2, 5, 1, 3, 4])) # Too chaotic
    print(minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]))  # Too chaotic
    print(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]))  # 7
