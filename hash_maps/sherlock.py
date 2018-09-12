#!/bin/python3
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    anagrams = 0
    substrings_letters_count = []
    getSubstringsLetterCount(s, substrings_letters_count)
    anagrams_count = Counter(substrings_letters_count)
    for key in anagrams_count:
        # Binomial coefficient of (n | 2) = n * (n-1) / 2 -> Combinations of n elements in pairs
        anagrams += anagrams_count[key] * (anagrams_count[key]-1) // 2
    return anagrams

def getSubstringsLetterCount(s, substrings_letters_count):
    for i in range(len(s)):
        substrings_letters_count.append(freezeDict(Counter(s[i:])))
        if i == 0:
            getSubstringsLetterCount(s[i: i - 1], substrings_letters_count)

def freezeDict(dictionary):
    # Unordered sequence of items. It's the same {(a, 1), (b,1)} than {(b,1), (a,1)}. Not necessary to sort
    return frozenset(dictionary.items())


# Read from input
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     q = int(input())
#
#     for q_itr in range(q):
#         s = input()
#
#         result = sherlockAndAnagrams(s)
#
#         fptr.write(str(result) + '\n')
#
#     fptr.close()

# Toy case
if __name__ == '__main__':
    print(sherlockAndAnagrams("ifailuhkqq")) # 3
    print(sherlockAndAnagrams("kkkk"))  # 6 + 3 + 1 = 10