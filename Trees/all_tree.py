# Binary tree: Basic Implementation & Traversal

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# Build tree:
#       1
#     /   \
#    2     3
#   / \
#  4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Traversals
# Depth first search - DFS
print("DFS")
def inorder(root): # (LEFT, ROOT, RIGHT)
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)
print("INORDER: ")
inorder(root)
print("")
def preorder(root): # (ROOT, LEFT, RIGHT)
    if root: 
        print(root.value,end= " ")
        preorder(root.left)
        preorder(root.right)
print("PREORDER: ")
preorder(root)
print("")
def postorder(root): # (LEFT, RIGHT, ROOT)
    if root: 
        postorder(root.left)
        postorder(root.right)
        print(root.value,end= " ")
print("POSTORDER: ")
postorder(root)

'''
Output:
INORDER: 
4 2 5 1 3 
PREORDER: 
1 2 4 5 3 
POSTORDER: 
4 5 2 3 1
'''

# LEVEL ORDER TRAVERSAL - BFS 

from collections import deque

def level_order(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.value, end = " ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

print("")
print("LEVEL ORDER TRAVERSAL - BFS")
level_order(root)