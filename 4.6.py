import utils


def getNext(root):
    if root == None:
        return None
    if root.right == None:
        parent = root.parent
        while parent:
            if parent.val >= root.val:
                return parent
            parent = parent.parent
        return None
    curr = root.right
    while curr.left:
        curr = curr.left
    return curr

g = {
    0: [-5,4],
    -5: [-10,-3],
    -3: [-4, None],
    4: [2,6],
}

tree = utils.createTree(g, bidirectional=True)
print(getNext(tree).val) # 2
print(getNext(tree.left).val) # -4
print(getNext(tree.right).val) # 6
print(getNext(tree.left.left).val) # -5
print(getNext(tree.left.right).val) # 0
print(getNext(tree.right.left).val) # 4
print(getNext(tree.right.right)) # None
print(getNext(None)) # None
print(getNext(utils.BinaryTreeNode(0))) # None