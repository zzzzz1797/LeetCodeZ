"""
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

    示例 1:
        输入: [7,1,5,3,6,4]
        输出: 7
        解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
             随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

    示例 2:
        输入: [1,2,3,4,5]
        输出: 4
        解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
             注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
             因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
    示例 3:
        输入: [7,6,4,3,1]
        输出: 0
        解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.greedy(prices)

    @classmethod
    def dp_1(cls, prices: List[int]) -> int:
        """
            dp[i][j]
            i 表示 第i天能获得的最大的利润
            j 取值 0， 1
                0 代表 第i天时，不持有
                1 代表 第i天时，持有

                dp[i][0] 表示第i天不持有，则有两种情况
                    1、第i-1天就不持有
                    2、第i-1天持有，但是第i天卖了
                    取两者之间的最大值就是dp[i][0]的最大利润

                dp[i][1] 表示第i天持有，两种情况
                    1、第i-1天就持有
                    2、第i-1天不持有，但是第i天买了
        """
        res = 0
        if size := len(prices):
            dp = [[0, 0] for i in range(size)]
            dp[0][0] = 0
            dp[0][1] = -prices[0]
            for i in range(1, size):
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            res = dp[-1][0]
        return res

    @classmethod
    def greedy(cls, prices: List[int]) -> int:
        res = 0
        size = len(prices)
        for index in range(1, size):
            if prices[index] > prices[index - 1]:
                res += prices[index] - prices[index - 1]
        return res


if __name__ == '__main__':
    print(Solution.dp_1([7, 1, 5, 3, 6, 4]))
