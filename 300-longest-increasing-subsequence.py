class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dynamic programming + dichotomy
        # time: O(nlogn), space: O(n)

        # use tails[k] array to represent the minimum element 
        # at the end in a k+1 subsequence
        tails = [0] * len(nums)
        ans = 0

        for num in nums:
            
            # dichotomy, to place the current num, in an ordered subseq tails
            i, j = 0, ans

            while i < j:
                m = (i+j)//2
                if tails[m] < num: 
                    i = m+1
                else: 
                    j = m
            
            tails[i] = num
            
            # if current num is bigger than last element(all elements) in the tails
            # then update the ans
            if j == ans: 
                ans += 1
        return ans
