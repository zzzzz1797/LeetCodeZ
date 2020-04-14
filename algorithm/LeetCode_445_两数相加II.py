"""
    给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
    你可以假设除了数字 0 之外，这两个数字都不会以零开头。

    进阶：
        如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
    示例：
        输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
        输出：7 -> 8 -> 0 -> 7
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.solve_1(l1, l2)

    @classmethod
    def solve_0(cls, l1: ListNode, l2: ListNode) -> ListNode:
        """
            stack

        """

        stack1 = []
        stack2 = []
        root1 = l1
        root2 = l2

        while root1:
            stack1.append(root1.val)
            root1 = root1.next

        while root2:
            stack2.append(root2.val)
            root2 = root2.next

        res = None
        carry = 0
        while stack1 or stack2 or carry != 0:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            tmp = (val1 + val2 + carry)
            val = tmp % 10
            carry = tmp // 10
            curr = ListNode(val)
            curr.next = res
            res = curr
        return res

    @classmethod
    def solve_1(cls, l1: ListNode, l2: ListNode) -> ListNode:
        """
            思路：
                1、先反转链表
                2、两个链表相加
                3、再反转结果链表
        """
        dummy_node = ListNode(-1)
        reversed_l1 = cls.reverse_node(l1)
        reversed_l2 = cls.reverse_node(l2)
        carry = 0
        root = dummy_node

        while reversed_l1 or reversed_l2:
            val1 = reversed_l1.val if reversed_l1 else 0
            val2 = reversed_l2.val if reversed_l2 else 0

            val = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            root.next = ListNode(val)

            reversed_l1 = reversed_l1.next if reversed_l1 else None
            reversed_l2 = reversed_l2.next if reversed_l2 else None
            root = root.next

        if carry:
            root.next = ListNode(carry)
        return cls.reverse_node(dummy_node.next)

    @classmethod
    def reverse_node(cls, node: ListNode):
        prev = None
        curr = node

        while curr:
            tmp_node = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_node
        return prev
