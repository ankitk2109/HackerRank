#Problem statement at: https://www.hackerrank.com/challenges/crush/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    m = [0]*(n+2) #Creating an array of size n+2( bcoz we want one extra element at end for comparision and given values index start from 1 so first element 0 and one extra ele at last so total 2 elements) and initializing all values to zero.
    #print(m)
    #print(queries)
    for row in queries:
        #a = row[0], b= row[1], k=row[2], Useful Link:https://www.youtube.com/watch?v=hDhf04AJIRs&list=PLSIpQf0NbcCltzNFrOJkQ4J4AAjW3TSmA
        m[row[0]] = m[row[0]]+row[2]  # m[a] = k
        m[row[1]+1] = m[row[1]+1] - row[2] #m[b+1] = m[b+1]-k, To balance the extra additions
        #print(m)

    sum_=0
    max_=0
    for ele in m:
        if ele == 0:
            continue
        sum_ +=ele
        if sum_>max_:
            max_=sum_
    return max_

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
