#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    alphabet = [0]*26
    final = []
    for x in s:
        tmp = ord(x)- ord('a')
        alphabet[tmp] +=1
    for x in alphabet:
        if x != 0:
            final.append(x)

    print(final)
    count =0
    i=0
    for x in final:
        if final[i]!= x:
            count +=1
          #  i += 1
        if count >1:
            return "NO"
    return "YES"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()