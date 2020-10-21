class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        # this solution considers the edges, not nodes
        # use linked-list g to record each node and its linked edges linked to another node
        # undirected graph, so swap if necessary for preparing next set union
        g = [[] for _ in range(n)]
        for edge in roads:
            if edge[0] < edge[1]:
                start, end = edge[0], edge[1]
            else:
                start, end = edge[1], edge[0]
            g[start].append((start,end))
            g[end].append((start,end))

        # for loop
        # find out maximum number of edges in set union
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, len(set(g[i]) | set(g[j])))
        
        return ans
        
        
####################
# original version #

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        # count the number of edges linked to each nodes
        
        dic = collections.defaultdict(int)
        for s, e in roads:
            dic[s] += 1
            dic[e] += 1
        
        # sort dict by value
        dic2 = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}
            
        # find out two nodes which have most nodes linked
        stk = []
        s = set()
        for k, v in dic2.items():
            stk.append(k)
            s.add(v)
            if len(s) > 2:
                break
                
        # count their sum and check if they are linked or not
        ans = 0
        for i in range(len(stk)):
            for j in range(i + 1, len(stk)):
                if [stk[i], stk[j]] in roads or [stk[j], stk[i]] in roads:
                    cur = dic2[stk[i]] + dic2[stk[j]] - 1
                else:
                    cur = dic2[stk[i]] + dic2[stk[j]]
                ans = max(ans, cur)
        
        return ans
