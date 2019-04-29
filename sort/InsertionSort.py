#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    val = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] > val:
            arr[i+1] = arr[i]
            printArray(arr)
        else:
            arr[i+1] = val
            printArray(arr)
            break
        if i == 0:
            arr[0] = val
            printArray(arr)

def printArray(arr):
    print( ' '.join(str(e) for e in arr) )


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)