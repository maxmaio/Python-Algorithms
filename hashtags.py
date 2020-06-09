#!/bin/python3

import math
import os
import random
import re
import sys

def calculateMax(p1, p2, h1, h2):
    gap = p2 - p1 -1
    smaller = min(h1,h2)
    taller = max(h1,h2)
    if gap == 1:
        return 0
    heightDiff = abs(h2 -h1)
    
    delta = gap - heightDiff
    if gap < heightDiff:
        return gap + smaller
    if delta%2 == 0:
        return taller + delta/2
    else:
        return taller + int(delta/2) +1 


 

    return 0





# Complete the hourglassSum function below.
def maxHeight(tablePos, tableHeight):
    print(*tablePos)
    print(*tableHeight)
    result = 0
    for x in range(1,len(tablePos)):
        print(x)
        maxVal = calculateMax(tablePos[x-1] ,tablePos[x],tableHeight[x-1], tableHeight[x]) 
        if maxVal > result:
            result = maxVal
    return int(result)
    

if __name__ == '__main__':

    arr1 = []
    arr2 = []
    n1 = int(input())

    for _ in range(n1):
        arr1.append(int(input().rstrip()))
    n2 = int(input())
    if n1 != n2:
        print("table height and posistions not equal")
        sys.exit()
    for _ in range(n2):
        arr2.append(int(input().rstrip()))
    result = maxHeight(arr1, arr2)
    print(result)

