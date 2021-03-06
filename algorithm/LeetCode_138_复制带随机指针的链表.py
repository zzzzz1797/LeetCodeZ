"""
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
要求返回这个链表的 深拷贝。 
我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
"""
from collections import defaultdict


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        pass

    @classmethod
    def solve_1(cls, head: Node) -> Node:
        res = defaultdict(lambda: Node(0))
        res[None] = None
        curr_node = head

        while curr_node:
            res[curr_node].val = curr_node.val
            res[curr_node].next = res[curr_node.next]
            res[curr_node].random = res[curr_node.random]
            curr_node = curr_node.next
        return res[head]

    @classmethod
    def solve_2(cls, head: None) -> Node:
        visited = {}

        def helper(node):
            if not node:
                return
            if node in visited:
                return visited[node]
            cloned_node = Node(node.val)
            visited[node] = cloned_node
            cloned_node.next = helper(node.next)
            cloned_node.random = helper(node.random)
            return cloned_node

        return helper(head)
