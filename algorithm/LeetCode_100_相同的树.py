"""
    给定两个二叉树，编写一个函数来检验它们是否相同。
    如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

    示例 1:
        输入:       1         1
                  / \       / \
                 2   3     2   3
                [1,2,3],   [1,2,3]
        输出: true

    示例 2:
        输入:      1          1
                  /           \
                 2             2
                [1,2],     [1,null,2]
        输出: false

    示例 3:
        输入:       1         1
                  / \       / \
                 2   1     1   2
                [1,2,1],   [1,1,2]
    输出: false
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        pass

    @classmethod
    def solve_1(cls, p: TreeNode, q: TreeNode) -> bool:
        def helper(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return helper(node1.left, node2.left) and helper(node2.left, node2.left)

        return helper(p, q)

    @classmethod
    def solve_2(cls, p: TreeNode, q: TreeNode) -> bool:
        def check(n1, n2) -> bool:
            if not n1 and not n2:
                return True

            if not n1 or not n2:
                return False

            if n1.val != n2.val:
                return False
            return True

        queue = [(p, q)]

        while queue:
            tmp_queue = []
            for tmp_p, tmp_q in queue:
                if not check(tmp_p, tmp_q):
                    return False
                if tmp_p or tmp_q:
                    tmp_queue.append((tmp_p.left if tmp_p else None, tmp_q.left if tmp_q else None))
                    tmp_queue.append((tmp_p.right if tmp_p else None, tmp_q.right if tmp_q else None))
            queue = tmp_queue
        return True
