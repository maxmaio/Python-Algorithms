#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s1,s2):
    alphabet = [0]*26
    for x in s1:
        tmp = ord(x)- ord('a')
        alphabet[tmp] +=1
    count = 0
    for x in s2:
        tmp = ord(x)- ord('a')
        alphabet[tmp] -=1
        if (alphabet[tmp] < 0) : 
            count += 1
  
    return count
if __name__ == '__main__':

    s1 = input()
    s2 = input()
    if len(s1) != len(s2):
        print(-1)
    else:
        result = isValid(s1, s2)
        print(result)
