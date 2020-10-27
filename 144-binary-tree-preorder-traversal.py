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
