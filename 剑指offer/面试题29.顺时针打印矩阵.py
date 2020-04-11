"""
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
    示例 1：
        输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
        输出：[1,2,3,6,9,8,7,4,5]

    示例 2：
        输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        输出：[1,2,3,4,8,12,11,10,9,5,6,7]
    限制：
        0 <= matrix.length <= 100
        0 <= matrix[i].length <= 100
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
            思路：
                1、定义上先左右四个边界  上 t  下b  左l 右r
                2、按照顺时针打印
        """
        row_size = len(matrix)
        col_size = row_size and len(matrix[0])
        res = []

        l = 0
        r = col_size - 1
        t = 0
        b = row_size - 1
        while True:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break

            for j in range(t, b + 1):
                res.append(matrix[j][r])
            r -= 1
            if l > r:
                break

            for x in range(r, l - 1, -1):
                res.append(matrix[b][x])
            b -= 1
            if t > b:
                break

            for z in range(b, t - 1, -1):
                res.append(matrix[z][l])
            l += 1
            if l > r:
                break
        return res


if __name__ == '__main__':
    print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
