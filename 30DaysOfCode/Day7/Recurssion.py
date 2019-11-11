#Problem Statement : https://www.hackerrank.com/challenges/30-recursion/

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if(n!=1):
        x = factorial(n-1)
        result = n*x
    else:
        x=1
        result = n*x
    return result #Returning value after each recursion
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
