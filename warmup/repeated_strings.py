#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    n_a = sum(1 for letter in s if letter == "a")
    n_a *= n // len(s)
    n_a += sum(1 for letter in s[:n % len(s)] if letter == "a")
    return n_a

# Read from input
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     n = int(input())
#
#     result = repeatedString(s, n)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

# Toy case
if __name__ == '__main__':
    s,n = "aba", 10
    result = repeatedString(s, n)
    print(result)

    s,n = "a", 1000000000000
    result = repeatedString(s, n)
    print(result)