"""
    给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

    示例 1:
        输入:
        [
          [1,1,1],
          [1,0,1],
          [1,1,1]
        ]
        输出:
        [
          [1,0,1],
          [0,0,0],
          [1,0,1]
        ]

    示例 2:
        输入:
        [
          [0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]
        ]
        输出:
        [
          [0,0,0,0],
          [0,4,5,0],
          [0,3,1,0]
        ]

    进阶:
        一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
        一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
        你能想出一个常数空间的解决方案吗？
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        return self.directly_1(matrix)

    @classmethod
    def directly_1(cls, matrix: List[List[int]]) -> None:
        """
            暴力解决：
                1、先生成两个set，用来保存需要置0的行和列
                2、先遍历整个矩阵。如果元素的值是0，则将元素的行和列的下标分别添加到1的两个集合中。
                3、再遍历一侧矩阵，根据需要置0的行和列进行实际操作。
            时间复杂度：O(m*n) m为矩阵的行数 n为矩阵的列数
            空间复杂度：O(m+n)
        """
        if matrix:
            # 初始化
            col_set = set()
            row_set = set()
            row_len = len(matrix)
            col_len = len(matrix[0])

            # 遍历整个矩阵
            for row in range(row_len):
                for col in range(col_len):
                    if matrix[row][col] == 0:
                        col_set.add(col)
                        row_set.add(row)

            # 再遍历一次 更改值
            for row in range(row_len):
                for col in range(col_len):
                    if row in row_set or col in col_set:
                        matrix[row][col] = 0

    @classmethod
    def directly_2(cls, matrix: List[List[int]]) -> None:
        """
        """
        first_row_need_change = False
        first_col_need_change = False

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_need_change = True
                    if j == 0:
                        first_col_need_change = True

                    matrix[i][0] = 0
                    matrix[0][j] = 0
