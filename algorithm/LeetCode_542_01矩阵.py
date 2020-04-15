"""
    给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
    两个相邻元素间的距离为 1 。
    示例 1:
        输入:
        0 0 0
        0 1 0
        0 0 0
    输出:
        0 0 0
        0 1 0
        0 0 0

    示例 2:
        输入:
            0 0 0
            0 1 0
            1 1 1
        输出:
            0 0 0
            0 1 0
            1 2 1
"""
from typing import List


class Solution:
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        pass

    @classmethod
    def bfs(cls, matrix: List[List[int]]) -> List[List[int]]:
        row_size = len(matrix)
        col_size = row_size and len(matrix[0])

        res = [[0 for j in range(col_size)] for i in range(row_size)]

        # 将所有的0 添加到队列中
        queue = []
        for i in range(row_size):
            for j in range(col_size):
                if matrix[i][j] == 0:
                    queue.append((i, j))
        visited = set()
        while queue:
            tmp_queue = []

            for x, y in queue:
                for new_x, new_y in cls.direction:
                    dx = new_x + x
                    dy = new_y + y
                    if 0 <= dx < row_size and 0 <= dy < col_size and (dx, dy) not in visited and matrix[dx][dy] != 0:
                        visited.add((dx, dy))
                        res[dx][dy] = res[x][y] + 1
                        tmp_queue.append((dx, dy))
            queue = tmp_queue
        return res

    @classmethod
    def dp(cls, matrix: List[List[int]]) -> List[List[int]]:
        """
            dp[i][j] 代表matrix[i][j]距离0的最近距离
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1  if matrix[i][j] !=0
            dp[i][j] = 0                    if matrix[i][j]==0
        """
        row_size = len(matrix)
        col_size = row_size and len(matrix[0])
        dp = [[float("inf") for i in range(col_size)] for j in range(row_size)]

        # 初始化数据
        for i in range(row_size):
            for j in range(col_size):
                if matrix[i][j] == 0:
                    dp[i][j] = 0

        for i in range(row_size):
            for j in range(col_size):
                if i - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

        for i in range(row_size - 1, -1, -1):
            for j in range(col_size - 1, -1, -1):
                if i + 1 < row_size:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j + 1 < col_size:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        return dp
    #
    # @classmethod
    # def dfs(cls, matrix: List[List[int]]) -> List[List[int]]:
    #     row_size = len(matrix)
    #     col_size = len(matrix[0])
    #     res = [[float("inf") for i in range(col_size)] for i in range(row_size)]
    #
    #     def helper(x, y, distance, visited) -> int:
    #         if matrix[x][y] == 0:
    #             return distance
    #
    #         tmp_res = float("inf")
    #         for new_x, new_y in cls.direction:
    #             dx = new_x + x
    #             dy = new_y + y
    #
    #             if 0 <= dx < row_size and 0 <= dy < col_size and (dx, dy) not in visited:
    #                 visited.add((dx, dy))
    #                 tmp_res = min(tmp_res, helper(dx, dy, distance + 1, visited))
    #         return tmp_res
    #
    #     for i in range(row_size):
    #         for j in range(col_size):
    #             res[i][j] = helper(i, j, 0, set())
    #     return res


if __name__ == '__main__':
    print(Solution().bfs([[1, 1, 1], [0, 1, 0], [1, 1, 1]]))
    print(Solution().dfs([[1, 1, 1], [0, 1, 0], [1, 1, 1]]))
