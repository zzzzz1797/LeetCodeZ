"""
    给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
    示例:
        输入: [1,2,3,null,5,null,4]
        输出: [1, 3, 4]
        解释:

           1            <---
         /   \
        2     3         <---
         \     \
          5     4       <---
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        pass

    @classmethod
    def dfs(cls, root: TreeNode) -> List:
        tmp_res = []

        def helper(level, node):
            if not node:
                return
            if level == len(tmp_res):
                tmp_res.append([])
            tmp_res[level].append(node.val)
            if node.left:
                helper(level + 1, node.left)
            if node.right:
                helper(level + 1, node.right)

        helper(0, root)
        return [i[-1] for i in tmp_res]

    @classmethod
    def bfs(cls, root: TreeNode) -> List[int]:
        res = []
        if root:
            queue = [root]

            while queue:
                tmp_queue = []
                tmp_val = []
                for node in queue:
                    tmp_val.append(node.val)
                    if node.left:
                        tmp_queue.append(node.left)
                    if node.right:
                        tmp_queue.append(node.right)

                if tmp_val:
                    res.append(tmp_val[-1])
                queue = tmp_queue
        return res
