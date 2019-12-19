#Problem Statement at: https://www.hackerrank.com/challenges/30-linked-list-deletion/
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        if(head==None):
            return
        elif(head.next==None):
            return head
        else:
            start = head
            tail = start.next
            while(start.next!=None):
                if(start.data == tail.data and tail.next == None):
                    start.next = None
                elif(start.data == tail.data and tail.next != None):
                    tail = tail.next
                    start.next = tail
                elif(start.data != tail.data and tail.next == None):
                    return head
                else:
                    tail = tail.next
                    start = start.next
            return head 

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 