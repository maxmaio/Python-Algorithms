#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    s1Len = len(s1)
    s2Len = len(s2)
    arr = [[None]*(s2Len + 1) for i in range(s1Len + 1)] 
    
    for i in range(s1Len +1):
        for j in range(s2Len+1):
            if i ==0 or j==0:
                arr[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                arr[i][j] = arr[i-1][j-1]+1
            else:
                arr[i][j] = max(arr[i-1][j],arr[i][j-1])
    return arr[s1Len][s2Len]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
