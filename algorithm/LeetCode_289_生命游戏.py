"""
    根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

    给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。
    每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。
    每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

    如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
    如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
    如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
    如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
    根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。
    下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
"""
import copy
from typing import List


class Solution:
    DIRECTION = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        return self.solve_2(board)

    def solve_1(self, board: List[List[int]]):
        m = len(board)
        n = m and len(board[0])

        copy_board = copy.deepcopy(board)

        for row in range(m):
            for col in range(n):
                living_cnt = 0
                for x, y in self.DIRECTION:
                    new_x, new_y = x + row, y + col

                    if 0 <= new_x < m and 0 <= new_y < n and copy_board[new_x][new_y] == 1:
                        living_cnt += 1

                # rule 1
                if living_cnt < 2 and copy_board[row][col] == 1:
                    board[row][col] = 0

                # rule 2
                if living_cnt in (2, 3):

                    # rule 4
                    if living_cnt == 3 and copy_board[row][col] == 0:
                        board[row][col] = 1
                    continue

                # rule 3
                if living_cnt > 3 and board[row][col] == 1:
                    board[row][col] = 0

    def solve_2(self, board: List[List[int]]):
        m = len(board)
        n = m and len(board[0])

        for row in range(m):
            for col in range(n):
                living_cnt = 0

                for x, y in self.DIRECTION:
                    new_x = x + row
                    new_y = y + col

                    if 0 <= new_x < m and 0 <= new_y < n and abs(board[new_x][new_y]) == 1:
                        living_cnt += 1

                # rule1 -1 代表这个细胞过去是活的现在死了
                if board[row][col] == 1 and living_cnt < 2:
                    board[row][col] = -1

                # rule3
                if board[row][col] == 1 and living_cnt > 3:
                    board[row][col] = -1

                # rule2
                if living_cnt in (2, 3):
                    # rule4         # 2 代表这个细胞过去是死的现在活了
                    if board[row][col] == 0 and living_cnt == 3:
                        board[row][col] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
