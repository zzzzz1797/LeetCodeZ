"""
    给定一个二叉树，检查它是否是镜像对称的。
    例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
        1
       / \
      2   2
       \   \
       3    3
 
    进阶：
        你可以运用递归和迭代两种方法解决这个问题吗？
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        pass

    @classmethod
    def recursive(cls, root: TreeNode) -> bool:
        def helper(node1: TreeNode, node2: TreeNode):
            if node1 is None and node2 is None:
                return True

            if node1 is None or node2 is None:
                return False

            return node1.val == node2.val and helper(node1.left, node2.right) and helper(node1.right, node2.left)

        return helper(root.left, root.right) if root else True

    @classmethod
    def iteration(cls, root: TreeNode) -> bool:
        if root:
            stack = [root.left, root.right]
            while stack:
                right_node = stack.pop()
                left_node = stack.pop()

                if right_node is None and left_node is None:
                    continue
                if right_node is None or left_node is None:
                    return False
                if right_node.val != left_node.val:
                    return False

                stack.append(right_node.left)
                stack.append(left_node.right)
                stack.append(right_node.right)
                stack.append(left_node.left)

        return True
