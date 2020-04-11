"""
    请完成一个函数，输入一个二叉树，该函数输出它的镜像。
    例如输入：

         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    镜像输出：
         4
       /   \
      7     2
     / \   / \
    9   6 3   1
    示例 1：
        输入：root = [4,2,7,1,3,6,9]
        输出：[4,7,2,9,6,3,1]
 

    限制：
        0 <= 节点个数 <= 1000
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        return self.recursive(root)

    @classmethod
    def recursive(cls, root: TreeNode) -> TreeNode:
        # 递归的终止条件
        if not root:
            return None
        node = root.left
        root.left = cls.recursive(root.right)
        root.right = cls.recursive(node)
        return root
