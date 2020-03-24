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


class DLinkNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity  # 缓存的容量
        self.size = 0  # 缓存当前所用容量
        self.cache = {}  # 用来保存 节点信息
        self.head = DLinkNode()  # 头节点信息 只是一个哑节点 可以省略判断None的逻辑
        self.tail = DLinkNode()  # 尾节点信息 同上

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1

        self._move_to_head(node)  # 将这个节点移动到头节点去
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if not node:
            # 是一个新的节点
            node = DLinkNode(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            self.size += 1

            if self.size > self.capacity:
                # 弹出最后一个节点
                tail_node = self._pop_tail_node()
                self.size -= 1
                del self.cache[tail_node.key]
        else:
            # 将这个节点移动到头节点去
            node.value = value
            self._move_to_head(node)

    def _add_to_head(self, node: DLinkNode):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _pop_tail_node(self):
        node = self.tail.prev
        self.remove_node(node)
        return node

    def _move_to_head(self, node):
        self.remove_node(node)
        self._add_to_head(node)

    @classmethod
    def remove_node(cls, node: DLinkNode):
        """
        删除一个节点
        """
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
