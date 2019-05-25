# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'doesCircleExist' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY commands as parameter.
#
N = 0
E = 1
S = 2
W = 3


def doesCircleExist(commands):
    # Write your code here
    result = []
    for command in commands:
        print(command)
        d = N
        x = 0
        y = 0
        for c in command:
            if c == 'L':
                d = (d-1) if d > 0 else 3
            elif c == 'R':
                d = (d+1) if d <3 else 0
            else :
                if d == N:
                    y+=1
                elif d == E:
                    x+=1
                elif d == S:
                    y-=1
                else:
                    x-=1
        if x == 0 and y == 0:
            result.append('YES')
        else
            result.append('NO')
        print(result)
    return result


if __name__ == '__main__':
    fptr = open('test_out.txt', 'w')

    commands_count = int(input().strip())

    commands = []

    for _ in range(commands_count):
        commands_item = input()
        commands.append(commands_item)

    result = doesCircleExist(commands)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()