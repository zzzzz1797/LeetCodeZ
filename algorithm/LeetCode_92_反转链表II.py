"""
    反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

    说明:
        1 ≤ m ≤ n ≤ 链表长度。

    示例:
        输入: 1->2->3->4->5->NULL, m = 2, n = 4
        输出: 1->4->3->2->5->NULL
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
            1.找出开始反转节点的上一个节点
            2.从指定位置开始反转
            3.拼接到原来的链表
        """
        dummy_node = ListNode(-1)
        dummy_node.next = head

        prev_node = dummy_node

        for i in range(m - 1):
            prev_node = prev_node.next

        new_node = None
        curr_node = prev_node.next

        for i in range(n - m + 1):
            tmp_node = curr_node.next
            curr_node.next = new_node
            new_node = curr_node
            curr_node = tmp_node
        prev_node.next.next = curr_node
        prev_node.next = new_node
        return dummy_node.next


if __name__ == '__main__':
    node = ListNode(3)
    node.next = ListNode(5)

    print(Solution().reverseBetween(node, 1, 1))
