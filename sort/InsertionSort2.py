#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the insertionSort2 function below.
def insertion_sort2(n, arr):
    for i in range(1, n):
        val = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] > val:
                arr[j + 1] = arr[j]
            else:
                arr[j + 1] = val
                break
            if j == 0:
                arr[0] = val
        printArray(arr)


def printArray(arr):
    print(' '.join(str(e) for e in arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertion_sort2(n, arr)
