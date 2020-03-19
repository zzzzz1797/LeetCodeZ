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
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return self.bfs(grid)

    @classmethod
    def dfs(cls, grid: List[List[int]]) -> int:
        """
        深度优先遍历

            时间复杂度：O(R * C)。其中 R 是给定网格中的行数，C 是列数。我们访问每个网格最多一次。
            空间复杂度：O(R * C)，递归的深度最大可能是整个网格的大小，因此最大可能使用 O(R * C)的栈空间。
            每次从当前位置的对应的上下左右触发，如果碰到不符合条件的返回0
        """

        def helper(row_index: int, col_index: int) -> int:
            # terminator
            if not Solution.check_row_and_col_invalid(grid, row_index, col_index):
                return 0

            # 这组下标的内容置成0
            grid[row_index][col_index] = 0

            ret = 1
            for tmp_row_index, tmp_col_index in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                new_row_index = row_index + tmp_row_index
                new_col_index = col_index + tmp_col_index

                if Solution.check_row_and_col_invalid(grid, new_row_index, new_col_index):
                    ret += helper(new_row_index, new_col_index)
            return ret

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, helper(i, j))
        return res

    @classmethod
    def bfs(cls, grid: List[List[int]]) -> int:
        """
            广度优先遍历
            思路和上面的一样
        """
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur = 0
                queue = [(i, j)]
                while queue:
                    cur_i, cur_j = queue.pop()
                    if cls.check_row_and_col_invalid(grid, cur_i, cur_j):
                        grid[cur_i][cur_j] = 0
                        cur += 1

                        for tmp_i, tmp_j in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                            new_i = cur_i + tmp_i
                            new_j = cur_j + tmp_j
                            queue.append((new_i, new_j))
                res = max(cur, res)
        return res

    @classmethod
    def check_row_and_col_invalid(cls, grid: List[List[int]], row_index: int, col_index: int) -> bool:
        res = False

        row_len = len(grid)
        col_len = len(grid[0]) if grid else 0

        if 0 <= row_index < row_len and 0 <= col_index < col_len and grid[row_index][col_index] == 1:
            res = True
        return res
