#Problem Statement avilable at: https://www.hackerrank.com/challenges/tree-level-order-traversal

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
def getHeight(root):
    if root == None:
        return -1
    else:
        left_height = getHeight(root.left)
        right_height = getHeight(root.right)
        max_height = 1+ max(left_height,right_height)
        return max_height

def printAtGivenLevel(root, level):
    if root== None:
        return
    if level == 1:
        print(root.info, end=' ')

    #Every time we move one level down we decrease the level. So when level==1 we can print the root.info. For eg if want to print the level 3 elements. Initially head is root and level=3. We move to root.left(subtree) and level=2. Again level!=1 then we move again to root.left and level=1. By this way we have reached to erd level and finally we can print the data.
    printAtGivenLevel(root.left,level-1) 
    printAtGivenLevel(root.right,level-1)

def levelOrder(root):
    height = getHeight(root)
    for i in range(height+1): #If the height of tree is 3 then there would be 4 levels. Hence we add 1 to height.
        printAtGivenLevel(root,i+1) #when i=0 level is 1, when i=1,l=2


    


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)