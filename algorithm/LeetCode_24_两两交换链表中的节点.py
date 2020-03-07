"""

    给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

    示例:
        给定 1->2->3->4, 你应该返回 2->1->4->3.

    https://leetcode-cn.com/problems/swap-nodes-in-pairs
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return self.user_iteration(head)

    @classmethod
    def recursive(cls, head: ListNode) -> ListNode:
        # 递归的终止条件
        if not head or not head.next:
            return head

        # 获取节点内容
        first = head
        second = head.next

        # 交换节点
        first.next = cls.recursive(second.next)
        second.next = first
        return second

    @classmethod
    def user_iteration(cls, head: ListNode) -> ListNode:
        res = ListNode(-1)
        res.next = head

        prev = res

        while head and head.next:
            first = head
            second = head.next

            prev.next = first
            first.next = second.next
            second.next = first

            head = first.next
            prev = first
        return res.next
