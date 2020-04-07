"""
    给定一幅由N × N矩阵表示的图像，其中每个像素的大小为4字节，编写一种方法，将图像旋转90度。
    不占用额外内存空间能否做到？

    示例 1:
        给定 matrix =
        [
          [1,2,3],
          [4,5,6],
          [7,8,9]
        ],

        原地旋转输入矩阵，使其变为:
        [
          [7,4,1],
          [8,5,2],
          [9,6,3]
        ]

    示例 2:
        给定 matrix =
        [
          [ 5, 1, 9,11],
          [ 2, 4, 8,10],
          [13, 3, 6, 7],
          [15,14,12,16]
        ],

        原地旋转输入矩阵，使其变为:
        [
          [15,13, 2, 5],
          [14, 3, 4, 1],
          [12, 6, 8, 9],
          [16, 7,10,11]
        ]
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

    @classmethod
    def solve_1(cls, matrix):
        """
            时间复杂度：N^2
            空间复杂度：N^2
            思路：
                1、旋转90度其实是将第一行挪到倒数第一列，第二行挪到倒数第二列...
                2、构建一个数组  每次重新赋值

        """
        size = len(matrix)

        top = [[0 for i in range(size)] for j in range(size)]

        for i in range(size):
            for j in range(size):
                top[j][size - i - 1] = matrix[i][j]
        matrix[:] = top
