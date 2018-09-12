#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the countTriplets function below.
def countTriplets(arr, r):
    B = defaultdict(int)
    C = defaultdict(int)
    triplets = 0
    for v in arr:
        triplets += C[v]
        C[v * r] += B[v]
        B[v * r] += 1
    return triplets


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
