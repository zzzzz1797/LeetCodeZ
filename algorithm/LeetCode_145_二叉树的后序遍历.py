"""
    给定一个二叉树，返回它的 后序 遍历。

    示例:
        输入: [1,null,2,3]
           1
            \
             2
            /
           3

        输出: [3,2,1]
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
            左右根
        """
        pass

    @classmethod
    def iteration(cls, root: TreeNode) -> List[int]:

        """
            根右左
            然后反转

        """
        res = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res[::-1]

    @classmethod
    def recursive(cls, root: TreeNode) -> List[int]:
        res = []

        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)
                res.append(node.val)

        helper(root)
        return res
