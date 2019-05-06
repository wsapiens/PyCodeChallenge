# Enter your code here. Read input from STDIN. Print output to STDOUT

# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = [0] * 100
    for i in range(n):
        v = int(input().rstrip().split()[0])
        arr[v] += 1

    for i in range(1, 100):
        arr[i] = arr[i - 1] + arr[i]

    print(' '.join(map(str, arr)))
    print('\n')

# Input
# 10
# 4 that
# 3 be
# 0 to
# 1 be
# 5 question
# 1 or
# 2 not
# 4 is
# 2 to
# 4 the


# Output
# 1 3 5 6 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10