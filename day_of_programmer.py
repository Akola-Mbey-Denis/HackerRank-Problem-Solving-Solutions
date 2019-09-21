 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    sum_of_days=0
    before_sum=0
    day=0
    month=0
    numbers_of_days_in_months=[31,28,31,30,31,30,31,31,30,31,30,31]

    if (year%400==0 or (year%100!=0 and year%4==0)) and (year>=1700 and year<=2700):
        numbers_of_days_in_months[1]=29
    elif (year%400!=0 or (year%100==0 and year%4!=0)) and (year>=1700 and year<=2700): 
        numbers_of_days_in_months[1]=28  
    if year==1918:
        numbers_of_days_in_months[2]=28-13    
       
    for k in range(0,len(numbers_of_days_in_months)):
        sum_of_days+=numbers_of_days_in_months[k]
        
        if sum_of_days>256:
            before_sum=sum(numbers_of_days_in_months[: k])
            day =256-before_sum
                          
             
             
            month =k+1
            break
               
    return str(day)+".0"+str(month)+"."+str(year)            




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
