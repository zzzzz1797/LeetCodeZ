"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
数独部分空格内已填入了数字，空白格用 '.' 表示。

说明:
    一个有效的数独（部分已被填充）不一定是可解的。
    只需要根据以上规则，验证已经填入的数字是否有效即可。
    给定数独序列只包含数字 1-9 和字符 '.' 。
    给定数独永远是 9x9 形式的。
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
            条件：
                1、一行内不能出现重复的数字
                2、一列内不能出现重复的数字
                3、一块内不能出现重复的数字（row //3） 3 + col
        """
        # 先生成三个set
        m = len(board)
        blocks = []
        rows = []
        cols = []
        for i in range(m):
            blocks.append(set())
            rows.append(set())
            cols.append(set())

        for i in range(m):
            for j in range(m):
                check_num = board[i][j]
                if check_num != ".":
                    block_size = self.find_block_index(i, j)

                    block_set = blocks[block_size]
                    row_set = rows[i]
                    col_set = cols[j]

                    if check_num in block_set or check_num in row_set or check_num in col_set:
                        return False

                    block_set.add(check_num)
                    row_set.add(check_num)
                    col_set.add(col_set)

    @staticmethod
    def find_block_index(row_index, col_index) -> int:
        return (row_index // 3) * 3 + col_index // 3
