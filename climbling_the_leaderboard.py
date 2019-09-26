 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    position=[]
    scores = sorted(list(set(scores)))[::-1]
    back = len(scores) - 1
    for a in alice:
        while back >= 0 and a > scores[back]:
            back -= 1
        if scores[back] == a:
            position.append(back+1)
        else:
            position.append(back+2)
    return position        


        
                 
             
                


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
