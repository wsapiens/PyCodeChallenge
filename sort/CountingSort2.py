#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i

    count = [0]*(max+1)
    result = []

    for i in arr:
        count[i] = count[i] + 1
    for i in range(0, len(count)):
        c = count[i]
        while(c > 0):
            result.append(i)
            print(str(i))
            c -= 1
    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('test2.txt', 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()