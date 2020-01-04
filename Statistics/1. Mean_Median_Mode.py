#Problem Statement at: https://www.hackerrank.com/challenges/s10-basic-statistics/problem

size = int(input())
numbers = list(map(int, input().split()))
total = 0
dic = {}

#Calculating the mean
for ele in numbers:
    total += ele
mean = total/size

#Calculating the median
numbers.sort()
if(size%2 == 0):
    median = (numbers[int(size/2)-1] + numbers[int(size/2)])/ 2
else:
    median = numbers[int(size/2)+1]

#Calculating the mode
for ele in numbers:
    if ele not in dic.keys():
        dic[ele] = 1
    else:
        dic[ele] = dic[ele] + 1

max_val = max(dic.values())
lst =[]
for key,value in dic.items():
    if(value == max_val):
        lst.append(key)
mode = min(lst)

print(mean)
print(median)
print(mode)