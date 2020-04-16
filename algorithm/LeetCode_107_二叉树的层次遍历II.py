"""
    给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
    例如：
        给定二叉树 [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    返回其自底向上的层次遍历为：
        [
          [15,7],
          [9,20],
          [3]
        ]
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        return self.bfs(root)

    @classmethod
    def bfs(cls, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = [root]
        while queue:
            tmp_queue = []
            res.append([])
            for node in queue:
                res[-1].append(node.val)
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            queue = tmp_queue
        return cls.reversed(res)

    @classmethod
    def dfs(cls, root: TreeNode) -> List[List[int]]:
        res = []

        def helper(level, node):
            if len(res) == level:
                res.append([])
            res[level].append(node.val)

            if node.left:
                helper(level + 1, node.left)
            if node.right:
                helper(level + 1, node.right)

        if root:
            helper(0, root)
        return cls.reversed(res)

    @classmethod
    def reversed(cls, params):
        if params:
            start = 0
            end = len(params) - 1
            while start < end:
                params[start], params[end] = params[end], params[start]
                start += 1
                end -= 1
        return params
