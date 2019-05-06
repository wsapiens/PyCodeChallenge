#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    l = []
    for i in range(0, len(arr)):
        l.append((i+1, arr[i]))

    s = sorted(l, key=getKey)
    i = 1
    j = len(s)
    while i < j:
        sum = s[i-1][1]+s[j-1][1]
        if sum == m:
            break
        elif sum < m:
            i += 1
        elif sum > m:
            j -= 1
    return sorted([s[i-1][0], s[j-1][0]])

def getKey(item):
    return item[1]

if __name__ == '__main__':
    fptr = open('test.txt', 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()



# Sample Input
#
# 2
# 4
# 5
# 1 4 5 3 2
# 4
# 4
# 2 2 4 3
# Sample Output
#
# 1 4
# 1 2