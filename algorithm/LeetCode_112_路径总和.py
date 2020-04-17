"""
    给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
    说明: 叶子节点是指没有子节点的节点。

    示例: 
        给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
        返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        pass

    @classmethod
    def recursive(cls, root: TreeNode, target: int) -> bool:
        def helper(node: TreeNode, tmp_res: int) -> bool:
            if not node:
                return False
            check_target = node.val + tmp_res
            if check_target == target and (node.left is None and node.right is None):
                return True

            if node.left and helper(node.left, check_target):
                return True
            if node.right and helper(node.right, check_target):
                return True
            return False

        return helper(root, 0)
