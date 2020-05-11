"""
    给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

    注意：两个节点之间的路径长度由它们之间的边数表示。

    示例 1:
        输入:
                      5
                     / \
                    4   5
                   / \   \
                  1   1   5
        输出:   2
    示例 2:
        输入:

                      1
                     / \
                    4   5
                   / \   \
                  4   4   5
        输出: 2
    注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        pass

    @classmethod
    def recursive(cls, root) -> int:
        ret = 0

        def helper(node):
            if not node:
                return 0

            left_res = helper(node.left)
            right_res = helper(node.right)

            tmp_left_res = tmp_right_res = 0

            if node.left and node.left.val == node.val:
                tmp_left_res = left_res + 1
            if node.right and node.right.val == node.val:
                tmp_right_res = right_res + 1
            nonlocal ret
            ret = max(ret, tmp_left_res + tmp_right_res)

            return max(tmp_right_res, tmp_left_res)

        helper(root)
        return ret
