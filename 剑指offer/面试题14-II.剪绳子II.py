"""
    给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。
    请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
    答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
    示例 1：
        输入: 2
        输出: 1
        解释: 2 = 1 + 1, 1 × 1 = 1
    示例 2:
        输入: 10
        输出: 36
        解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
"""
from functools import lru_cache


class Solution:
    def cuttingRope(self, n: int) -> int:
        return self.recursive(n) % 1000000007

    @classmethod
    @lru_cache(None)
    def recursive(cls, n: int) -> int:
        if n <= 2:
            return 1

        res = 0
        for i in range(1, n):
            res = max(max(i * cls.recursive(n - i), i * (n - i)), res)
        return res

    @classmethod
    def dp_1(cls, n: int) -> int:
        dp = [0] * (n + 1)

        dp[:2] = [1, 1, 1]
        for i in range(3, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], max((i - j) * j, dp[i - j] * j))

        return dp[n]
