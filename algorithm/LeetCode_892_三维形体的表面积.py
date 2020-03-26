"""
    在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
    每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
    请你返回最终形体的表面积。
    示例 1：
        输入：[[2]]
        输出：10

    示例 2：
        输入：[[1,2],[3,4]]
        输出：34

    示例 3：
        输入：[[1,0],[0,2]]
        输出：16

    示例 4：
        输入：[[1,1,1],[1,0,1],[1,1,1]]
        输出：32

    示例 5：
        输入：[[2,2,2],[2,1,2],[2,2,2]]
        输出：46
    提示：
        1 <= N <= 50
        0 <= grid[i][j] <= 50
"""
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        res = 0
        length = len(grid)

        for i in range(length):
            for j in range(length):
                if grid[i][j]:
                    res += 2

                    for tmp_i, tmp_j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        new_i = i + tmp_i
                        new_j = j + tmp_j

                        if 0 <= new_i < length and 0 <= new_j < length:
                            tmp_res = grid[new_i][new_j]
                        else:
                            tmp_res = 0
                        res += max(0, grid[i][j] - tmp_res)
        return res



if __name__ == '__main__':
    print(Solution().surfaceArea([[1, 5], [6, 7]]))
