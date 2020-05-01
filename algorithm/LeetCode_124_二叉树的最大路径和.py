"""
    给定一个非空二叉树，返回其最大路径和。
    本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

    示例 1:
        输入: [1,2,3]

               1
              / \
             2   3
        输出: 6
    示例 2:
        输入: [-10,9,20,null,null,15,7]

           -10
           / \
          9  20
            /  \
           15   7
        输出: 42
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return self.dfs(root)

    @classmethod
    def dfs(cls, root: TreeNode) -> int:
        res = float("-inf")

        def helper(node: TreeNode):
            # 递归终止条件
            if not node:
                return 0

            # 业务逻辑处理
            max_left = max(helper(node.left), 0)
            max_right = max(helper(node.right), 0)

            tmp_res = node.val + max_left + max_right
            nonlocal res
            res = max(res, tmp_res)

            # Drill down
            return node.val + max(max_left, max_right)

        helper(root)
        return res
