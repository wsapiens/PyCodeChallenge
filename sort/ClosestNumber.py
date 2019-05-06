#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    result = []
    min = 0
    s = sorted(arr)
    for i in range(1, len(s)):
        # print(i)
        # print(s[i-1])
        # print(s[i])
        abs_diff = abs(s[i-1]-s[i])
        # print(abs_diff)
        if min > abs_diff or len(result) == 0:
            result.clear()
            result.append(s[i-1])
            result.append(s[i])
            min = abs_diff
        elif min == abs_diff:
            result.append(s[i-1])
            result.append(s[i])
    return result

if __name__ == '__main__':
    fptr = open('test3.txt', 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()