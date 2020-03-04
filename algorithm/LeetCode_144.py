"""
    给定一个二叉树，返回它的 前序 遍历。
    进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
            根左右
        """
        res = []
        if root:
            self.iteration(root, res)
        return res

    @classmethod
    def recursive(cls, root: TreeNode, res: List[int]):
        if root:
            res.append(root.val)
            if root.left:
                cls.recursive(root.left, res)
            if root.right:
                cls.recursive(root.right, res)

    @classmethod
    def iteration(cls, root: TreeNode, res: List[int]):
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)

                stack.append(node.right)

                stack.append(node.left)
