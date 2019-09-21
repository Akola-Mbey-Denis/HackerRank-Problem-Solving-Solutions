#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum_right=sum_left=0
    for i in range(0, len(arr)):
        for k in  range (0,len(arr[0])):
            if  i==k:
                sum_right+=arr[i][k]

    for j in range (len(arr)-1,-1,-1):
        for k in range(0,len(arr)):
            if j+k==(len(arr[0])-1):
                sum_left+=arr[j][k]
    return  abs(sum_right-sum_left )          



 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
