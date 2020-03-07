"""
    翻转一棵二叉树。

    示例：

    输入：

         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    输出：

         4
       /   \
      7     2
     / \   / \
    9   6 3   1
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.iteration(root)

    @classmethod
    def recursive(cls, root: TreeNode) -> TreeNode:
        if root:
            left = cls.recursive(root.left)
            right = cls.recursive(root.right)

            root.left = right
            root.right = left

        return root

    @classmethod
    def iteration(cls, root: TreeNode) -> TreeNode:
        if root:
            queue = [root]
            while queue:
                node = queue.pop()
                if node:
                    node.left, node.right = node.right, node.left
                    queue.append(node.left) if node.left else ''
                    queue.append(node.right) if node.right else ''
        return root
