"""
    在给定的网格中，每个单元格可以有以下三个值之一：
        值 0 代表空单元格；
        值 1 代表新鲜橘子；
        值 2 代表腐烂的橘子。
    每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
    返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

    示例 1：
        输入：[[2,1,1],[1,1,0],[0,1,1]]
        输出：4

    示例 2：
        输入：[[2,1,1],[0,1,1],[1,0,1]]
        输出：-1
        解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。

    示例 3：
        输入：[[0,2]]
        输出：0
        解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
 
    提示：
        1 <= grid.length <= 10
        1 <= grid[0].length <= 10
        grid[i][j] 仅为 0、1 或 2
"""
from typing import List


class Solution:
    DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        return self.bfs(grid)

    @classmethod
    def bfs(cls, grid):
        minutes = 0
        row_size = len(grid)
        col_size = row_size and len(grid[0])

        fresh_cnt = sum([1 for j in range(col_size) for i in range(row_size) if grid[i][j] == 1])
        if fresh_cnt:
            queue = [(i, j) for j in range(col_size) for i in range(row_size) if grid[i][j] == 2]
            while queue:
                tmp_queue = []

                for x, y in queue:
                    for tmp_x, tmp_y in cls.DIRECTION:
                        new_x = x + tmp_x
                        new_y = y + tmp_y
                        if 0 <= new_x < row_size and 0 <= new_y < col_size and grid[new_x][new_y] == 1:
                            tmp_queue.append([new_x, new_y])
                            grid[new_x][new_y] = 2
                            fresh_cnt -= 1
                queue = tmp_queue
                if queue:
                    minutes += 1

        return minutes if not fresh_cnt else -1


if __name__ == "__main__":
    print(Solution().bfs([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    print(Solution().bfs([[0, 2]]))
    print(Solution().bfs([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
