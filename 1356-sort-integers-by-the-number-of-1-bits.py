class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dic = collections.defaultdict(list) 
        # use dic to map number ans its # of 1

        for i in arr:
            c = 0
            for s in str(bin(i)):
                if s == '1':
                    c += 1
            dic[c].append(i)
        
        ans = []
        for j in range(15):
            if dic[j]:
                for temp in sorted(dic[j]):
                    ans.append(temp)
        
        return ans
