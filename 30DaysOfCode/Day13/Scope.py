# problem Statement at: https://www.hackerrank.com/challenges/30-scope/
class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        max_ = max(a)
        min_ = min(a)
        self.maximumDifference = max_- min_
        return self.maximumDifference
	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)