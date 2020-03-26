"""
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
    网格中的障碍物和空位置分别用 1 和 0 来表示。

    说明：m 和 n 的值均不超过 100。

    示例 1:

    输入:
        [
          [0,0,0],
          [0,1,0],
          [0,0,0]
        ]

    输出: 2
    解释:
        3x3 网格的正中间有一个障碍物。
        从左上角到右下角一共有 2 条不同的路径：
        1. 向右 -> 向右 -> 向下 -> 向下
        2. 向下 -> 向下 -> 向右 -> 向右
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            # 开始就有障碍物，直接返回0
            return 0
        return self.dp_1(obstacleGrid)

    @classmethod
    def dp_1(cls, obstacleGrid: List[List[int]]) -> int:
        """
            定义dp数组  dp[i][j] 代表下标为i和j的的最多路径数
            定义状态转移方程：
                dp[i][j] = dp[i+1][j] + dp[i][j-1]

            时间复杂度：
                O(m*n)
            空间复杂度：
                O(m*n)
        """
        row_len = len(obstacleGrid)
        col_len = row_len and len(obstacleGrid[0])

        dp = [[0] * col_len for i in range(row_len)]

        # 初始化dp 因为第一行和第一列的值是可以确定的
        dp[0][0] = 1
        for i in range(1, row_len):
            dp[i][0] = 0 if obstacleGrid[i][0] == 1 else dp[i - 1][0]

        for j in range(1, col_len):
            dp[0][j] = 0 if obstacleGrid[0][j] == 1 else dp[0][j - 1]

        for i in range(1, row_len):
            for j in range(1, col_len):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] if obstacleGrid[i][j] != 1 else 0
        return dp[-1][-1]

    @classmethod
    def dp_2(cls, obstacleGrid: List[List[int]]) -> int:
        """
            优化空间复杂度
                dp_1 中开辟了一个m*n数组，但是在循环遍历的时候，其实只用到当前行的上一行，所以可以加空间复杂度压缩到O(n)

            时间复杂度：
                O(m*n)
            空间复杂度：
                O(n)

        """
        row_len = len(obstacleGrid)
        col_len = row_len and len(obstacleGrid)

        dp = [0] * col_len
        # 初始化一下数组
        dp[0] = 1
        for i in range(1, col_len):
            dp[i] = 0 if obstacleGrid[0][i] == 1 else dp[i - 1]

        for i in range(1, row_len):
            for j in range(col_len):
                target = obstacleGrid[i][j]
                if j == 0:
                    dp[j] = 0 if target == 1 else 1
                else:
                    dp[j] = 0 if target == 1 else dp[j - 1] + dp[j]
        return dp[row_len - 1]

    @classmethod
    def dp_3(cls, obstacleGrid: List[List[int]]) -> int:
        """
        相对于dp_2来说，继续压缩空间复杂度，复用给定的数组，则空间复杂度可以下降到O(1)。但是破坏了给定数组的内容。
        时间复杂度：
            O(m*n)
        空间复杂度：
            O(1)
        """
        row_len = len(obstacleGrid)
        col_len = row_len and len(obstacleGrid[0])

        obstacleGrid[0][0] = 1

        for i in range(1, row_len):
            obstacleGrid[i][0] = 0 if obstacleGrid[i][0] == 1 else obstacleGrid[i - 1][0]

        for j in range(1, col_len):
            obstacleGrid[0][j] = 0 if obstacleGrid[0][j] == 1 else obstacleGrid[0][j - 1]

        for i in range(1, row_len):
            for j in range(1, col_len):
                obstacleGrid[i][j] = 0 if obstacleGrid[i][j] == 1 else obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[-1][-1]
