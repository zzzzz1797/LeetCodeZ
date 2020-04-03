"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
    示例 1：

    输入：head = [1,3,2]
    输出：[2,3,1]
"""

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        pass

    @classmethod
    def iteration(cls, head: ListNode) -> List[int]:
        root = None
        curr = head

        while curr:
            tmp_node = curr.next
            curr.next = root
            root = curr
            curr = tmp_node
        res = []
        while root:
            res.append(root.val)
            root = root.next
        return res

    @classmethod
    def recursive(cls, head: ListNode) -> List[int]:
        def helper(node):
            if not node or not node.next:
                return node

            new_node = helper(node.next)
            node.next.next = node
            node.next = None
            return new_node

        reverse_node = helper(head)
        res = []
        while reverse_node:
            res.append(reverse_node.val)
            reverse_node = reverse_node.next
        return res
