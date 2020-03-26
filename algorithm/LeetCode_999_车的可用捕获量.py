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
        return self.solve_1(board)

    @classmethod
    def solve_1(cls, board: List[List[str]]) -> int:
        # 定义车的位置 和捕获到卒 的数量
        i = j = cnt = 0

        # 获取棋盘的长度
        length = len(board)

        # 找出车的位置
        for row in range(length):
            for col in range(length):
                if board[row][col] == "R":
                    i = row
                    j = col
                    break

        # 从四个方向出发 判断车可以搞到多少卒
        for tmp_i, tmp_j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_i = i
            new_j = j
            step = 0
            while True:

                print(new_i, new_j)
                if not (0 <= new_i < length and 0 <= new_j < length):
                    break
                target = board[new_i][new_j]
                if target == "B":
                    break

                if target == "p":
                    cnt += 1
                    break

                new_i = tmp_i * step + i
                new_j = tmp_j * step + j
                step += 1
        return cnt


if __name__ == '__main__':
    b = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]

    print(Solution.solve_1(b))
