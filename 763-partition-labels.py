class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        # use an array to record each character last appearance index  
        last = [0] * 26
        for i, c in enumerate(S):
            last[ord(c)-ord("a")] = i
        
        partition = []
        # two pointers start and end, maintain current partition
        # initialize them
        start, end = 0, 0
        
        # greedy, each partition has all same characters as much as it can
        for i, c in enumerate(S):
            end = max(end, last[ord(c)-ord("a")])
            if i == end:
                partition.append(end-start+1)
                start = end + 1
        
        return partition
