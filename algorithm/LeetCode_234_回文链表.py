"""
    请判断一个链表是否为回文链表。

    示例 1:
        输入: 1->2
        输出: false

    示例 2:
        输入: 1->2->2->1
        输出: true

    进阶：
        你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pass

    @classmethod
    def solve_1(cls, head: ListNode) -> bool:
        """
            快慢指针
        """
        fast_node = head
        slow_node = head
        check_node = head

        while fast_node and fast_node.next and slow_node and slow_node.next:
            fast_node = fast_node.next.next
            slow_node = slow_node.next

        # 如果是偶数 把slow_node算上比         # 如果是奇数 过滤slow_node
        return cls.compare_node(check_node, slow_node) or cls.compare_node(check_node, slow_node.next)

    @classmethod
    def compare_node(cls, node1, node2):
        node2 = cls.reverse_node(node2)

        if node1 and not node2:
            return False
        while node2:
            if node2.val == node1.val:
                node2 = node2.next
                node1 = node1.next
            else:
                return False
        return True

    @classmethod
    def reverse_node(cls, node):
        if not node or not node.next:
            return node
        prev = None
        root = node

        while root:
            next_node = root.next
            root.next = prev
            prev = root
            root = next_node
        return prev


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(2)
    a.next.next.next = ListNode(1)

    print(Solution.solve_1(a))
