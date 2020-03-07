"""
    给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
    k 是一个正整数，它的值小于或等于链表的长度。
    如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

    示例 :
        给定这个链表：1->2->3->4->5
        当 k = 2 时，应当返回: 2->1->4->3->5
        当 k = 3 时，应当返回: 3->2->1->4->5
    说明 :
        你的算法只能使用常数的额外空间。
        你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
    https://leetcode-cn.com/problems/reverse-nodes-in-k-group
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return self.reversed_n_link(head, k)

    @classmethod
    def recursive(cls, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = cls.recursive(cur, k)
            while count:
                tmp = head.next
                head.next = cur
                cur, head = head, tmp
                count -= 1
            head = cur
        return head

    @classmethod
    def use_stack(cls, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        p = dummy

        while True:
            count = k
            stack = []
            tmp = head

            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1

            if count:
                # 说明元素不足count个了
                p.next = head
                break

            # 反转操作
            while stack:
                p.next = stack.pop()
                p = p.next

            p.next = tmp
            head = tmp
        return dummy.next

    @classmethod
    def reversed_n_link(cls, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        dummy_node = ListNode(-1)
        dummy_node.next = head

        pre_node = dummy_node
        end_node = dummy_node

        while end_node.next is not None:
            count = k

            while count and end_node:
                count -= 1
                end_node = end_node.next

            if not end_node:
                break

            start_node = pre_node.next
            next_node = end_node.next

            end_node.next = None
            pre_node.next = cls.reversed_link(start_node)

            start_node.next = next_node

            pre_node = start_node
            end_node = start_node
        return dummy_node.next

    @classmethod
    def reversed_link(cls, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre

            cur, pre = tmp, cur
        return pre
