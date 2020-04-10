"""
    假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
    当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的矩阵来表示的。
    例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，
    以此类推。请你计算出粉刷完所有房子最少的花费成本。

    注意：
        所有花费均为正整数。

    示例：
        输入: [[17,2,17],[16,16,5],[14,3,19]]
        输出: 10
        解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成红色。 最少花费: 2 + 5 + 3 = 10。

"""
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        pass

    @classmethod
    def dp_1(cls, costs: List[List[int]]) -> int:
        """
            动态规划：
            dp[i][0] 代表第i减房子刷蓝色的最小成本
            dp[i][1] 代表第i减房子刷绿色的最小成本
            dp[i][2] 代表第i减房子刷红色的最小成本

            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]

            时间复杂度：O(n)
            空间复杂度：O(n)
        """
        res = 0
        if costs:
            size = len(costs)
            dp = [[0, 1, 2] for i in range(size)]

            dp[0][0] = costs[0][0]
            dp[0][1] = costs[0][1]
            dp[0][2] = costs[0][2]

            for i in range(1, size):
                dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
                dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
                dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
            res = min(dp[size - 1][0], dp[size - 1][1], dp[size - 1][2])
        return res

    @classmethod
    def dp_2(cls, costs: List[List[int]]) -> int:
        """
            原理同上
            只是优化了空间复杂度为：O(1)

        """
        res = 0
        if costs:
            blue = costs[0][0]
            green = costs[0][1]
            red = costs[0][2]
            size = len(costs)
            for i in range(1, size):
                new_blue = min(green, red) + costs[i][0]
                new_green = min(blue, red) + costs[i][1]
                new_red = min(blue, green) + costs[i][2]

                blue = new_blue
                green = new_green
                red = new_red

            res = min(blue, green, red)
        return res
