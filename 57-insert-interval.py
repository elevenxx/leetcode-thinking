class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        placed = False
        ans = []
        for l, r in intervals:
            if l > right:
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([l, r])
            elif r < left:
                ans.append([l, r])

            # intersection exists
            else:
                left = min(left, l)
                right = max(right, r)
        
        if not placed:
            ans.append([left, right])
        return ans
