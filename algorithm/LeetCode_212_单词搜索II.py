"""
    给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
    单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

    示例:

        输入:
        words = ["oath","pea","eat","rain"] and board =
            [
              ['o','a','a','n'],
              ['e','t','a','e'],
              ['i','h','k','r'],
              ['i','f','l','v']
            ]

        输出: ["eat","oath"]
        说明:
        你可以假设所有输入都由小写字母 a-z 组成。
"""
from typing import List


class Solution:
    end_flag = "#"

    def __init__(self):
        self.row_size = 0
        self.col_size = 0
        self.board = None
        self.res = []

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. 初始化一些变量
        self.row_size = len(board)
        self.col_size = self.row_size and len(board[0])
        self.board = board

        # 2. 根据words构建一个trie树
        trie = self.build_trie(words)

        # 3. 循环
        for i in range(self.row_size):
            for j in range(self.col_size):
                self.dfs(i, j, trie)

        # 4. 去重
        return list(set(self.res))

    def dfs(self, row_index, col_index, trie, tmp_str=""):
        ch = self.board[row_index][col_index]
        if ch not in trie:
            return
        tmp_str += ch
        trie = trie[ch]
        if self.end_flag in trie:
            self.res.append(tmp_str)

        self.board[row_index][col_index] = self.end_flag

        for x, y in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            new_x = x + row_index
            new_y = y + col_index
            if 0 <= new_x < self.row_size and 0 <= new_y < self.col_size and self.board[new_x][new_y] != self.end_flag:
                self.dfs(new_x, new_y, trie, tmp_str)

        self.board[row_index][col_index] = ch

    @classmethod
    def build_trie(cls, words: List[str]):
        trie = {}

        for word in words:
            root = trie
            for ch in word:
                root = root.setdefault(ch, {})
            root[cls.end_flag] = cls.end_flag
        return trie
