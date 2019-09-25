#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    pairs=0
    number_of_pair=[]
    freq=[]
    if n>=1 and n<=100:
        for k in ar:
            if k not in number_of_pair:
                number_of_pair.append(k)

    for k in number_of_pair:
        freq.append(ar.count(k))
    print(freq)
    print(number_of_pair)  

    for i in freq:
        pairs+=i//2

    return pairs    


             



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
