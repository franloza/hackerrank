#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    output = []
    c = defaultdict(int)
    f = defaultdict(int)
    for op, elem in queries:
        if op == 1:
            if f[c[elem]] > 0:
                f[c[elem]] -= 1
            c[elem] +=1
            f[c[elem]] += 1
        elif op == 2:
            if c[elem] > 0:
                f[c[elem]] -= 1
                c[elem] -= 1
                f[c[elem]] += 1
        else:
            output.append(int(f[elem] > 0))
    print(c)
    print(f)
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
