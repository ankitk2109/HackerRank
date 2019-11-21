#Problem Statement at:https://www.hackerrank.com/challenges/30-queues-stacks/
class Solution:
    stack = []
    queue = []
    def pushCharacter(self,element):
        self.stack.append(element)
    def enqueueCharacter(self,element):
        self.queue.append(element)
    def popCharacter(self):
        return(self.stack.pop()) #Removing the last element from stack(LIFO)
    def dequeueCharacter(self):
        return(self.queue.pop(0))   #Removing the first element from queue(FIFO)
    '''
    def show(self):
        print("Stack:",self.stack)
        print("Queue:",self.queue)
    '''
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
