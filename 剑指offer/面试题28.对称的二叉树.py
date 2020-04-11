"""
    请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
    例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

        1
       / \
      2   2
     / \ / \
    3  4 4  3
    但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

        1
       / \
      2   2
       \   \
       3    3
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.recursive(root)

    @classmethod
    def recursive(cls, root: TreeNode) -> bool:

        def helper(left, right):
            if not left and not right:
                return True

            if not left or not right or left.val != right.val:
                return False

            return helper(left.left, right.right) and helper(left.right, right.left)

        return helper(root.left, root.right) if root else True
