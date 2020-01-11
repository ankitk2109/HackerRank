#Problem Statement at: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    if root == None: #If there are no left or right child then return -1
        return -1
    else:
        left_height = getHeight(root.left) #Finding left height
        right_height = getHeight(root.right)
        max_height = 1+ max(left_height,right_height) #Adding 1 because the above recurssion misses the edge from root(we can say current node) to next Level. Hence we need to add that edge.
        return max_height
    '''
    #OR
    if(root==None):
        return -1
    return 1 + max(height(root.left), height(root.right))
    '''

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))