#Problem Statement available at: https://www.hackerrank.com/challenges/s10-interquartile-range/

n = int(input())
e = list(map(int,input().split()))
f = list(map(int,input().split()))
ele_dic = dict(zip(e,f))
#print(ele_dic)
lst = []
for key in (ele_dic.keys()):
    for i in range(ele_dic[key]):
        lst.append(key)

lst.sort()
s = len(lst)

def median(x):
    n = len(x)
    if n%2 == 0:
       m  = ((x[int(n/2)] + x[int(n/2)-1])/2)
       return m
    else:
        m = x[int(n/2)]
        return m

if s%2 == 0:
    l = lst[:(s//2)]
    #print(l)
    u = lst[(s//2):]
    #print(u)
    q1 = median(l)
    #print(q1)
    q3 = median(u)
    #print(q3)
else:
    mid_idx = s//2
    l = lst[:mid_idx]
    #print(l)
    u = lst[mid_idx+1:]
    #print(u)
    q1 = median(l)
    #print(q1)
    q3 = median(u)
    #print(q3)

result = float(q3 - q1)
print(round(result,1))
