"""
    给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。
    转换需遵循如下规则：
        每次转换只能改变一个字母。
        转换过程中的中间单词必须是字典中的单词。

    说明:
        如果不存在这样的转换序列，返回 0。
        所有单词具有相同的长度。
        所有单词只由小写字母组成。
        字典中不存在重复的单词。
        你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

    示例 1:
        输入:
        beginWord = "hit",
        endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]

        输出: 5
        解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
             返回它的长度 5。
    示例 2:
        输入:
            beginWord = "hit"
            endWord = "cog"
            wordList = ["hot","dot","dog","lot","log"]

        输出: 0
"""
from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return self.BFS(beginWord, endWord, wordList)

    @classmethod
    def BFS(cls, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0

        if beginWord and endWord and wordList and endWord in wordList:

            # 转换一下
            beginWord_len = len(beginWord)
            all_combo_dict = defaultdict(list)
            for word in wordList:
                for index in range(beginWord_len):
                    all_combo_dict[word[:index] + "*" + word[index + 1:]].append(word)

            # BFS
            queue = [(beginWord, 1)]
            visited = {beginWord: True}

            while queue:
                current_word, current_level = queue.pop(0)

                for index in range(beginWord_len):
                    for word in all_combo_dict[current_word[:index] + "*" + current_word[index + 1:]]:
                        if word == endWord:
                            return current_level + 1
                        if word not in visited:
                            visited[word] = True
                            queue.append((word, current_level + 1))
        return res
