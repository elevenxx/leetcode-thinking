class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        b = b % len(s)
        alls = {s}
        
        def addOp(s):
            ans = [c for c in s]
            for i in range(1, len(s), 2):
                ans[i] = str((int(s[i]) + a))[-1]
            return ''.join(ans)
        
        def circleOp(s):
            return s[-b:]+s[:-b]
        
        # brute force, consider all possible outcomes 
        # after add and circle operations
        def dfs(s):
            alls.add(s)
            s1 = addOp(s)
            s2 = circleOp(s)

            if s1 not in alls:
                dfs(s1)
            if s2 not in alls:
                dfs(s2)
        
        dfs(s)
        return min(alls)
