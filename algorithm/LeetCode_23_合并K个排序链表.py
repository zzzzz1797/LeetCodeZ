"""
    合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
    示例:
        输入:
        [
          1->4->5,
          1->3->4,
          2->6
        ]
        输出: 1->1->2->3->4->4->5->6
"""
from queue import PriorityQueue
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.solve_3(lists)

    @classmethod
    def solve_1(cls, lists: List[ListNode]) -> ListNode:
        res = None
        if size := len(lists):
            res = lists[0]
            for i in range(1, size):
                res = cls.merge(res, lists[i])
        return res

    @classmethod
    def solve_2(cls, lists: List[ListNode]) -> ListNode:
        root = curr = ListNode(0)
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))

        while not q.empty():
            val, node = q.get()
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next
            if node:
                q.put((node.val, node))
        return root.next

    @classmethod
    def solve_3(cls, lists: List[ListNode]) -> ListNode:
        size = len(lists)
        interval = 1
        while interval < size:
            for i in range(0, size - interval, interval * 2):
                lists[i] = cls.merge(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if size > 0 else None

    @classmethod
    def merge(cls, node1: ListNode, node2: ListNode) -> ListNode:
        root = curr = ListNode(0)

        while node1 and node2:
            if node1.val > node2.val:
                curr.next = ListNode(node2.val)
                node2 = node2.next
            else:
                curr.next = ListNode(node1.val)
                node1 = node1.next
            curr = curr.next

        if node1:
            curr.next = node1
        if node2:
            curr.next = node2

        return root.next
