"""
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    问总共有多少条不同的路径？

    示例 1:
        输入: m = 3, n = 2
        输出: 3
    解释:
        从左上角开始，总共有 3 条路径可以到达右下角。
        1. 向右 -> 向右 -> 向下
        2. 向右 -> 向下 -> 向右
        3. 向下 -> 向右 -> 向右

    示例 2:
        输入: m = 7, n = 3
        输出: 28
 
    提示：
        1 <= m, n <= 100
        题目数据保证答案小于等于 2 * 10 ^ 9
"""
from typing import Dict


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # return self.recursive_use_memo(m, n, {})
        return self.dp(m, n)

    @classmethod
    def recursive_use_memo(cls, m: int, n: int, memo: Dict) -> int:
        """
            时间复杂度：O(m*n)
            空间复杂度：O(m+n)
        """
        # terminator
        if m < 0 or n < 0:
            return 0
        if m == 1 or n == 1:
            return 1

        # process code logic
        if (m, n) not in memo:
            # drill down
            memo[(m, n)] = cls.recursive_use_memo(m - 1, n, memo) + cls.recursive_use_memo(m, n - 1, memo)
        return memo[(m, n)]

    @classmethod
    def dp(cls, m: int, n: int) -> int:
        """
            时间复杂度：O(m*n)
            空间复杂度： O(1)
        """
        table = [n * [0] for i in range(m)]
        # 初始化
        for i in range(m):
            table[i][0] = 1
        for j in range(n):
            table[0][j] = 1

        # 循环计算
        for i in range(1, m):
            for j in range(1, n):
                table[i][j] = table[i - 1][j]

        return table[m - 1][n - 1]
