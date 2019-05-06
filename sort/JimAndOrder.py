#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):
    result = []
    for i in range(1, len(orders)+1):
        result.append((i, sum(orders[i-1])))
    s = sorted(result, key=getKey)
    return [i[0] for i in s]

def getKey(item):
    return item[1]

if __name__ == '__main__':
    fptr = open('test4.txt', 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
