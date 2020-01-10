#Problem Statement available at: https://www.hackerrank.com/challenges/tree-level-order-traversal
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    queue = [] #To store level wise address of nodes
    if(root == None):
        return
    else:
        queue.append(root) # Inserting root node to queue as it is the starting point.
        while(len(queue)!=0):   #Run until the queue is empty
            temp = queue.pop(0) #Removing the first node and storing its address into temp
            print(temp.info, end = ' ') #Printing the temp.info  
            if(temp.left):
                queue.append(temp.left)
            if(temp.right):
                queue.append(temp.right)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)