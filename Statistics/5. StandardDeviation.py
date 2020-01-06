#Problem Statement at: https://www.hackerrank.com/challenges/s10-standard-deviation

import math

n = int(input())
x = list(map(int,input().split()))

def cal_mean(x):
    return sum(x)/n

def mean_squared_dist(x,mean):
    sum_of_square = 0
    for ele in x:
        sum_of_square += (ele-mean)**2
    return sum_of_square
        
mean = cal_mean(x)
#print(mean)
sum_sq_dist = mean_squared_dist(x,mean)
#print(sum_sq_dist)

std_dev = math.sqrt(sum_sq_dist/n)
print(round(std_dev,1))