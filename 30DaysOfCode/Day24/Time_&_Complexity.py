#Problem Statement at: https://www.hackerrank.com/challenges/30-running-time-and-complexity

import math
def isPrime(num):
    if (num > 1):
        for i in range(2,int(math.sqrt(num))+1):
            if(num%i==0):
                return("Not prime")
        return("Prime")
    else:
        return 'Not prime'

T =  int(input())

for _ in range(T):
    num = int(input())
    print(isPrime(num))

