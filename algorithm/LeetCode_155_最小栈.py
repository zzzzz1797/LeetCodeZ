"""
    设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
    push(x) —— 将元素 x 推入栈中。
    pop() —— 删除栈顶的元素。
    top() —— 获取栈顶元素。
    getMin() —— 检索栈中的最小元素。
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ori_stack = []  # 用来存储总数据
        self.min_stack = []

    def push(self, x: int) -> None:
        self.ori_stack.append(x)
        if self.min_stack and self.getMin() < x:
            self.min_stack.append(self.getMin())
        else:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.min_stack:
            self.min_stack.pop()
            self.ori_stack.pop()

    def top(self) -> int:
        if self.ori_stack: return self.ori_stack[-1]

    def getMin(self) -> int:
        if self.min_stack: return self.min_stack[-1]
