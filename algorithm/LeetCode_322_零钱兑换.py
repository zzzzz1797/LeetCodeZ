"""
    给定不同面额的硬币 coins 和一个总金额 amount。
    编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

    示例 1:
        输入: coins = [1, 2, 5], amount = 11
        输出: 3
        解释: 11 = 5 + 5 + 1

    示例 2:
        输入: coins = [2], amount = 3
        输出: -1

    说明:
        你可以认为每种硬币的数量是无限的。
"""
from functools import lru_cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.dp(coins, amount)

    @classmethod
    def dp(cls, coins: List[int], amount: int) -> int:
        """
            定义dp数组：dp[i] 表示兑换金额为i需要的最少次数。
            状态转移方程：
                dp[i] = min([dp[i-coin]] for coin in coins) + 1
            时间复杂度：O(Sn)
            空间复杂度：O(S)
            S为金额
            n为面额数
        """
        # 1. 初始化dp数组
        dp = [float("inf") for i in range(amount + 1)]
        dp[0] = 0

        # 2. 遍历amount
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - coin] if i >= coin else float("inf") for coin in coins]) + 1
        return -1 if dp[amount] == float("inf") else dp[amount]

    @classmethod
    def recursive(cls, coins: List[int], amount: int) -> int:
        """
            时间复杂度：O(Sn) S为金额 n是面额数
            空间负载度：O(S) 因为缓存了每个金额的最少兑换次数
        """

        @lru_cache(None)
        def helper(amt):
            """
               helper这个函数的目的是返回兑换这个amt 需要的最少次数
               使用了缓存，缓存每个金额的最少兑换次数，防止重复计算
            """
            # terminator
            if amt == 0:
                # 如果金额等于0，则说明兑换次数也是0
                return 0
            if amt < 0:
                # 如果金额小于0，说明不够兑换（比如 给你2块 让你兑3块 这时amt就是-1）。则根据题目要求返回-1
                return -1

            # 初始化最少次数为无穷大
            res = float("inf")

            # 遍历给定的硬币列表 依次取出来判断
            for coin in coins:
                # 获取子问题的兑换的最少次数，
                sub_problem = helper(amt - coin)
                if sub_problem == -1:
                    # 如果这个子问题返回了-1，说明这个子问题可以抛弃了，因为这个子问题不能完成金额的兑换
                    continue
                # 取子问题和定义的最少次数 的最小值 赋给最少次数。这里的加1是本身也会消耗一枚硬币。
                res = min(res, sub_problem + 1)
            # 判断最少次数是否等于无穷大，如果等于则说明这个金额无解（也就是不能完成金额兑换），返回-1
            return res if res != float("inf") else -1

        return helper(amount)


if __name__ == '__main__':
    Solution().coinChange([1, 2, 5], 100)
