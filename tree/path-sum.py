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
            else:
                bt = BTNode(next_data)
                bt.left = self.createBinaryTree(bt.left)
                bt.right = self.createBinaryTree(bt.right)
        except Exception as e:
            print(e)
        return bt

    def preorder(self, bt):
        if bt is None:
            print("#", end=" ")
        else:
            print(bt.key, end=" ")
            self.preorder(bt.left)
            self.preorder(bt.right)


import collections


def hasPathSum(root, target):
    if not root:
        return False
    q = collections.deque()
    q.append((root, root.key))
    while q:
        node, cur = q.popleft()
        cur = int(cur)
        if not node.left and not node.right and cur == target:
            return True
        if node.left:
            q.append((node.left, int(node.left.key) + cur))
        if node.right:
            q.append((node.right, int(node.right.key) + cur))
    return False


data_list = list(input("input node: ").split())  # 5 4 11 7 # # 2 # # # 8 13 # # 4 # 1 # #
target = int(input("target: "))
btree = BinaryTree(data_list)

root = btree.createBinaryTree()
# btree.preorder(root)

if hasPathSum(root, target):
    print("True")
else:
    print("False")
