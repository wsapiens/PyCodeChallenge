#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    # alphabet list
    al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',\
          'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',\
          's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # rotated
    ro = al[k%26:]+al[:k%26]
    result = ''
    for c in s:
        # check case
        cc = ord(c.lower()) - ord(c)
        if cc > 0:
            i = ord(c) - ord('A')
        else:
            i = ord(c) - ord('a')
        if 25 >= i >= 0:
            if cc > 0:
                result += ro[i].upper()
            else:
                result += ro[i]
        else:
            result += c
    return result

if __name__ == '__main__':
    fptr = open('test2.txt', 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
