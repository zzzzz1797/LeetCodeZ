"""
    在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

    示例 1:
        输入: 4->2->1->3
        输出: 1->2->3->4
    示例 2:
        输入: -1->5->3->4->0
        输出: -1->0->3->4->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.merge_sort(head)

    @classmethod
    def merge_sort(cls, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow_node = head
        fast_node = head.next

        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        mid_node = slow_node.next
        slow_node.next = None

        left = cls.merge_sort(head)
        right = cls.merge_sort(mid_node)

        tmp_node = dummy_node = ListNode(-1)

        while left and right:
            if left.val > right.val:
                tmp_node.next = right
                right = right.next
            else:
                tmp_node.next = left
                left = left.next
            tmp_node = tmp_node.next
        tmp_node.next = left or right
        return dummy_node.next
