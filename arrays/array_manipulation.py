#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * n
    for a, b, k in queries:
        arr[a - 1] += k
        if b < len(arr):
            arr[b] -= k
    expanding_max, expanding_sum = 0, 0
    for elem in arr:
        if expanding_sum + elem > expanding_max:
            expanding_max = expanding_sum + elem
        expanding_sum += elem
    return expanding_max

# Read from input
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     nm = input().split()
#
#     n = int(nm[0])
#
#     m = int(nm[1])
#
#     queries = []
#
#     for _ in range(m):
#         queries.append(list(map(int, input().rstrip().split())))
#
#     result = arrayManipulation(n, queries)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

# Toy case
if __name__ == '__main__':
    n = 5
    queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    print(arrayManipulation(n, queries)) # 200
    n = 40
    queries =[
        [29,40,787],[9,26,219],[21,31,214],[8,22,719],[15,23,102],[11,24,83],[14,22,321],[5,22,300],[11,30,832],[5,25,29],
        [16,24,577],[3,10,905],[15,22,335],[29,35,254],[9,20,20],[33,34,351],[30,38,564],[11,31,969],[3,32,11],
        [29,35,267],[4,24,531],[1,38,892],[12,18,825],[25,32,99],[3,39,107],[12,37,131],[3,26,640],[8,39,483],
        [8,11,194],[12,37,502]]
    print(arrayManipulation(n, queries))  # 8628