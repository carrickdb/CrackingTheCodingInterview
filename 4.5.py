import utils, math

def validateBSTRec(root, s,e):
    if not root:
        return True
    # print(root.val, s,e)
    if root.val <= s or root.val > e:
        return False
    return validateBSTRec(root.left, s, root.val) and validateBSTRec(root.right, root.val, e)


def validateBST(tree):
    return validateBSTRec(tree, -math.inf, math.inf)


tree = utils.createBST([0,1,2,3,4,5,6,7,8])
print(validateBST(tree)) # True
tree = utils.createTree({})
print(validateBST(tree)) # True

tree = {
    0:[None, None],
}
tree = utils.createTree(tree)
print(validateBST(tree)) # True

tree = {
    0:[1, 2],
}
tree = utils.createTree(tree)
print(validateBST(tree)) # False

tree = {
    0:[-5, 10],
    -5: [-10, 3],  # 3 is wrong
    10: [5, 15],
    5: [None, 7],
    15: [12, None]
}
tree = utils.createTree(tree)
print(validateBST(tree)) # False

tree = {
    0:[-5, 10],
    -5: [-10, -3],
    10: [5, 15],
    5: [None, 7],
    15: [12, None]
}
tree = utils.createTree(tree)
print(validateBST(tree)) # True

root = utils.BinaryTreeNode(10)
five = utils.BinaryTreeNode(5)
root.left = five
five.right = utils.BinaryTreeNode(10)
print(validateBST(root)) # True

root = utils.BinaryTreeNode(10)
fifteen = utils.BinaryTreeNode(15)
root.right = fifteen
fifteen.left = utils.BinaryTreeNode(10)
print(validateBST(root)) # False