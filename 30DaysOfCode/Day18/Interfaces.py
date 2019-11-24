#Problem Statement at: https://www.hackerrank.com/challenges/30-interfaces/problem

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum_ = 0
        for i in range(1,n+1):
            if n%i==0:
                sum_ = sum_+i
        return sum_


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
#print(type(my_calculator).__bases__[0]) #__bases__ return a tuple of base classes wrt to current class. __name__ fetches the name of base class.   
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)