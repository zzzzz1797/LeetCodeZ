"""
    给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
    说明:
        树的深度不会超过 1000。
        树的节点总数不会超过 5000。
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        res = []
        if root:
            # return self.BFS(root)
            res = []
            self.DFS(root, res, 0)
        return res

    @classmethod
    def BFS(cls, root: Node):
        res = []
        queue = [root]

        while queue:
            new_queue = []
            tmp_res = []
            for node in queue:
                if node:
                    tmp_res.append(node.val)
                    new_queue += node.children
            queue = new_queue
            res.append(tmp_res)
        return res

    @classmethod
    def DFS(cls, root: Node, res: List[List[int]], level: int):
        if len(res) == level:
            res.append([])
        res[level].append(root.val)

        for node in root.children:
            cls.DFS(node, res, level + 1)
