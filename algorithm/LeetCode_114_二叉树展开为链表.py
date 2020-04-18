"""
    给定一个二叉树，原地将它展开为链表。
    例如，给定二叉树

        1
       / \
      2   5
     / \   \
    3   4   6
    将其展开为：
    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pass

    @classmethod
    def solve_1(cls, root: TreeNode) -> None:
        """前序遍历"""
        queue = []

        def helper(node):
            if node:
                queue.append(node.val)
                helper(node.left)
                helper(node.right)

        helper(root)
        head = queue.pop(0)
        head.left = None
        while queue:
            tmp = queue.pop(0)
            tmp.left = None
            head.right = tmp
            head = tmp

    @classmethod
    def solve_2(cls, root: TreeNode) -> None:

        prev = None

        def helper(node):
            if node:
                nonlocal prev
                helper(node.right)
                helper(node.left)
                node.left = None
                node.right = prev
                prev = node

        helper(root)
