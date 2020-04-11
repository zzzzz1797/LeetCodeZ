"""
    输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
    B是A的子结构， 即 A中有出现和B相同的结构和节点值。
    例如:
        给定的树 A:

             3
            / \
           4   5
          / \
         1   2
        给定的树 B：

           4 
          /
         1
    返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

    示例 1：
        输入：A = [1,2,3], B = [3,1]
        输出：false
    示例 2：
        输入：A = [3,4,5,1,2], B = [4,1]
        输出：true
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        return self.recursive(A, B)

    @classmethod
    def recursive(cls, A: TreeNode, B: TreeNode) -> bool:

        def helper(tree1, tree2):
            # 递归的终止条件
            if not tree2:
                return True
            if not tree1 or tree1.val != tree2.val:
                return False
            # 下探
            return helper(tree1.left, tree2.left) and helper(tree1.right, tree2.right)

        return bool(A and B) and (helper(A, B) or cls.recursive(A.left, B) or cls.recursive(A.right, B))
