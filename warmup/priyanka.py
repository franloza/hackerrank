#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    sorted_w = sorted(w)
    result = 1
    n = sorted_w[0] + 5
    for elem in sorted_w[1:]:
        if elem >= n:
            result +=1
            n = elem + 5
    return result

if __name__ == '__main__':
    print(toys([1, 2, 3, 21, 7, 12, 14, 21]))