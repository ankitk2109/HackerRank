#Problem Statement at: https://www.hackerrank.com/challenges/30-more-exceptions/

#Write your code here
class Calculator():
    def power(self,n,p):
        if(n<0 or p<0):
            raise Exception('n and p should be non-negative') #Raised Exception will go to the subsequent Exception block of the caller function
        else:
            ans = n**p
            return ans

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   