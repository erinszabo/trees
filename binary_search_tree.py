"""

"""


def BinaryTree(r):
    """
    :param r: root node
    :return: a new binary tree, root with 2 empty children
    """
    return [r, [], []]


def insertLeft(root, newBranch):
    """
    :param root: parent of node to be inserted
    :param newBranch: node to be inserted
    :return:
    """
    t = root.pop(1)  # could have called getLeftChild here
    if len(t) > 1:  # is there a left child?
        root.insert(1, [newBranch, t, []])  # insert newBranch with the pre-existing child as a left child to it
    else:  # if there is not a child there
        root.insert(1, [newBranch, [], []])  # insert newBranch with no children
    return root


def insertRight(root, newBranch):
    """
    :param root: parent of node to be inserted
    :param newBranch: node to be inserted
    :return:
    """
    t = root.pop(2)  # could have called getRightChild here
    if len(t) > 1:  # is there a right child?
        root.insert(2, [newBranch, [], t])  # insert newBranch with the pre-existing child as a right child to it
    else:  # if there is not a child there
        root.insert(2, [newBranch, [], []])  # insert newBranch with no children
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]
