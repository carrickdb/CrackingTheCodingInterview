import utils, math


def checkBalance(root):
    if root == None:
        return -1
    err = -math.inf
    lh = checkBalance(root.left)
    rh = checkBalance(root.right)
    if lh==err or rh==err:
        return err
    diff = abs(lh - rh)
    if diff > 1:
        return err
    return max(lh, rh)+1

def isBalanced(root):
    return checkBalance(root) != -math.inf


tree = {
    0:[1,2],
    2:[5,None],
}

bt = utils.createTree(tree)
utils.printBinaryTree(bt)
print()
print(isBalanced(bt))
