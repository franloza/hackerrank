#!/bin/python3

import os
import sys
import heapq

#
# Complete the cookies function below.
#
def cookies(k, A):
    #
    # Write your code here.
    #
    p_queue = list(A)
    heapq.heapify(p_queue)
    operations = 0
    while p_queue[0] < k and len(p_queue) > 1:
        least_sweet_cookie = heapq.heappop(p_queue)
        second_least_sweet_cookie = heapq.heappop(p_queue)
        result_cookie = least_sweet_cookie + 2*second_least_sweet_cookie
        heapq.heappush(p_queue, result_cookie)
        operations += 1
    if p_queue[0] < k:
        return -1
    else:
        return operations

# Read from input
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     nk = input().split()
#
#     n = int(nk[0])
#
#     k = int(nk[1])
#
#     A = list(map(int, input().rstrip().split()))
#
#     result = cookies(k, A)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

# Toy case
if __name__ == '__main__':
    n, k = 3, 10

    A = [1, 1, 1]

    result = cookies(k, A)

    print(result)