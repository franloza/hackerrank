#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    sorted_prices = sorted(prices)
    toys, spent = 0, 0
    finish = False
    while (not finish and toys < len(sorted_prices)):
        if spent + sorted_prices[toys] < k:
            spent += sorted_prices[toys] 
            toys += 1
        else:
            finish=True
    return toys



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
