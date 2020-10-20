class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
    
        # sort scores in the order of ages respectively
        ss = [b for a, b in sorted(zip(ages, scores))]
        
        # put a sentinel in the first place
        ss = [0] + ss

        # dp[i] represents the maximum value possible 
        # at and before position i
        # also known as the longest increasing sequence problem
        
        dp = [0] * len(ss)
        for i in range(1, len(ss)):
            for j in range(i):
                if ss[i] >= ss[j]:
                    dp[i] = max(dp[i], dp[j] + ss[i])
        
        return max(dp)
