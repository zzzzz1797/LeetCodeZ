"""
    给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
    示例：
        给定一个链表: 1->2->3->4->5, 和 n = 2.
        当删除了倒数第二个节点后，链表变为 1->2->3->5.
    说明：
        给定的 n 保证是有效的。
    进阶：
        你能尝试使用一趟扫描实现吗？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        return self.solve_1(head, n)

    @classmethod
    def solve_1(cls, head: ListNode, n: int) -> ListNode:
        """
            先定一个一个哑节点，可以处理好边界情况。
            快慢指针
            快指针先走n次，然后快慢一起走，快指针走完，慢指针就到了应该删除节点的前一个

        """
        dummy_node = ListNode(-1)
        dummy_node.next = head
        fast_node = dummy_node
        slow_node = dummy_node

        while n + 1:
            fast_node = fast_node.next
            n -= 1

        while fast_node:
            fast_node = fast_node.next
            slow_node = slow_node.next

        slow_node.next = slow_node.next.next
        return dummy_node.next


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    print(Solution().solve_1(a, 2))
