"""
    给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

    图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

    class Node {
        public int val;
        public List<Node> neighbors;
    }
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors or []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        pass

    @classmethod
    def dfs(cls, node: Node) -> Node:
        visited = {}

        def helper(n: Node):
            if not n:
                return n

            if n in visited:
                return visited[n]

            cloned_node = Node(n.val, [])
            visited[n] = cloned_node

            if n.neighbors:
                cloned_node.neighbors = [helper(i) for i in n.neighbors]
            return cloned_node

        return helper(node)
