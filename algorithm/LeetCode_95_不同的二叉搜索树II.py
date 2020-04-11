"""
    给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
    示例:
        输入: 3
        输出:
            [
              [1,null,3,2],
              [3,2,null,1],
              [3,1,null,null,2],
              [2,1,3],
              [1,null,2,null,3]
            ]
        解释:
        以上的输出对应以下 5 种不同结构的二叉搜索树：

           1         3     3      2      1
            \       /     /      / \      \
             3     2     1      1   3      2
            /     /       \                 \
           2     1         2                 3
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
            二叉搜索树
                1、根节点的值大于左子节点
                2、根节点的值小于右子节点
        """
        return self.recursive(n)

    @classmethod
    def recursive(cls, n: int) -> List[TreeNode]:
        def helper(left, right):
            if left > right:
                return [None, ]

            all_trees = []

            for i in range(left, right + 1):
                left_trees = helper(left, i - 1)
                right_trees = helper(i + 1, right)

                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            return all_trees

        return helper(1, n) if n else []
