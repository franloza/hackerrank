#!/bin/python3
from itertools import combinations
import os

# Complete the acmTeam function below.
def acmTeam(topic):
    n_combinations = 0
    max_n_topics = 0
    for topic_items in combinations(topic, 2):
        n_topics = 0
        for i in range(len(topic_items[0])):
            if int(topic_items[0][i]) or int(topic_items[1][i]):
                n_topics += 1
        if n_topics > max_n_topics:
            max_n_topics = n_topics
            n_combinations = 1
        elif n_topics == max_n_topics:
            n_combinations += 1
    return max_n_topics, n_combinations


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
