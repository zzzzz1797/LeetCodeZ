"""
    给定一个二叉树
    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
    填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
    初始状态下，所有 next 指针都被设置为 NULL。
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        pass

    @classmethod
    def solve_1(cls, root: Node) -> Node:
        if not root:
            return root

        left_most = root

        while left_most:
            dummy_node = Node(0)
            tail_node = dummy_node

            while left_most:
                if left_most.left:
                    tail_node.next = left_most.left
                    tail_node = tail_node.next
                if left_most.right:
                    tail_node.next = left_most.right
                    tail_node = tail_node.next

                left_most = left_most.next
            left_most = dummy_node.next
        return root
