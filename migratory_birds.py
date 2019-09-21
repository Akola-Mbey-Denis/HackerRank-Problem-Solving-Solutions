#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    birds_species =[]
    count=0
    frequency=[]
    most_frequent=0
    arr.sort(key=None,reverse=False)
    for k in arr:
        if len(arr)>=5:
            if k not in birds_species:
                birds_species.append(k)
    print(birds_species)  

    
    for j in birds_species: 
        frequency.append(arr.count(j)) 
    print(frequency)         
               
    for l in range(0,len(birds_species)):
        if  birds_species[l-1]<birds_species[l] and frequency.index(max(frequency))==l:
            return birds_species[l]                       
                
                
    




                


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
