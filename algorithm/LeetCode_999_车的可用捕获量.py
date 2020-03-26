"""
    在一个 8 x 8 的棋盘上，有一个白色车（rook）。
    也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。
    它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。

    车按国际象棋中的规则移动：
    它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，
    直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。
    另外，车不能与其他友方（白色）象进入同一个方格。
    返回车能够在一次移动中捕获到的卒的数量。
"""
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        """
            R 代表车
            B 代表白旗
            p 代表卒

            1、遇到B，停止
            2、吃掉一个p，停止
        """
        # 1、初始化变量
        row_index = col_index = None
        cnt = 0

        # 找到i j 的位置
        length = len(board)
        for i in range(length):
            for j in range(length):
                if board[i][j] == 'R':
                    row_index = i
                    col_index = j
                    break
            else:
                continue

        # 从上下左右四个方位开始找
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            step = 0
            while True:
                new_i = row_index + i * step
                new_j = col_index + j * step

                if not (0 <= new_i < length and 0 <= new_j < length):
                    break

                if board[new_i][new_j] == "B":
                    break

                if board[new_i][new_j] == "p":
                    cnt += 1
                    break

                step += 1
        return cnt
