#Problem Statement: https://www.hackerrank.com/challenges/array-left-rotation/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def leftRotate(n,d,arr):
    temp = 0 #To store the first element which would be removed in each iteration
    for i in range(d): #Running loop 'd' times 
        temp = arr.pop(0) 
        arr.append(temp)
    arr = list(map(str,arr)) #we need string elements to join hence converting each element of list to string.
    return(" ".join(arr))


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = leftRotate(n,d,a)

    print (result)
