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

    def inorder(self, bt):
        if bt is not None:
            self.inorder(bt.left)
            print(bt.key, end=" ")
            self.inorder(bt.right)


def invert(root):
    if not root:
        return
    root.left, root.right = root.right, root.left
    invert(root.left)
    invert(root.right)
    return root


data = input("input node value: ")  # abd#g###ce##fh###
data_list = list(data)
btree = BinaryTree(data_list)
root = btree.createBinaryTree()
print("preorder")
btree.preorder(root)
print("\ninorder")
btree.inorder(root)

root = invert(root)
print("\n\npreorder after invert")
btree.preorder(root)
print("\ninorder after invert")
btree.inorder(root)
