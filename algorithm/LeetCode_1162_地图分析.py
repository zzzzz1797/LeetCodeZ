"""
    你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。
    其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。
    我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。
    如果我们的地图上只有陆地或者海洋，请返回 -1。
"""
from typing import List


class Solution:
    DIRECTION = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def maxDistance(self, grid: List[List[int]]) -> int:
        return self.use_bfs(grid)

    @classmethod
    def use_dfs(cls, grid: List[List[int]]) -> int:
        m = len(grid)
        n = m and len(grid[0])
        res = -1

        def helper(x, y, distance=1):
            if 0 <= x < m and 0 <= y < n and (grid[x][y] == 0 or grid[x][y] > distance):
                grid[x][y] = distance
                for p, q in cls.DIRECTION:
                    helper(p + x, q + y, distance + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    helper(i, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 1:
                    res = max(res, grid[i][j] - 1)
        return res

    @classmethod
    def use_bfs(cls, grid: List[List[int]]) -> int:
        m = len(grid)
        n = m and len(grid[0])

        stack = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    stack.append([i, j, 0])

        if not stack or len(stack) == m * n:
            return -1

        for i, j, d in stack:
            for x, y in cls.DIRECTION:
                dx = x + i
                dy = y + j
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] != 1:
                    grid[dx][dy] = 1
                    stack.append([dx, dy, d + 1])
        return stack[-1][-1]


if __name__ == '__main__':
    Solution.use_dfs([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
