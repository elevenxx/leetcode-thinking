class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A:
            return 0
        n = len(A)

        # left[i] represents the element at index i, reaching at most left as it can
        left = [0] * n
        for i in range(1, n):
            left[i] = (left[i-1] + 1 if A[i-1] < A[i] else 0)
        
        # right[i] represents the element at index i, reaching at most right as it can
        right = [0] * n
        for i in range(n-2, -1, -1):
            right[i] = (right[i+1] + 1 if A[i+1] < A[i] else 0)
        
        ans = 0
        # traverse left and right array, to find out the largest amount of elements
        for i in range(n):
            if left[i] > 0 and right[i] > 0:
                ans = max(ans, left[i] + right[i] + 1)
        
        return ans
