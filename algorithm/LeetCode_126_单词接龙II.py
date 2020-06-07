"""
    给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。
    转换需遵循如下规则：
        每次转换只能改变一个字母。
        转换过程中的中间单词必须是字典中的单词。

    说明:
        如果不存在这样的转换序列，返回一个空列表。
        所有单词具有相同的长度。
        所有单词只由小写字母组成。
        字典中不存在重复的单词。
        你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
    示例 1:
        输入:
            beginWord = "hit",
            endWord = "cog",
            wordList = ["hot","dot","dog","lot","log","cog"]

        输出:
            [
              ["hit","hot","dot","dog","cog"],
              ["hit","hot","lot","log","cog"]
            ]

    示例 2:
        输入:
            beginWord = "hit"
            endWord = "cog"
            wordList = ["hot","dot","dog","lot","log"]

        输出: []
"""
from collections import deque, defaultdict
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        return self.solve_1(beginWord, endWord, wordList)

    @classmethod
    def solve_1(cls, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        size = len(begin_word)

        # 1. 先将word_list 构建成一个模糊单词的映射关系表
        word_dict = defaultdict(list)
        for word in word_list:
            for index in range(size):
                blur_word = word[:index] + "*" + word[index + 1:]
                word_dict[blur_word].append(word)
        # 2. 广度有限遍历
        queue = deque([(begin_word, 1)])
        founded = {begin_word: 1}
        pre_words = defaultdict(list)
        while queue:
            cur_word, cur_level = queue.popleft()
            for i in range(size):
                blur_word = cur_word[:i] + "*" + cur_word[i + 1:]
                for word in word_dict.get(blur_word, []):
                    if word not in founded:
                        founded[word] = cur_level + 1
                        queue.append((word, cur_level + 1))
                    if founded[word] == cur_level + 1:
                        pre_words[word].append(cur_word)
            if end_word in founded and cur_level + 1 > founded[end_word]:
                break
        if end_word in founded:
            res = [[end_word]]

            while res[0][0] != begin_word:
                res = [[word] + r for r in res for word in pre_words[r[0]]]
            return res
        return []


if __name__ == '__main__':
    print(Solution.solve_1("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
