import utils

def getCommonAncestorRec(root, n1, n2):
    if not root.right and not root.left:
        return None, n1==root, n2==root
    r, r1, r2 = None, False, False
    l, l1, l2 = None, False, False
    if root.right:
        r,r1,r2 = getCommonAncestorRec(root.right, n1,n2)
    if root.left:
        l,l1,l2 = getCommonAncestorRec(root.left, n1,n2)
    if r: return r, True, True
    if l: return l, True, True
    n1Found = r1 or l1 or root==n1
    n2Found = r2 or l2 or root==n2
    if n1Found and n2Found:
        return root, True, True
    return None, n1Found, n2Found


def getCommonAncestor(root, n1, n2):
    return getCommonAncestorRec(root, n1, n2)[0]


g = {
    0: [-5,4],
    -5: [-10,-3],
    -3: [-4, None],
    4: [2,6],
}

tree = utils.createTree(g)

print(getCommonAncestor(tree, tree.left, tree.left.right.left).val)