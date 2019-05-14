#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    result = []
    index = 0
    for c in s:
        if index != 0 and result[index-1] == c:
            result.pop()
            index -= 1
        else:
            result.append(c)
            index += 1
    if result:
        return ''.join(result)
    return 'Empty String'

if __name__ == '__main__':
    fptr = open('result.txt', 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

# Input (stdin)Download
# aaabccddd
# Your Output (stdout)
# abd