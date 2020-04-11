"""
    输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
    示例1：
        输入：1->2->4, 1->3->4
        输出：1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        root = res
        while l1 and l2:
            if l1.val > l2.val:
                root.next = l2
                l2 = l2.next
            else:
                root.next = l1
                l1 = l1.next
            root = root.next
        if l1:
            root.next = l1
        if l2:
            root.next = l2

        return res.next
