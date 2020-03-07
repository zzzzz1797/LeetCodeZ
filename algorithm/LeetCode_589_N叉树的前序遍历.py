"""
    给定一个 N 叉树，返回其节点值的前序遍历。
    说明: 递归法很简单，你可以使用迭代法完成此题吗?

"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        """前序遍历 根左右"""
        res = []
        if root:
            # self.recursive(root, res)
            self.use_stack(root, res)

        return res

    @classmethod
    def use_stack(cls, root: Node, res: List[int]) -> None:
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack += node.children[::-1]

    @classmethod
    def recursive(cls, root: Node, res: List[int]) -> None:
        # terminator
        if root:
            res.append(root.val)
            for node in root.children:
                cls.recursive(node, res)
