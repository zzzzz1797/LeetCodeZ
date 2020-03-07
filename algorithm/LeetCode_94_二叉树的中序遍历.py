"""
    给定一个二叉树，返回它的中序 遍历。

    示例:

    输入: [1,null,2,3]
           1
            \
             2
            /
           3

    输出: [1,3,2]

    进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            self.recursive(root, res)
        return res

    @classmethod
    def use_stack(cls, root: TreeNode, res: List[int]):
        """
            手动维护一个
        """
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            curr = stack.pop()
            res.append(curr.val)
            root = curr.right
        return res

    @classmethod
    def recursive(cls, root: TreeNode, res: List[int]):
        """
            左根右
        """
        if root.left:
            cls.recursive(root.left, res)
        res.append(root.val)
        if root.right:
            cls.recursive(root.right, res)
