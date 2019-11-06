#PROBLEM STATEMENT AT: https://www.hackerrank.com/challenges/dynamic-array/problem

1#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    seq={}
    for i in range(n):
        s= 'S'+str(i)
        seq[s]=[]

    result=[]
    lastAnswer = 0
    for j in range(len(queries)):
        x = queries[j][1]
        y = queries[j][2]
        idx = (x ^ lastAnswer)%n
        
        if (queries[j][0] == 1):
            pos = 'S'+str(idx)
            seq[pos].append(y)

        else :
            pos = 'S'+str(idx)
            idx_of_seq = y % len(seq[pos])
            lastAnswer = seq[pos][idx_of_seq]
            result.append(lastAnswer)

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
