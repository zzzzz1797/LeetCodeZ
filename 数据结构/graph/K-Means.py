class UnionSet:
    """
        并查集
    """

    def __init__(self):
        self._exist_map = {}
        self._father_map = {}
        self._size_map = {}

    def init_set(self, nodes):
        """
            初始化并查集
        """
        self._exist_map.clear()
        self._father_map.clear()
        self._size_map.clear()

        for node in nodes:
            self._size_map[node] = 1
            self._father_map[node] = node
            self._exist_map[node] = True

    def is_same_set(self, node_a, node_b):
        return self._is_exist(node_a) and self._is_exist(node_b) and self._find_father(node_a) == self._find_father(
            node_b)

    def union(self, node_a, node_b):
        if not (self._is_exist(node_a) and self._is_exist(node_b)):
            return

        father_a = self._find_father(node_a)
        father_b = self._find_father(node_b)

        if father_a != father_b:
            size_a = self._size_map[father_a]
            size_b = self._size_map[father_b]

            if size_a > size_b:
                large_node, small_node = father_a, father_b
            else:
                large_node, small_node = father_b, father_a

            self._father_map[small_node] = large_node
            self._size_map[large_node] = size_b + size_a
            del self._size_map[small_node]

    def size(self):
        return len(self._size_map)

    def _is_exist(self, node):
        return node in self._exist_map

    def _find_father(self, node_a):
        stack = []
        # 找到顶层节点
        while node_a != self._father_map[node_a]:
            stack.append(node_a)
            node_a = self._father_map[node_a]

        # 路径压缩
        while stack:
            self._father_map[stack.pop()] = node_a

        return node_a


if __name__ == "__main__":
    union_set = UnionSet()
    sets = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    union_set.init_set(sets)

    print(union_set.size())
    union_set.union('a', 'b')
    union_set.union('c', 'd')
    union_set.union('b', 'd')
    print(union_set.size())
