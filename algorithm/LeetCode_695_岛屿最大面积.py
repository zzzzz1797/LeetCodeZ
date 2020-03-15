"""
    给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。
    你可以假设二维矩阵的四个边缘都被水包围着。
    找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

    示例 1:

        [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。
    示例 2:
        [[0,0,0,0,0,0,0,0]]

    对于上面这个给定的矩阵, 返回 0。
    注意: 给定的矩阵grid 的长度和宽度都不超过 50。
"""
from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return self.bfs(grid)

    @classmethod
    def dfs(cls, grid: List[List[int]]) -> int:
        """
        深度优先遍历

            时间复杂度：O(R * C)。其中 RR 是给定网格中的行数，CC 是列数。我们访问每个网格最多一次。
            空间复杂度：O(R * C)，递归的深度最大可能是整个网格的大小，因此最大可能使用 O(R * C)O(R∗C) 的栈空间。
            每次从当前位置的对应的上下左右触发，如果碰到不符合条件的返回0
        """
        def helper(i, j):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            ans = 1
            for tmp_i, tmp_j in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                new_i = i + tmp_i
                new_j = j + tmp_j
                ans += helper(new_i, new_j)
            return ans

        res = 0
        if grid:
            m = len(grid)
            n = len(grid[0])
            for row in range(m):
                for col in range(n):
                    res = max(res, helper(row, col))
        return res

    @classmethod
    def bfs(cls, grid: List[List[int]]) -> int:
        """
            广度优先遍历
            思路和上面的一样
        """
        res = 0

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                cur = 0
                q = deque([(i, j)])
                while q:
                    cur_i, cur_j = q.popleft()
                    if cur_i < 0 or cur_j < 0 or cur_i == m or cur_j == n or grid[cur_i][cur_j] == 0:
                        continue
                    cur += 1
                    grid[cur_i][cur_j] = 0

                    for tmp_i, tmp_j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        next_i = tmp_i + cur_i
                        next_j = tmp_j + cur_j
                        q.append((next_i, next_j))
                res = max(res, cur)
        return res
