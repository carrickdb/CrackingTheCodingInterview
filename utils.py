from collections import deque
from typing import Dict

class BinaryTreeNode:
    def __init__(self, val, parent=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = parent

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def createLL(vals):
    head = Node(0)
    curr = head
    for i in vals:
        curr.next = Node(i)
        curr = curr.next
    return head.next

def printLL(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

def printBinaryTree(root: BinaryTreeNode):
    q = deque([root])
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            print(curr.val, end=" ")
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        print()

def createTree(g: Dict, bidirectional=False):
    """
    Expected format:
    tree = {
        0:[1,2], # 0 must be the root
        1:[3,4],
        2:[5,None],
        5:[None, 6]
    }
    """
    if len(g) == 0:
        return None
    root = BinaryTreeNode(0)
    s = [root]
    while s:
        curr = s.pop()
        if curr.val in g:
            lchild, rchild = g[curr.val]
            if rchild != None:
                if bidirectional:
                    right = BinaryTreeNode(rchild, curr)
                else:
                    right = BinaryTreeNode(rchild)
                curr.right = right
                s.append(right)
            if lchild != None:
                if bidirectional:
                    left = BinaryTreeNode(lchild, curr)
                else:
                    left = BinaryTreeNode(lchild)
                curr.left = left
                s.append(left)
    return root

def createBSTRec(arr,l,r):
    if l>=r:
        return None
    m = l + (r-l)//2
    root = BinaryTreeNode(arr[m])
    ls = createBSTRec(arr, l, m)
    rs = createBSTRec(arr, m+1, r)
    root.right = rs
    root.left = ls
    return root

def createBST(arr):
    return createBSTRec(arr, 0, len(arr))
