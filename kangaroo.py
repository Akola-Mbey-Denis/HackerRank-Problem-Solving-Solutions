#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    check =False

    while x1!=x2 and x1<=10000 and x2<=10000 and v1<=10000and v2<=10000:
        x1=x1+v1
        x2=x2+v2
        if x1==x2:
            check=True
    if check:
        return "YES" 
    else:
        return "NO"           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
