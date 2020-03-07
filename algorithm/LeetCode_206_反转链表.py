"""
    反转一个单链表。
    示例:
        输入: 1->2->3->4->5->NULL
        输出: 5->4->3->2->1->NULL
    进阶:
        你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

    https://leetcode-cn.com/problems/reverse-linked-list
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        curr = head
        prev = None

        while curr:
            tmp_node = curr.next
            curr.next = prev

            curr, prev = tmp_node, curr
        return prev

    def recursive(self, head):
        if head is None or head.next is None:
            return head

        new_node = self.recursive(head.next)
        head.next.next = head
        head.next = None
        return new_node
