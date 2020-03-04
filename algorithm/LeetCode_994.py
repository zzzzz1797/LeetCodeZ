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
    def orangesRotting(self, grid: List[List[int]]) -> int:
        return self.BFS(grid)

    @classmethod
    def BFS(cls, grid: List[List[int]]) -> int:
        # 初始化一些需要的变量

        # 总共多少行
        m = len(grid)
        # 总共多少列
        n = len(grid[0])
        # 用来判断变量是否已经被访问过来了
        visited = [[False] * n for i in range(m)]
        # 总共需要花费多少时间
        minute = 0
        # 坏橘子的集合
        fresh_cnt = sum(1 for j in range(n) for i in range(m) if grid[i][j] == 1)
        stack = [(i, j) for j in range(n) for i in range(m) if grid[i][j] == 2]
        direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]  # 坏橘子腐烂的四个方向

        if not fresh_cnt:
            return 0
        while True:
            new_stack = []
            while stack:
                x, y = stack.pop()  # 拿出一个坏橘子
                for dx, dy in direction:
                    new_x, new_y = dx + x, dy + y
                    if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y] and grid[new_x][new_y] == 1:
                        visited[new_x][new_y] = True
                        grid[new_x][new_y] = 2
                        new_stack.append((new_x, new_y))
                        fresh_cnt -= 1

            if not new_stack:
                break
            stack = new_stack
            minute += 1
        if fresh_cnt:
            return -1
        return minute


if __name__ == "__main__":
    print(Solution().BFS([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
