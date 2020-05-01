"""
    给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。
    s 也可以看做它自身的一棵子树。
    示例 1:
        给定的树 s:

             3
            / \
           4   5
          / \
         1   2
        给定的树 t：

           4
          / \
         1   2
        返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

    示例 2:
        给定的树 s：

             3
            / \
           4   5
          / \
         1   2
            /
           0
        给定的树 t：

           4
          / \
         1   2
        返回 false。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        pass

    @classmethod
    def recursive(cls, s: TreeNode, t: TreeNode) -> bool:
        def helper(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False
            return node1.val == node2.val and helper(node1.left, node2.left) and helper(node1.right, node2.right)

        if not t:
            return True

        if not s:
            return False

        return helper(s, t) or cls.recursive(s.left, t) or cls.recursive(s.right, t)
