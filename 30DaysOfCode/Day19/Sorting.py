#Problem Statement at:https://www.hackerrank.com/challenges/30-sorting

#!/bin/python3

def sortArray(n,a):
    numOfSwaps = 0
    for i in range(n):
        for i in range(n-i-1):
            if(a[i]>a[i+1]):
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                numOfSwaps += 1
        if(numOfSwaps == 0):
            break
    return a,numOfSwaps



n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
sortedArray,numOfSwaps = sortArray(n,a)

print("Array is sorted in",numOfSwaps,"swaps.")
print("First Element:",sortedArray[0])
print("Last Element:",sortedArray[-1])