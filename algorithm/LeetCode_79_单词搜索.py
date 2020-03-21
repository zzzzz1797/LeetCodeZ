"""
    给定一个二维网格和一个单词，找出该单词是否存在于网格中。
    单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
    同一个单元格内的字母不允许被重复使用。

    示例:
        board =
        [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]
        给定 word = "ABCCED", 返回 true
        给定 word = "SEE", 返回 true
        给定 word = "ABCB", 返回 false

    提示：
        board 和 word 中只包含大写和小写英文字母。
        1 <= board.length <= 200
        1 <= board[i].length <= 200
        1 <= word.length <= 10^3
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.dfs(board, word)

    @classmethod
    def dfs(cls, board: List[List[str]], word: str) -> bool:
        word_len = len(word)
        m = len(board)
        n = len(board[0]) if m else 0

        def helper(row_index, col_index, index):
            char = board[row_index][col_index]
            if index == word_len - 1:
                return word[index] == char

            if word[index] == board[row_index][col_index]:
                board[row_index][col_index] = "#"

                for tmp_row_index, tmp_col_index in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    new_row_index = row_index + tmp_row_index
                    new_col_index = col_index + tmp_col_index

                    if 0 <= new_row_index < m and 0 <= new_col_index < n and board[new_row_index][
                        new_col_index] != "#" and helper(new_row_index, new_col_index, index + 1):
                        return True

                board[row_index][col_index] = char

            return False

        for i in range(m):
            for j in range(n):
                if helper(i, j, 0):
                    return True
        return False
