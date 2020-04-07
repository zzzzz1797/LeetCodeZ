"""
    在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
    你可以从棋盘的左上角开始拿格子里的礼物，
    并每次向右或者向下移动一格、直到到达棋盘的右下角。
    给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

    示例 1:
        输入:
        [
          [1,3,1],
          [1,5,1],
          [4,2,1]
        ]
        输出: 12
        解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
        提示：
            0 < grid.length <= 200
            0 < grid[0].length <= 200
"""

from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        return self.dp_1(grid)

    @classmethod
    def dp_2(cls, grid: List[List[int]]) -> int:
        """
            时间复杂度和dp_1一样
            空间复杂度：O(1)

        """
        row_size = len(grid)
        col_size = len(grid[0])

        for i in range(row_size):
            for j in range(col_size):
                if i != 0 and j != 0:
                    if i == 0 and j != 0:
                        grid[i][j] = grid[i][j - 1] + grid[i][j]
                    elif i != 0 and j == 0:
                        grid[i][j] = grid[i - 1][j] + grid[i][j]
                    else:
                        grid[i][j] = max(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]

    @classmethod
    def dp_1(cls, grid: List[List[int]]) -> int:
        """
            动态规划 dp[i,j] 代表下标为i j时能拿到的最多价值的礼物。
            dp[i, j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

            当i=0,j=0时: dp[i][j] = grid[i][j]
            当i=0,j!=0时：dp[i][j] = dp[i][j-1] + grid[i][j]
            当i!=0,j=0时：dp[j][j] = dp[i-1][j] + grid[i][j]
            当i!=0,j!=0时， dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            时间复杂度：O（m*n）
            空间复杂度：O(m*n)
        """
        row_size = len(grid)
        col_size = len(grid[0])

        dp = [[0 for i in range(col_size)] for j in range(row_size)]

        for i in range(row_size):
            for j in range(col_size):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]
