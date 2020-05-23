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
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass
