"""

    给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

    例如:
        给定二叉树: [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        返回其层次遍历结果：
            [
              [3],
              [9,20],
              [15,7]
            ]
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.dfs(root)

    @classmethod
    def bfs(cls, root: TreeNode) -> List[List[int]]:
        """
            广度优先遍历
            时间复杂度：O(n)
            空间复杂度：O(n)

        """
        res = []
        queue = [root]
        while queue:
            node_list = []
            val_list = []

            for node in queue:
                # 如果node存在肯定会有左右节点和值
                if node:
                    val_list.append(node.val)
                    node_list.append(node.left)
                    node_list.append(node.right)

            # 防止添加一个空的列表进去
            if val_list:
                res.append(val_list)
            queue = node_list
        return res

    @classmethod
    def dfs(cls, root: TreeNode) -> List[List[int]]:
        """
            深度优先遍历
            时间复杂度：O(n)
            空间复杂度：O(n)

            思路：
                1）从root节点开始往下走，走到底再回溯
                2）单独用一个变量表示走到第几层了，
                3）用这个变量找出val应该存放的下标数组在哪儿
        """

        def helper(node: TreeNode, res: List[List[int]], level: int):
            # terminator
            if level == len(res):
                # 这里表示需要新增一个数组， 当level表示的层级 也代笔res的下标，下面代表在res.append之前 level和res的值
                # 0 []
                # 1 [[3]]
                # 2 [[3], [9, 20]]

                res.append([])
            # process
            res[level].append(node.val)
            # drill down
            if node.left:
                helper(node.left, res, level + 1)
            if node.right:
                helper(node.right, res, level + 1)

        ret = []
        helper(root, ret, 0)
        return ret
