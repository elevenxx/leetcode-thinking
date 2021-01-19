# disjoint union set(DSU)
# 1. 判断node1, node2 是否相连，就是判断两者的 root 是否相同
# 2. 如果不相连，就把两者相连，把两者的 root 相连

#   1, 2, 3, 4 # node
# [ -1,2,-1,-1,-1] # 上面 node 的 root
class DSU:
    def __init__(self, node_number):
        # 把所有 node 初始化为没有连接的情况
        self.root_relation_list = [-1] * (node_number + 1)

    def root_node_find(self, node):
        # 给一个 node，找到直属的 node，依次往上找，直到 root，循环操作
        while self.root_relation_list[node] != -1:
            node = self.root_relation_list[node]
        return node

    def node_connected(self, node1, node2):
        node1_root = self.root_node_find(node1)
        node2_root = self.root_node_find(node2)

        if node1_root != node2_root:  # 不相连
            self.root_relation_list[node1_root] = node2_root  # 让它们相连，把 node1 连到 node2 上
        else:
            print("connected")
        return


dsu = DSU(4)  # 初始化4个节点
dsu.node_connected(1, 2)  # 把节点1和2相连，此时节点1的 root 是2
dsu.node_connected(1, 3)  # 把节点1和3相连，此时将节点1的 root 即节点2 连接到节点3
print(dsu.root_relation_list)  # 输出，看是否相连
dsu.node_connected(2, 3)  # 输出 connected，因为节点2和3已经相连了
