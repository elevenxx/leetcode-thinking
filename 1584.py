class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))

    def find(self, x: int) -> int:
        if self.f[x] == x:  # 直到找到根，根是本节点连到本节点
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False  # x & y 连通，属于两个集合

        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx

        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx
        return True


class Solution:
    def minCostConnectPoints(points) -> int:
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])  # 定义距离

        n = len(points)
        dsu = DisjointSetUnion(n)
        edges = list()

        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(i, j), i, j))

        edges.sort()  # 按照距离排序

        ans, num = 0, 1
        for length, x, y in edges:
            if dsu.unionSet(x, y):
                ans += length
                num += 1
                if num == n:  # 连接了所有点
                    break

        return ans


points = [[0,0],[2,2],[3,10],[5,2],[7,0]] # 20
points = [[3,12],[-2,5],[-4,1]] # 18
print(Solution.minCostConnectPoints(points))