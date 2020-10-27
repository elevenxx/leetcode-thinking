class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stk = []
        ans = []
        while root or stk:
            while root:
                ans.append(root.val)
                stk.append(root)
                root = root.left
            root = stk.pop()
            root = root.right
        return ans

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []
