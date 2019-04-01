#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    numSwaps = 0
    for i in range(len(a)-1):
        for j in range(len(a) -1 - i):
            if a[j] > a[j+1]:
                # Swap
                a[j], a[j+1] = a[j+1], a[j]
                numSwaps += 1
    return numSwaps

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    numSwaps = countSwaps(a)

    print("Array is sorted in {} swaps.".format(numSwaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
