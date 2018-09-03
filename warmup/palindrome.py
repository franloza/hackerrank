#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    index = -1
    left_idx = 0
    right_idx = len(s) - 1
    while left_idx < right_idx:
        left_elem = s[left_idx]
        right_elem = s[right_idx]
        if left_elem != right_elem:
            if index == -1:
                next_right_elem = s[right_idx - 1]
                next_left_elem = s[left_idx + 1]
                if left_elem == next_right_elem and next_left_elem == right_elem:
                    if s[left_idx + 2] == next_right_elem:
                        index = left_idx
                        left_idx += 1
                    elif next_left_elem == s[right_idx-2]:
                        index = right_idx
                        right_idx -= 1
                    else:
                        return -1
                else:
                    if left_elem == next_right_elem:
                        index = right_idx
                        right_idx -= 1
                    else:
                        index = left_idx
                        left_idx += 1
            else:
                # More than two indexes is not possible
                return -1
        else:
            left_idx += 1
            right_idx -= 1

    return index


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

