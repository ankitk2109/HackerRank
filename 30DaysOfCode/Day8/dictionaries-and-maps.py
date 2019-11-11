# Problem Statement: https://www.hackerrank.com/challenges/30-dictionaries-and-maps

#!/bin/python3
import sys
def mergePhonebook(ph,q):
    for ele in range(len(q)-1):
        if q[ele] in ph.keys():
            print(q[ele]+'='+str(ph[q[ele]]))
        else:
            print('Not found')

n = int(input())
phonebook = {}
#Creating name and phone dictionary
for _ in range(n):
    record = input().split(" ")
    phonebook[record[0]] = int(record[1])
#print(phonebook)
query= []
flag=1
#Taking querries
while(flag):
    query.append(sys.stdin.readline().rstrip())
    if len(query[-1]) == 0: #Reading until user enters querries
        flag = 0

mergePhonebook(phonebook,query)
