"""
    给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
    本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

    示例:
        给定的有序链表： [-10, -3, 0, 5, 9],
        一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

              0
             / \
           -3   9
           /   /
         -10  5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        mid_node = self.find_mid_node(head)
        node = TreeNode(mid_node.val)
        if head == mid_node:
            return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid_node.next)
        return node

    @classmethod
    def find_mid_node(cls, node: ListNode) -> ListNode:
        fast_node = node
        slow_node = node
        prev_node = None

        while fast_node and fast_node.next:
            prev_node = slow_node
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        if prev_node:
            # 将链表从左侧断开
            prev_node.next = None

        return slow_node
