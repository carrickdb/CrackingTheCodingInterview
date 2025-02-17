import utils

arr = [1,2,3,4,5,6,7,8,9,10]
# arr = [1,2,3]

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


tree = createBST(arr, 0, len(arr))
utils.printBinaryTree(tree)
print()

def getLevels(root):
    levels = []
    currLevel = None
    if root:
        currLevel = utils.Node(root)
    while currLevel:
        levels.append(currLevel)
        lastLevel = currLevel
        currLevel = utils.Node(0)
        newNode = currLevel
        while lastLevel:
            if lastLevel.val.left:
                newNode.next = utils.Node(lastLevel.val.left)
                newNode = newNode.next
            if lastLevel.val.right:
                newNode.next = utils.Node(lastLevel.val.right)
                newNode = newNode.next
            lastLevel = lastLevel.next
        currLevel = currLevel.next
    return levels

for l in getLevels(tree):
    while l:
        print(l.val.val, end=" ")
        l = l.next
    print()