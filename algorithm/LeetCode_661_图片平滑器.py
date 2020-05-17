"""
    包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

    示例 1:

        输入:
            [[1,1,1],
             [1,0,1],
             [1,1,1]]
        输出:
            [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
        解释:
            对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
            对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
            对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
    注意:
    给定矩阵中的整数范围为 [0, 255]。
    矩阵的长和宽的范围均为 [1, 150]。
"""
from typing import List


class Solution:
    choices = (
        (1, 0),
        (0, 1),
        (0, -1),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
        (0, 0),
    )

    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        pass

    @classmethod
    def solve_1(cls, M: List[List[int]]) -> List[List[int]]:
        row_size = len(M)
        col_size = len(M[0])
        res = [[0 for j in range(col_size)] for i in range(row_size)]

        for i in range(row_size):
            for j in range(col_size):
                count = 0

                for tmp_i, tmp_j in cls.choices:
                    new_i = tmp_i + i
                    new_j = tmp_j + j

                    if 0 <= new_i < row_size and 0 <= new_j < col_size:
                        res[i][j] += M[new_i][new_j]
                        count += 1
                res[i][j] //= count
        return res
