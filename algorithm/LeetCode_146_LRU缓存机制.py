"""
    运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
    它应该支持以下操作： 获取数据 get 和 写入数据 put 。
    获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
    写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
    当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

    进阶:
        你是否可以在 O(1) 时间复杂度内完成这两种操作？

    示例:
        LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

        cache.put(1, 1);
        cache.put(2, 2);
        cache.get(1);       // 返回  1
        cache.put(3, 3);    // 该操作会使得密钥 2 作废
        cache.get(2);       // 返回 -1 (未找到)
        cache.put(4, 4);    // 该操作会使得密钥 1 作废
        cache.get(1);       // 返回 -1 (未找到)
        cache.get(3);       // 返回  3
        cache.get(4);       // 返回  4
"""


class DoubleLinkNode:
    def __init__(self, key: int = None, value: int = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # 实际用量
        self.size = 0
        # 头节点（哑节点）
        self.head = DoubleLinkNode()
        # 尾节点（哑节点）
        self.tail = DoubleLinkNode()
        # 字典 存储key和node之间的映射关系
        self.mapping = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.mapping.get(key)

        if not node:
            return -1

        # 1.删除node
        self.remove_node(node)
        # 2.将node插入到头部
        self.add_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.mapping.get(key)

        if not node:
            # 说明是一个新的key
            node = DoubleLinkNode(key, value)
            self.mapping[key] = node
            self.add_to_head(node)

            # 更新实际用量
            self.size += 1

            # 判断是否需要更新整个链表
            if self.size > self.capacity:
                # 弹出做后一个节点
                tail_node = self.pop_tail()
                # 清空mapping
                del self.mapping[tail_node.key]
                self.size -= 1
        else:
            # 更新节点信息
            node.value = value
            self.remove_node(node)
            self.add_to_head(node)

    @classmethod
    def remove_node(cls, node: DoubleLinkNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_head(self, node: DoubleLinkNode):
        # 取出真正的头节点
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def pop_tail(self) -> DoubleLinkNode:
        prev_node = self.tail.prev
        self.remove_node(prev_node)
        return prev_node
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
