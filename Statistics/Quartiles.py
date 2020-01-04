#Problem Statement available at: https://www.hackerrank.com/challenges/s10-quartiles/problem

n = int(input())
x = list(map(int,input().split()))

x.sort()
#print(x)

def median(x):
    n = len(x)
    if n%2 == 0:
       m  = int((x[int(n/2)] + x[int(n/2)-1])/2)
       return m
    else:
        m = x[int(n/2)]
        return m
if n%2 == 0:
    m  = int((x[int(n/2)] + x[int(n/2)-1])/2)
    q2 = m
    l = x[:int(n/2)]
    u = x[int(n/2):] 
    q1 = median(l)
    q3 = median(u)

else:
    m = x[int(n/2)]
    l = x[:x.index(m)]
    u = x[x.index(m)+1:]
    q2 = m
    q1 = median(l)
    q3 = median(u)

print(q1)
print(q2)
print(q3)
