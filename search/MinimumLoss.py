#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(price):
    p = []
    for i in range(len(price)):
        p.append((i, price[i]))
    s = sorted(price, reverse=True)

    min=0
    for i in range(len(s)-1):
        d = s[i]-s[i+1]
        if (d < min or min == 0) and price.index(s[i]) < price.index(s[i+1]):
            min =d
    return min


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()


# Sample Input 1
#
# 5
# 20 7 8 2 5
# Sample Output 1
#
# 2