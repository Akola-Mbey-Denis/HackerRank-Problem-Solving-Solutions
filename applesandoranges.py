#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    oranges_in_house=0
    apples_in_house=0
    for i in range(0,len(apples)):
        apples[i]=apples[i]+a

    for k in range(0,len(oranges)):
        oranges[k]=oranges[k]+b    
    
    #count oranges in house:
    for k in oranges:
        if k>=s and k<=t:
            oranges_in_house+=1
    #count apples in house       
    for j in apples:
        if j>=s and j<=t:
            apples_in_house+=1

    print(apples_in_house) 
    print(oranges_in_house)                   
     

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
