"""
    给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的数值。

    注意：
        给定的目标值 target 是一个浮点数
        题目保证在该二叉搜索树中只会存在一个最接近目标值的数

    示例：
        输入: root = [4,2,5,1,3]，目标值 target = 3.714286
                4
               / \
              2   5
             / \
            1   3
        输出: 4
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        return self.solve_1(root, target)

    @classmethod
    def solve_1(cls, root: TreeNode, target: float) -> int:
        closest_val = root.val
        while root:
            closest_val = min(closest_val, root.val, key=lambda i: abs(i - target))
            root = root.left if root.val < target else root.right
        return closest_val
