"""
    实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
    调用 next() 将返回二叉搜索树中的下一个最小的数。

    提示：
        next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
        你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    """二叉搜索树的中序列遍历是一个有序的序列"""

    def __init__(self, root: TreeNode):
        self.stack = []
        self._left_in_order(root)

    def hasNext(self) -> int:
        """
        @return the next smallest number
        """
        return len(self.stack) > 0

    def next(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        topmost_node = self.stack.pop()

        if topmost_node.right:
            self._left_in_order(topmost_node.right)
        return topmost_node.val

    def _left_in_order(self, root: TreeNode):
        while root:
            self.stack.append(root)
            root = root.left
