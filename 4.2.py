import utils

def createBST(arr,l,r):
    if l>=r:
        return None
    m = l + (r-l)//2
    root = utils.BinaryTreeNode(arr[m])
    ls = createBST(arr, l, m)
    rs = createBST(arr, m+1, r)
    root.right = rs
    root.left = ls
    return root

arr = [1,2,3,4,5,6,7,8,9,10]
# arr = [1,2,3]

tree = createBST(arr, 0, len(arr))
utils.printBinaryTree(tree)