#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
     
    no_of_vallies=0
    up_counts=0
    for i in range(0,len(s)):
        if  s[i]=='U':
            up_counts+=1
            if up_counts==0:

                no_of_vallies+=1
        else:
            up_counts-=1        

     

    return no_of_vallies   



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
