class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val<root.value:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def search(root, val):
    if not root or root.value == val:
        return root
    if val < root.value:
        return search(root.left, val)
    return search(root.right, val)

root = TreeNode(5)
insert(root, 2)
insert(root, 1)
insert(root, 3)
insert(root, 7)
insert(root, 6)
insert(root, 8)
search_result = search(root, 2)
print(search_result.value)
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

# Other implementations of BST

def maxDepth(root):
    if not root:
        return 0
    return 1+ max(maxDepth(root.left), maxDepth(root.right))


# Check if tree is balanced

def isBalanced(root):
    def check(node):
        if not node:
            return 0

        left = check(node.left)
        right = check(node.right)
        if left == -1 or right == -1 or abs(left - right)>1:
            return -1
        return 1+ max(left, right)
    return check(root)!=-1 

print(isBalanced(root))

# Lowest Common Ancestor (LCA)

def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p,q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    return left if left else right

# inverting a Binary Tree

def invertTree(root):
    if root:
        root.left, root,right = invertTree(root.right), invertTree(root.left)
    return root

# Same Tree 

def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.value!=q.value:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

