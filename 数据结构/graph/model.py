class Node:
    def __init__(self, value, in_degree=0, out_degree=0, next_nodes=None, edges=None):
        self.value = value
        self.in_degree = in_degree  # 入度为0
        self.out_degree = out_degree  # 出度为0
        self.next_nodes = next_nodes or []
        self.edges = edges or []

    def add_edge(self, to_node, weight=1):
        edge = Edge(weight, self, to_node)
        self.next_nodes.append(to_node)
        self.out_degree += 1
        to_node.in_degree += 1
        self.edges.append(edge)

    def __str__(self):
        return str(self.value)

    __repr__ = __str__


class Edge:
    def __init__(self, weight, from_node, to_node):
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node


class Graph:
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or {}
        self.edges = edges or set()

    def add_node(self, value):
        node = Node(value)
        self.nodes[value] = node
        return node


def topological_sort(graph: Graph):
    in_map = {}
    queue = []
    result = []

    for node in graph.nodes.values():
        node: Node = node
        in_map[node] = node.in_degree
        if node.in_degree == 0:
            queue.append(node)

    while queue:
        node = queue.pop(0)
        result.append(node)

        for next_node in node.next_nodes:
            in_map[next_node] = in_map[next_node] - 1
            if in_map[next_node] == 0:
                queue.append(next_node)

    print(result)


if __name__ == "__main__":
    g = Graph()

    node_a = g.add_node('a')
    node_b = g.add_node('b')
    node_c = g.add_node('c')
    node_a.add_edge(node_b)
    node_a.add_edge(node_c)
    node_b.add_edge(node_c)

    node_d = g.add_node('d')
    node_c.add_edge(node_d)

    node_e = g.add_node("e")
    node_f = g.add_node("f")
    node_g = g.add_node("g")
    node_d.add_edge(node_e)
    node_d.add_edge(node_f)

    node_e.add_edge(node_g)
    node_f.add_edge(node_g)

    topological_sort(g)
