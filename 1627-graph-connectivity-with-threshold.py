class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n+1)]       
        
        # union-find set
        # find parent
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        # union together
        def union(x, y):
            u = find(x)
            v = find(y)
            if u == v:
                return True
            parent[v] = u
            return False
        
        # converse view
        # union together all numbers that have common factor 
        # and are bigger than threshold
        for i in range(threshold+1, n+1):
            for j in range(i*2, n+1, i):
                union(i, j)
        
        res = []
        # if u and v in the same union set, then there is at least
        # a path between u and v
        for u, v in queries:
            res.append(find(u) == find(v))
        return res
