class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        # step 1: map position and characters
        dic = collections.defaultdict(list)
        for i, c in enumerate(s):
            dic[c].append(i)
        ans = -1

        # step 2: for each character, calcaulate their maximum length
        # between two same chars, which is the distance between first and following
        for k in dic:
            cur = dic[k]
            for j in range(1, len(cur)):
                ans = max(ans, cur[j]-cur[0]-1)
        
        return ans
