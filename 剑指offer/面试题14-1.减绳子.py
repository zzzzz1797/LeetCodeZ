"""
    给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。
    请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

    示例 1：
        输入: 2
        输出: 1
        解释: 2 = 1 + 1, 1 × 1 = 1
    示例 2:
        输入: 10
        输出: 36
        解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

    提示：
        2 <= n <= 58
"""
from functools import lru_cache


class Solution:
    def cuttingRope(self, n: int) -> int:
        return self.recursive(n)

    @lru_cache(None)
    def recursive(cls, n: int) -> int:
        """
            递归的推导式：f(n) = max(i*(n-i), i*f(n-i)) ) 1<=i<=n-1
            i*(n-i)  代表剩下绳子可以不减
            i*f(n-i) 代表剩下绳子要减
            时间复杂度：O(n^2)
            空间复杂度：O(n^2)
        """
        if n == 2:
            return 1
        res = 0
        for i in range(1, n):
            res = max(max(i * cls.recursive(n - i), i * (n - i)), res)
        return res

    @classmethod
    def dp(cls, n: int):
        """
            动态规划
            dp[i]  表示长度为i是的最大乘积
            dp[1] = 1
            dp[2] = 1

            dp[i] = max(dp[i], max((i-j)*j, j*dp[i-j]))
            时间复杂度：O(n^2)
            空间复杂度：O(n)
        """
        res = 1
        if n >= 2:
            dp = [0] * (n + 1)
            dp[1] = 1
            dp[2] = 1
            for i in range(3, n + 1):
                for j in range(i):
                    dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))
            res = dp[n]
        return res

    @classmethod
    def dp_1(cls, n: int):
        """
            任何大于3的数都可以拆分为数字 1，2，3的和，且它们对 3 的余数总是 0，1，2。
            时间复杂度：O(n)
            空间复杂度：O(1)

        """
        dp = [0, 1, 1]

        for i in range(3, n + 1):
            dp[i % 3] = max(
                1 * max(dp[(i - 1) % 3], i - 1),
                2 * max(dp[(i - 2) % 3], i - 2),
                3 * max(dp[(i - 3) % 3], i - 3)
            )

        return dp[n % 3]


if __name__ == '__main__':
    print(Solution().dp_1(10))
