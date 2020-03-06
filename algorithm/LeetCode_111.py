"""
    给定一个二叉树，找出其最小深度。
    最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
    说明: 叶子节点是指没有子节点的节点。
    示例:
        给定二叉树 [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        返回它的最小深度  2.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.recursive(root)

    @classmethod
    def recursive(cls, root: TreeNode) -> int:

        # terminator
        if not root:
            return 0

        # code logic '
        # (1) 左右节点都为空 返回1
        if not root.left and not root.right:
            return 1

        # drill down
        left_depth = cls.recursive(root.left)
        right_depth = cls.recursive(root.right)

        # （2）左右节点其中一个为空，则肯定有一个返回了0 所以返回两者之和+1
        if root.left is None or root.right is None:
            return left_depth + right_depth + 1
        # (3) 左右节点都为空 则取较小的值+1
        return min(left_depth, right_depth) + 1
