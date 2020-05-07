"""
    在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
    示例:
        输入:
            1 0 1 0 0
            1 0 1 1 1
            1 1 1 1 1
            1 0 0 1 0
        输出: 4
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        pass

    def solve(self, matrix: List[List[str]]) -> int:
        """
            dp[i][j] = (dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            dp[i][j]表示当右下角为1时，正方形的最大面积
        """

        row_size = len(matrix)
        col_size = row_size and len(matrix[0])

        dp = [[0 for j in range(row_size)] for i in range(col_size)]

        side = 0
        for i in range(1, row_size + 1):
            for j in range(1, row_size + 1):
                if matrix[i][j] == 1:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    side = max(side, dp[i][j])
        return side * side
