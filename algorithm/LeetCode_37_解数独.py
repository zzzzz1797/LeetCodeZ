"""
    编写一个程序，通过已填充的空格来解决数独问题。
    一个数独的解法需遵循如下规则：
        数字 1-9 在每一行只能出现一次。
        数字 1-9 在每一列只能出现一次。
        数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
        空白格用 '.' 表示。
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # init
        rows = [set(range(1, 10)) for i in range(9)]
        cols = [set(range(1, 10)) for i in range(9)]
        blocks = [set(range(1, 10)) for i in range(9)]

        # prepare
        emtpy = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    # update rows cols blocks
                    val = int(board[i][j])
                    rows[i].remove(val)
                    cols[j].remove(val)
                    blocks[self.find_block_index(i, j)].remove(val)
                else:
                    emtpy.append((i, j))

        def back_track(index=0):
            # terminator
            if index == len(emtpy):
                return True

            # process
            row_index, col_index = emtpy[index]
            block_index = self.find_block_index(row_index, col_index)

            for target in rows[row_index] & cols[col_index] & blocks[block_index]:
                rows[row_index].remove(target)
                cols[col_index].remove(target)
                blocks[block_index].remove(target)

                board[row_index][col_index] = str(target)
                # drill down
                if back_track(index + 1):
                    return True

                # reverse state
                rows[row_index].add(target)
                cols[col_index].add(target)
                blocks[block_index].add(target)

            return False

        back_track()

    @staticmethod
    def find_block_index(row_index: int, col_index: int) -> int:
        return (row_index // 3) * 3 + col_index // 3
