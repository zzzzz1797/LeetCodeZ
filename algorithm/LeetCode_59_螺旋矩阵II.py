"""
    给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
    示例:
        输入: 3
    输出:
        [
         [ 1, 2, 3 ],
         [ 8, 9, 4 ],
         [ 7, 6, 5 ]
        ]
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        pass

    @classmethod
    def solve_1(cls, n: int) -> List[List[int]]:
        """
            固定方向右下左上，
        """
        choices = (
            (0, 1),  # 右
            (1, 0),  # 下
            (0, -1),  # 左
            (-1, 0),  # 上
        )

        flag = row_index = col_index = 0
        res = [[False for i in range(n)] for j in range(n)]
        for index in range(1, n * n + 1):
            res[row_index][col_index] = index
            new_row_index = row_index + choices[flag][0]
            new_col_index = col_index + choices[flag][1]

            if 0 <= new_row_index < n and 0 <= new_col_index < n and not res[new_row_index][new_col_index]:
                row_index = new_row_index
                col_index = new_col_index
            else:
                flag = (flag + 1) % 4
                row_index = row_index + choices[flag][0]
                col_index = col_index + choices[flag][1]

        return res


if __name__ == '__main__':
    print(Solution.solve_1(3))
