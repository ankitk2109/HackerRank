#Problem statement at: https://www.hackerrank.com/challenges/30-review-loop/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
def oddEven(s):
    even=[]
    odd=[]
    s = list(s)
    for j in range(len(s)):
        if(j%2==0):
            even.append(s[j])
        else:
            odd.append(s[j])
    print("".join(even),"".join(odd))

t = int(input())
for i in range(t):
    s = input()
    oddEven(s)
