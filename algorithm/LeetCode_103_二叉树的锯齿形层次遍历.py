"""
    给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

    例如：
        给定二叉树 [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    返回锯齿形层次遍历如下：
        [
          [3],
          [20,9],
          [15,7]
        ]
"""
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.dfs(root)

    @classmethod
    def dfs(cls, root: TreeNode) -> List[List[int]]:
        res = []

        def helper(level, node):
            if level == len(res):
                res.append(deque())
            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].appendleft(node.val)

            if node.left:
                helper(level + 1, node.left)
            if node.right:
                helper(level + 1, node.right)

        if root:
            helper(0, root)
        return res

    @classmethod
    def bfs(cls, root: TreeNode) -> List[List[int]]:
        res = []
        if root:
            queue = [root]
            level = 1
            while queue:
                tmp_queue = []

                res.append(deque([]))

                for node in queue:
                    if level % 2 == 0:
                        res[-1].appendleft(node.val)
                    else:
                        res[-1].append(node.val)

                    if node.left:
                        tmp_queue.append(node.left)
                    if node.right:
                        tmp_queue.append(node.right)
                res[-1] = list(res[-1])
                queue = tmp_queue
                level += 1
        return res
