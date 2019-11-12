#Problem Statement: https://www.hackerrank.com/challenges/30-binary-numbers

#!/bin/python3

import math
import os
import random
import re
import sys


def cal_consecutive1s(n):
    l = []
    while(n>=1):
        r = int(n%2)
        l.append(r)
        n = n/2
    l = l[::-1]
    #print(l)
    count = 0
    max_=0
    i=0
    while(i<len(l)):
        if(l[i]==1):
            count +=1
            if(max_<count):
                max_ = count
        else:
            count = 0
        i +=1
    return max_
    
if __name__ == '__main__':
    n = int(input())
    result = cal_consecutive1s(n)
    print(result)