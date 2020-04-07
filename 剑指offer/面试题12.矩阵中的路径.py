"""
    请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
    路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
    如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

    [["a","b","c","e"],
    ["s","f","c","s"],
    ["a","d","e","e"]]
    但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

    示例 1：
        输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        输出：true
    示例 2：
        输入：board = [["a","b"],["c","d"]], word = "abcd"
        输出：false
    提示：
        1 <= board.length <= 200
        1 <= board[i].length <= 200
"""

from typing import List


class Solution:
    DIRECTION = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.dfs(board, word)

    @classmethod
    def dfs(cls, board: List[List[str]], word: str) -> bool:
        row_size = len(board)
        col_size = row_size and len(board[0])

        def helper(row, col, index):
            # terminal
            if not (0 <= row < row_size and 0 <= col < col_size and word[index] == board[row][col]):
                return False

            if index == len(word) - 1:
                return True

            # code logic
            target = board[row][col]
            # 因为使用过的不允许重复用 所以先更改值
            board[row][col] = "-"
            res = False
            for x, y in cls.DIRECTION:
                new_x, new_y = x + row, y + col
                if helper(new_x, new_y, index + 1):
                    res = True
                    break

            # reverse state
            board[row][col] = target
            return res

        for i in range(row_size):
            for j in range(col_size):
                if helper(i, j, 0):
                    return True
        return False
