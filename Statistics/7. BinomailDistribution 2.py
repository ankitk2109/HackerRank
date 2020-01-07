#Problem Statement available at: https://www.hackerrank.com/challenges/s10-binomial-distribution-2

'''
n = number of trials = 10

p = probability of reject in each trial = 0.12

x = number of reject

Probability of binomial distribution = nCx * (p**x) * ((1-p)**(n-x))

where nCx = n! / x! * (n-x)!
'''

from math import factorial

def bionomial(x,n,p):
    factional_part = factorial(n)/(factorial(x)*factorial(n-x))
    result =factional_part*p**x*(1-p)**(n-x) #q =(n-x)
    return result


if __name__ == "__main__":
    rej_per,n = map(int, input().split(' '))
    p = rej_per/100
    ans1 = 0
    ans2=0
    #No more than 2 rejects(0,1,2)
    for x in range(3):
        ans1+= bionomial(x,n,p)
    print(round(ans1,3))

    #At least 2 rejects(2,3,4,....,10)
    for x in range(2,n+1):
        ans2+= bionomial(x,n,p)
    print(round(ans2,3))
