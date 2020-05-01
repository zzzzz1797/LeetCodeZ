"""
    给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
    示例 :
        给定二叉树

                  1
                 / \
                2   3
               / \
              4   5
        返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
    注意：两结点之间的路径长度是以它们之间边的数目表示。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.recursive(root)

    @classmethod
    def recursive(cls, root: TreeNode) -> int:
        res = 1

        def helper(node: TreeNode):
            if not node:
                return 0

            max_left = helper(node.left)
            max_right = helper(node.right)

            nonlocal res
            res = max(res, max_left + max_right + 1)
            return max(max_left, max_right) + 1

        helper(root)
        return res - 1  # 走过的所有节点树 -1 就是最大直径
