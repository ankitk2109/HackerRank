#Problem Statement available at: https://www.hackerrank.com/challenges/tree-top-view

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
'''
Steps to find the top view of the Tree.
1. Create a queue and Initialise it with the root node of tree.
2. Create a horizontal distance(hd) whose initial value is set to zero.
3. Initialise the root.level= hd for start.
4. Run a loop until the queue is empty.
5. Firstly pop the first element, check if its hd is preseny in dic. If not insert.
6. Check if current nodes, left and right child exists. If exist then adjust the hd accordingly and insert them into the queue.
'''
def topView(root):
    if(root == None):
        return
    queue = [];dic = {}
    queue.append(root)
    
    #Initialising horizontal distance(hd)=0 and level = hd
    hd=0
    root.level = hd

    while(len(queue)!=0):
        root = queue.pop(0)
        hd = root.level

        if(hd not in dic):        
            dic[hd]= root.info
        
        if(root.left):
            root.left.level = hd - 1 
            queue.append(root.left)

        if(root.right):
            root.right.level = hd + 1
            queue.append(root.right)

    for i in sorted(dic):
        print(dic[i], end = ' ')




tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)