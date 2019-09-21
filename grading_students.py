#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
   

    new_grades=[]
    student_new_grade=0
    

    for i in range(0,len(grades)):
        
        if grades[i]<38:
            new_grades.append(grades[i])
           
        else:
            x=grades[i]//5
            student_new_grade= int(x*5+5)
            print(student_new_grade)
            if(student_new_grade-grades[i]<3):  
                new_grades.append(student_new_grade)
            else:
                 new_grades.append(grades[i])
    for k in range(0,len(new_grades)):               
        if new_grades[k]>100:
            new_grades.replace(new_grades[i],100) 

    return new_grades             

              




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
