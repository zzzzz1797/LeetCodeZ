"""
    二叉树上有 n 个节点，按从 0 到 n - 1 编号，其中节点 i 的两个子节点分别是 leftChild[i] 和 rightChild[i]。
    只有 所有 节点能够形成且 只 形成 一颗 有效的二叉树时，返回 true；否则返回 false。

    如果节点 i 没有左子节点，那么 leftChild[i] 就等于 -1。右子节点也符合该规则。
    注意：节点没有值，本问题中仅仅使用节点编号。
"""

from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        return self.solve_1(n, leftChild, rightChild)

    @classmethod
    def solve_1(cls, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        dis_join_set = DisJoinSet(n)
        for i in range(n):
            if leftChild[i] != -1:
                if dis_join_set.find(leftChild[i]) != leftChild[i] or dis_join_set.is_connected(i, leftChild[i]):
                    return False
                dis_join_set.union(i, leftChild[i])

            if rightChild[i] != -1:
                if dis_join_set.find(rightChild[i]) != rightChild[i] or dis_join_set.is_connected(i, rightChild[i]):
                    return False
                dis_join_set.union(i, rightChild[i])

        return dis_join_set.size == 1


class DisJoinSet:

    def __init__(self, num: int):
        self.size = num
        self.parents = [i for i in range(num)]

    def find(self, target: int):
        root = target
        parent = self.parents
        while root != parent[root]:
            root = parent[root]

        # 路径压缩
        while parent[target] != target:
            tmp = target
            target = parent[target]
            parent[tmp] = root
        return root

    def union(self, target1, target2):
        parent1 = self.find(target1)
        parent2 = self.find(target2)
        if parent1 != parent2:
            self.parents[parent1] = parent2
            self.size -= 1

    def is_connected(self, target1, target2):
        return self.find(target1) == self.find(target2)
