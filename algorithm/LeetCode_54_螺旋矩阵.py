"""
    给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

    示例 1:
        输入:
        [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
        输出: [1,2,3,6,9,8,7,4,5]

    示例 2:
        输入:
        [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12]
        ]
        输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass

    @classmethod
    def solve_1(cls, matrix: List[List[int]]) -> List[int]:
        """
            绘制螺旋轨迹路径，我们发现当路径超出界限或者进入之前访问过的单元格时，会顺时针旋转方向。
        """
        res = []
        if matrix:
            row_size = len(matrix)
            col_size = len(matrix[0])
            visited = [[False for j in range(col_size)] for i in range(row_size)]

            dr = [0, 1, 0, -1]
            dc = [1, 0, -1, 0]

            r = c = di = 0
            for i in range(row_size * col_size):
                res.append(matrix[r][c])
                visited[r][c] = True

                cr = r + dr[di]
                cc = c + dc[di]

                if 0 <= cr < row_size and 0 <= cc < col_size and not visited[cr][cc]:
                    r = cr
                    c = cc
                else:
                    di = (di + 1) % 4
                    r = r + dr[di]
                    c = c + dc[di]
        return res
