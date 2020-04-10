"""
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

    注意：你不能在买入股票前卖出股票。
    示例 1:
        输入: [7,1,5,3,6,4]
        输出: 5
        解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
             注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
    示例 2:
        输入: [7,6,4,3,1]
        输出: 0
        解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.dp_2(prices)

    @classmethod
    def dp_1(cls, prices: List[int]) -> int:
        """
            dp[i] 代表第i天能获取的最大利润
            dp[i] = max(dp[i-1], prices[i]-min_price)
            时间复杂度：O(n)
            空间复杂度：O(n)
        """
        res = 0

        if prices:
            size = len(prices)
            dp = [0] * size
            min_price = float("inf")

            for i in range(size):
                min_price = min(min_price, prices[i])
                dp[i] = max(dp[i], prices[i] - min_price)
                res = max(res, dp[i])
        return res

    @classmethod
    def dp_2(cls, prices: List[int]) -> int:
        res = 0
        first = float("inf")
        size = len(prices)
        second = 0

        for i in range(size):
            first = min(prices[i], first)
            second = max(second, prices[i] - first)
            res = max(res, second)
        return res


if __name__ == '__main__':
    print(Solution().dp_2([7, 1, 5, 3, 6, 4]))
