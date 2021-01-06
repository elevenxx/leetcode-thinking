"""
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。

另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。

 

注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

 

示例 1：

输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-division
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # 参考 https://leetcode-cn.com/problems/evaluate-division/solution/tu-lun-wen-ti-floydsuan-fa-by-jun-heng-jpxo/

        # 转化为带权图问题
        # a/b = 2, b/c = 3, a/c = 6
        # 抽象为 a 到 b 的权重为2，b 到 c 的权重为3，a 到 c 的权重为 2*3 = 6

        from collections import defaultdict
        graph = defaultdict(int) # 带权图，字典存储，键为顶点对，值为权重
        set1 = set() # 存放图的顶点

        for i in range(len(equations)):
            a, b = equations[i]
            graph[(a, b)] = values[i] 
            graph[(b, a)] = 1 / values[i] # 反方向取倒数
            
            # 存放出现的顶点
            set1.add(a)
            set1.add(b)
        
        
        # Floyd 算法，求图中任意两个顶点距离
        arr = list(set1) 
        for k in arr:
            for i in arr:
                for j in arr:
                    if graph[(i, k)] and graph[(k, j)]: # 两条边都在字典中，生成新的键值对，方便下一步查找操作
                        graph[(i, j)] = graph[(i, k)] * graph[(k, j)]
        
        res = [] # 结果集合
        for x, y in queries:
            if graph[(x, y)]: # 直接查找，若存在返回即可，不存在返回-1
                res.append(graph[x, y])
            else:
                res.append(-1)
        return res
