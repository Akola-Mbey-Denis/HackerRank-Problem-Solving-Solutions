#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(a):
    m = M = a[0]
    x=y=0
    for i in a[1:]:
        if i > M:
            M = i
            x += 1
        elif i < m:
            m = i
            y += 1
    return str(x)+""+str(y)
    





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
