#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    count = [0]*len(arr)
    for i in arr:
        count[i] = count[i] + 1
    for i in range(len(count)-1, -1, -1):
        if count[i] != 0:
            return count[:i+1]
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('test.txt', 'w')
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()