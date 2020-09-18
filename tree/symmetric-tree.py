class BTNode(object):
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, data_list):
        self.it = iter(data_list)

    def createBinaryTree(self, bt=None):
        try:
            next_data = next(self.it)
            if next_data == "#":
                bt = None
            else:  # preorder build
                bt = BTNode(next_data)
                bt.left = self.createBinaryTree(bt.left)
                bt.right = self.createBinaryTree(bt.right)
        except Exception as e:
            print(e)
        return bt

    def preorder(self, bt):
        if bt is not None:
            print(bt.key, end=" ")
            self.preorder(bt.left)
            self.preorder(bt.right)


def isSymmetric(root):
    if not root:
        return True

    def dfs(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.key != right.key:
            return False
        return dfs(left.left, right.right) and dfs(left.right, right.left)

    return dfs(root.left, root.right)


data_list = list(input("input node value: "))   # abd#g###ce##fh###   123##4##24##3##
btree = BinaryTree(data_list)
root = btree.createBinaryTree()
if isSymmetric(root):
    print("True")
else:
    print("False")