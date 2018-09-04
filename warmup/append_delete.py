import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    if k > (len(s) + len(t)):
        return "Yes"
    movements = 0
    if len(s) > len(t):
        movements += len(s) - len(t)
        s = s[:len(t)]

    for i in range(len(t)):
        try:
            if s[i] != t[i]:
                # Pop and push len(s) - i elements
                movements += (len(s) - i) * 2
                break
        except IndexError:
            # Push len(t) - i elements
            movements += (len(t) - i)
            break
    return "Yes" if (movements <= k) and ((k-movements) % 2) == 0 else "No"

# Read from input
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     t = input()
#
#     k = int(input())
#
#     result = appendAndDelete(s, t, k)
#
#     fptr.write(result + '\n')
#
#     fptr.close()

# Toy case
if __name__ == '__main__':
    s, t, k = "hackerhappy", "hackerrank", 9
    print(appendAndDelete(s, t, k)) # Yes

    s, t, k = "aba", "aba", 7
    print(appendAndDelete(s, t, k)) # Yes

    s, t, k = "ashley", "ash", 2
    print(appendAndDelete(s, t, k)) # No

    s, t, k = "qwerasdf", "qwerbsdf", 6
    print(appendAndDelete(s, t, k))  # No

    s, t, k = "y", "yu", 2
    print(appendAndDelete(s, t, k))  # No

    s, t, k = "aaaaaaaaaa", "aaaaa", 7
    print(appendAndDelete(s, t, k))  # Yes

