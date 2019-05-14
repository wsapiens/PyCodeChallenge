#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the pangrams function below.
def pangrams(s):
    n = set()
    for c in s.lower():
        if c != ' ':
            n.add(c)
    if len(n) >= 26:
        return 'pangram'
    return 'not pangram'


if __name__ == '__main__':
    fptr = open('test3.txt', 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
