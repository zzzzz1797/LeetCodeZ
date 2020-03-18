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

        # 1. 初始化数据
        rows, cols, blocks = self.init_data()

        # 2. 循环遍历board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    # 表示需要验证这个数字

                    # 将获取块索引的计算抽出来作为一个方法
                    block_index = self.get_block_index(i, j)

                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    blocks[block_index][num] = blocks[block_index].get(num, 0) + 1

                    # 判断上述赋值操作之后得到的结果是否合法
                    if rows[i][num] > 1 or cols[j][num] > 1 or blocks[block_index][num] > 1:
                        return False
        return True

        pass

    @classmethod
    def init_data(cls):
        rows = []
        cols = []
        blocks = []

        for i in range(9):
            rows.append({})
            cols.append({})
            blocks.append({})

        return rows, cols, blocks

    @classmethod
    def get_block_index(cls, row_index, col_index) -> int:
        return (row_index // 3) * 3 + col_index // 3