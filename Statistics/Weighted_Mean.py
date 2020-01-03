#Problem Statement available at: https://www.hackerrank.com/challenges/s10-weighted-mean/

N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))

sum_W = sum(W)
total = 0
for i in range(N):
    total += X[i]*W[i]

wt_avg = round((total/sum_W),1)

print(wt_avg)