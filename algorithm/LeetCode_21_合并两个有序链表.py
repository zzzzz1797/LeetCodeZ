"""
    将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

    示例：
        输入：1->2->4, 1->3->4
        输出：1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.use_iteration(l1, l2)

    @classmethod
    def use_recursive(cls, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1 > l2:
            l1.next = cls.use_recursive(l1.next, l2)
            return l1
        else:
            l2.next = cls.use_recursive(l1, l2.next)
            return l2

    @classmethod
    def use_iteration(cls, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(-1)
        prev = root
        while l1 and l2:
            if l1.val > l2.val:
                prev.next = l2
                l2 = l2.next
            else:
                prev.next = l1
                l1 = l1.next
            prev = prev.next

        prev.next = l1 or l2
        return root
