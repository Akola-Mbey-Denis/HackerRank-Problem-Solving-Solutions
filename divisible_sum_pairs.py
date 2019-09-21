#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, arr):
    count=0
    sum_array=[]


    if len(arr)>=2 and len(arr)<=100and k>=1 and k<=100:
        for i in range (0,len(arr)):
            for j in range(i+1,len(arr)):
                sum_array.append(arr[i]+arr[j])         
            

        for j in sum_array:
            if j%k==0:
                count+=1        

        print(sum_array)     
            
            
            
        return count            
                
      
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
