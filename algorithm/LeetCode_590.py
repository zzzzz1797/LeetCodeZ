"""
    给定一个 N 叉树，返回其节点值的后序遍历。
    说明: 递归法很简单，你可以使用迭代法完成此题吗?
"""

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> List[int]:
        res = []
        if root:
            self.iteration(root, res)

        return res

    @classmethod
    def recursive(cls, root: Node, res: List[int]):
        """
            左右根
        """
        if root:
            for node in root.children:
                cls.recursive(node, res)
            res.append(root.val)

    @classmethod
    def iteration(cls, root: Node, res: List[int]):
        """
            先根右左 输出 然后反转  
        """
        stack = [root]

        while stack:
            node = stack.pop()
            if node is not None:
                res.append(node.val)
            for child in node.children:
                stack.append(child)
        res.reverse()
