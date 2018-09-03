#!/bin/python3

import os
import sys
from collections import deque

#
# Complete the equalStacks function below.
#
def equalStacks(*stacks):
    stack_sizes = [sum(a) for a in stacks]
    while len(set(stack_sizes)) > 1:
        max_stack_idx = stack_sizes.index(max(stack_sizes))
        stack_sizes[max_stack_idx] -= stacks[max_stack_idx].pop(0)
    return sum(stacks[0])

# Read from input
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n1N2N3 = input().split()
#
#     n1 = int(n1N2N3[0])
#
#     n2 = int(n1N2N3[1])
#
#     n3 = int(n1N2N3[2])
#
#     h1 = list(map(int, input().rstrip().split()))
#
#     h2 = list(map(int, input().rstrip().split()))
#
#     h3 = list(map(int, input().rstrip().split()))
#
#     result = equalStacks(h1, h2, h3)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

# Toy case
if __name__ == '__main__':

    n1, n2, n3 = 5, 3, 4
    h1 = [3, 2, 1, 1, 1]
    h2 = [4, 3, 2]
    h3 = [1, 1, 4, 1]

    result = equalStacks(h1, h2, h3)

    print(result) # 5
