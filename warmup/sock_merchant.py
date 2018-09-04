#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks = {}
    for elem in ar:
        if elem in socks:
            socks[elem] += 1
        else:
            socks[elem] = 1
    return sum(elem // 2 for elem in socks.values())

# Read from input
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     ar = list(map(int, input().rstrip().split()))
#
#     result = sockMerchant(n, ar)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

# Toy case
if __name__ == '__main__':
    n, ar = 9, [10, 20, 20, 10, 10, 30, 50, 10, 20]
    print(sockMerchant(n, ar))
