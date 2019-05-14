#!/bin/python3

import os
import sys


#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    s1 = []
    s2 = []
    s3 = []
    th1 = 0
    th2 = 0
    th3 = 0
    for i in range(len(h1)-1, -1, -1):
        th1 += h1[i]
        s1.append(h1[i])
    for i in range(len(h2)-1, -1, -1):
        th2 += h2[i]
        s2.append(h2[i])
    for i in range(len(h3)-1, -1, -1):
        th3 += h3[i]
        s3.append(h3[i])

    while True:
        sz1 = len(s1)
        sz2 = len(s2)
        sz3 = len(s3)
        if sz1 == 0 or sz2 == 0 or sz3 == 0:
            return 0

        if th1 == th2 and th2 == th3:
            return th1

        if th1 >= th2 and th1 >= th3:
            th1 -= s1.pop()
        elif th2 >= th1 and th2 >= th3:
            th2 -= s2.pop()
        elif th3 >= th1 and th3 >= th2:
            th3 -= s3.pop()


if __name__ == '__main__':
    fptr = open('test.txt', 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

# 5 3 4
# 3 2 1 1 1
# 4 3 2
# 1 1 4 1