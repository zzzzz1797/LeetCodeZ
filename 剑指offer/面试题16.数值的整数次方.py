"""
    实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。
    示例 1:
        输入: 2.00000, 10
        输出: 1024.00000

    示例 2:
        输入: 2.10000, 3
        输出: 9.26100

    示例 3:
        输入: 2.00000, -2
        输出: 0.25000
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        if n == 1:
            return 1

        half = self.myPow(x, n // 2)

        return half * half if n % 2 == 0 else half * half * x
