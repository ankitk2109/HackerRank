#Problem Statement available at: 1https://www.hackerrank.com/challenges/s10-binomial-distribution-1

#Binomial Distribution: b(x,n,p) = (nCx)*(p**x)*(q**(n-x)), where nCx is combination

from math import factorial

def bionomial(x,n,p):
    factional_part = factorial(n)/(factorial(x)*factorial(n-x))
    result =factional_part*p**x*(1-p)**(n-x) 
    return result


if __name__ == "__main__":
    a,b = map(float, input().split())
    p = a/(a+b)
    n = 6
    answer = 0
    for x in range(3,7):
        answer+= bionomial(x,n,p)
    print(round(answer,3))