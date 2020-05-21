# 编写一个程序，找到两个单链表相交的起始节点。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pass

    @classmethod
    def solve_1(cls, headA: ListNode, headB: ListNode) -> ListNode:
        tmp_node_a = headA
        tmp_node_b = headB

        while tmp_node_a != tmp_node_b:
            tmp_node_a = tmp_node_a.next if tmp_node_a else headB
            tmp_node_b = tmp_node_b.next if tmp_node_b else headA
        return tmp_node_b


if __name__ == '__main__':
    A = ListNode(2)
    A.next = ListNode(6)
    A.next.next = ListNode(4)

    B = ListNode(1)
    B.next = ListNode(5)

    print(Solution.solve_1(A, B))
