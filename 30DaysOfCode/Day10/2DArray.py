#Problem statement at: https://www.hackerrank.com/challenges/30-2d-arrays/

#!/bin/python3

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    sum_list=[]
    for i in range(0,4):
        for j in range(0,4):
            sum_list.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
    return max(sum_list)

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    print((str(result) + '\n'))