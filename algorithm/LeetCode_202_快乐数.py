"""
    编写一个算法来判断一个数 n 是不是快乐数。
    「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，
    也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

    如果 n 是快乐数就返回 True ；不是，则返回 False 。

 

    示例：
        输入：19
        输出：true
        解释：
            12 + 92 = 82
            82 + 22 = 68
            62 + 82 = 100
            12 + 02 + 02 = 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        return self.solve_2(n)

    @classmethod
    def solve_1(cls, n: int) -> bool:
        used = {n}

        while n != 1:
            n = cls.compute_big_sum(n)
            if n in used:
                return False
            used.add(n)
        return True

    @classmethod
    def solve_2(cls, n: int) -> bool:
        fast = slow = n

        while True:
            slow = cls.compute_big_sum(slow)
            fast = cls.compute_big_sum(fast)
            fast = cls.compute_big_sum(fast)
            if fast == slow:
                break
        return slow == 1

    @classmethod
    def compute_big_sum(cls, n: int) -> int:
        total = 0
        while n > 0:
            curr = n % 10
            total += curr * curr
            n = n // 10
        return total


if __name__ == '__main__':
    print(Solution().solve_2(4))
