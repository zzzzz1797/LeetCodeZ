"""
    统计所有小于非负整数 n 的质数的数量。
    示例:
        输入: 10
        输出: 4
        解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        pass

    @classmethod
    def solve_1(cls, n: int) -> int:
        """
            厄拉多塞筛法：要得到自然数n以内的全部质数，必须把不大于根号n的所有质数的倍数剔除，剩下的就是质数。
            算术基本定理：任何一个合数(非质数)，都可以以唯一的形式被写成有限个质数的乘积，即分解质因数。
        """
        pass
        if n < 2:
            return 0
        is_prime = [1] * n

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                is_prime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)
        return sum(is_prime)
