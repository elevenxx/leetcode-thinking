n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。

如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。

给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。

 

示例 1：

输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
输出：5
解释：一种移除 5 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。

示例 2：

输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
输出：3
解释：一种移除 3 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,0] 同行。
2. 移除石头 [2,0] ，因为它和 [0,0] 同列。
3. 移除石头 [0,2] ，因为它和 [0,0] 同行。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # 将二维平面抽象成图，石子抽象成节点。石子同行或同列关系看作边。只需要统计整张图中有多少个连通分量。总节点数减去连通块的数量，即为可以删除的点的数量

        # 参考 https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/solution/yi-chu-zui-duo-de-tong-xing-huo-tong-lie-m50r/

        # 建图
        n = len(stones)
        edge = collections.defaultdict(list)
        for i, (x1, y1) in enumerate(stones):
            for j, (x2, y2) in enumerate(stones):
                if x1 == x2 or y1 == y2:
                    edge[i].append(j)
        
        # DFS 找连通分量
        def dfs(x: int):
            visited.add(x)
            for y in edge[x]:
                if y not in visited:
                    dfs(y)
        
        # 计算连通分量个数
        visited = set()
        num = 0
        for i in range(n):
            if i not in visited:
                num += 1
                dfs(i)
        
        return n - num

"""
方法一维护的是石子，这里直接维护石子所在的行和列.
实际操作：将每个石子的行和列进行合并。理解为每个点不是和其它点进行连接，而是连接到自己所在的行和列上。
并查集。代码中以哈希表为底层数据结构实现父亲数组 f，最后哈希表中所有的键均为出现过的行和列，计算有多少行和列的父亲就是自己，即为连通块的数量。
参考：https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/solution/yi-chu-zui-duo-de-tong-xing-huo-tong-lie-m50r/
"""
class DisjointSetUnion:
    def __init__(self):
        self.f = dict()
        self.rank = dict()
    
    def find(self, x: int) -> int:
        if x not in self.f:
            self.f[x] = x
            self.rank[x] = 1
            return x
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x: int, y: int):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx # 将 y 接到 x 所在的图上
    
    def numberOfConnectedComponent(self) -> int:
        return sum(1 for x, fa in self.f.items() if x == fa)


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = DisjointSetUnion()
        for x, y in stones:
            dsu.unionSet(x, y + 10001) # 分开行和列
        return len(stones) - dsu.numberOfConnectedComponent()

